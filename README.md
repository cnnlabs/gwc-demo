# Girls Who Code Demo
This repo contains the starter files to get up and running with a Pig Latin Alexa Skill using a Python Lambda Function + the Amazon Developer console for skills.


## How to use:
1. [Setup your AWS Lambda](https://github.com/cnnlabs/gwc-demo#setup-your-aws-lambda)
2. [Setup your Alexa Skill](https://github.com/cnnlabs/gwc-demo#setup-your-alexa-skill)


## Setup your AWS Lambda
[![Watch the video](https://a.cnnlabs.com/show-assets/dev/shows/test/gwc/lambda.png)](https://a.cnnlabs.com/show-assets/dev/shows/test/gwc/create-lambda.mp4)

1. Go to [AWS Console](https://console.aws.amazon.com), and log in to your account.
2. Navigate to Lambda.
3. Click "Create a Lambda function."
4. Search for the "alexa-skills-kit-color-expert-python" starter blueprint, and click on it.
5. Click "next" on the Configure triggers tab.
6. Make a name for your function!
7. Delete the code in the "Lambda function code" input.
8. Copy the code provided for the AWS Lambda code in lambda_function.py, and paste it into the "Lambda function code" input.
9. At the bottom of the page, under Lambda function handler & role, select "Create a custom role."
10. When the IAM role management console opens, choose Allow to got back to your Lambda console.
9. Click "Next."
10. Click "Create function."
11. Copy the Amazon Resource Name (ARN) displayed in the upper right corner of the console `arn:aws:lambda...` (You will use this when setting up your skill!)

## Setup your Alexa Skill
[![Watch the video](https://a.cnnlabs.com/show-assets/dev/shows/test/gwc/skill.png)](https://a.cnnlabs.com/show-assets/dev/shows/test/gwc/skill-setup.mp4)

1. Log in to the [Amazon Developer Console](https://developer.amazon.com/alexa-skills-kit/alexa-skills-developer-training)
2. Click the Alexa tab.
3. Click Alexa Skills Kit "Get Started."
4. Click "Add a New Skill."
5. Add a name for your skill.
6. Add an Invocation name for your skill.
7. Click "save."
8. On the Interaction Model Page, copy and paste intentSchema.txt into the Intent Schema input.
9. In Custom Slot Types, copy and paste the customSlots.txt file into the input.
10. In the Sample Utterances, copy and paste the sampleUtterances.txt file into the input.
11. Click "Next."
12. On the Configuration tab, add your AWS Lambda ARN into the slot for "North America" Lambda under Endpoint.
13. Click "Next."
14. On the testing tab, you can now test your skill!
15. You also test using echosim.io.

## Getting your skill on a device
To get your skill on a device, you should finish up the Publishing Info and Privacy Compliance fields that are required.

Once you do, you will see the "Skills Beta Testing" say active. Click that button, and add the email address you use on your Alexa device like an Echo or Dot. Go to your Alexa app on your phone, and enable your skill to start playing!
