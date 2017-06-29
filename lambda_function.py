"""
This skill is a demo for the Girls Who Code visit to CNN.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as how to open the skill are in https://github.com/cnnlabs/gwc-demo.

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome, Girls Who Code"
    speech_output = "<speak>Hello - welcome Girls Who Code, to CNN. <break time='0.5s'/> an-cay ou-yay eak-spay ig-pay atin-lay?</speak>"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "<speak>haaa haaaa, you don't speak Pig Latin I guess... Say anything, and I will translate for you!</speak>"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Goodbye, let's play again soon!"
    speech_output = "oodbyegay, et'slay ayplay againway oonsay! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def translate_pig_latin(intent, session):
    """ Takes what a user says and sends to function that
        translates into pig latin. If we don't get a PHRASE value,
        we need to let the user know.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'PHRASE' in intent['slots']:
        phrase = intent['slots']['PHRASE']['value']
        print(phrase)
        sound_clip = "<speak><audio src='https://a.cnnlabs.com/show-assets/dev/shows/test/gwc/dial-up.mp3'></audio>"
        speech_output = sound_clip + \
                        "<break time='2s'/>" + \
                        translator(phrase) + \
                        ". Tell me another phrase </speak> "
        reprompt_text = "<speak>Say another phrase if you want me to translate it</speak> " 
    else:
        speech_output = "<speak>I'm sorry I didn't get that. Can you say it again?</speak>"
        reprompt_text = "<speak>I don't understand. What did you say?</speak>"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def translator(phrase):
        """ Takes what a user says and translates into pig latin."""
        lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
        phrase = phrase.lower().split()
        for k in range(len(phrase)):
                i = phrase[k]
                print(i)
                if i[0] in ['a', 'e', 'i', 'o', 'u']:
                        phrase[k] = i+'ay'
                elif t(i) in lst:
                        phrase[k] = i[2:]+i[:2]+'ay'
                        print(phrase[k])
                elif i.isalpha() == False:
                        phrase[k] = i
                else:
                        phrase[k] = i[1:]+i[0]+'ay'
        return ' '.join(phrase)


def t(str):
        print(str)
        return str[0]+str[1]



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "PigLatinIntent":
        return translate_pig_latin(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
