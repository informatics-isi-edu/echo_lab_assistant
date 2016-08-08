# Jarvis lab assistant: Alexa/Amazon Echo Skill

_The lab partner that does things right!_

## What is Jarvis?
Jarvis is an Alexa/Amazon Echo Skill that can walk you through the Gel Electrophoresis experiment and store data
for your retrieval in the future.

## Installation
1. Sign into the AWS management console(how to create an account: http://docs.aws.amazon.com/lambda/latest/dg/setting-up.html)
1. Click on 'Services' in the top left corner of the screen and choose Lambda
1. Click 'Create a Lambda Function'
1. Press skip when presented with example functions
1. Set the trigger to 'Alexa Skills Kit' 
1. Name the Function and add a description where the space is provided and Set 'Runtime*' to 'python 2.7'
1. Change 'Code entry type' to 'Upload a .zip'
1. Clone this repository to your machine
1. run the 'create_deployment.py' script. This should create a folder and .zip file in your deployments directory
1. On the create Lambda function page under 'Code entry type' click 'upload' and upload the zip that 'create_deployment' created
1. In the 'Handler*' box change 'lambda_function.lambda_handler' to 'main.lambda_handler'
1. Set 'existing role' to 'lambda_basic_execution'
1. Press 'Next' and then 'Create Function'
1. On the 'Triggers' tab click 'Alexa Developer Portal'. (Copy the ARN in the top right corner)
1. Press 'Alexa Skills Kit' then click 'Add a new Skill'
1. Name the skill, then set the 'invocation name' to 'Jarvis'. Click Next
1. In the 'Interaction_Model' folder open 'sample_utterances.txt','genie_intent_schema' and 'custom slot types'.
1. Set the corresponding sections to the text in the files. Click Next
1. Chose 'Lambda ARN' for 'endpoint*' and paste your functions ARN in the space provided. Click Next

Now the skill should be set up for use on your account!

## Using Jarvis
In order to use Jarvis the user must first log in. Login can be done in two ways.
 - Through a simple voice command: 'Alexa ask Jarvis, Login user {UserName}'
 - Through the Bluetooth Login feature: https://github.com/arstevens/BluetoothLogin

Once the session has started, the user can do a few things.
 - Open an old experiment for data retrieval or continuation(Experiment ID is required)
 - Start a new experiment.
 - Ask who the current user is
 - Logout

Voice Commands
 - All voice commands Jarvis understands can be found in the 'sample_utterances.txt' file. (in 'Interaction_Model' folder)
 - Any word enclosed in {} are key words that the user must provides.
 - The text presented before the phrase is not be said. It is their only for the Lambda functions use. (signifies intent)
   - Example: 'ExperimentIntent this is an experiment intent'. The phrase is 'This is an experiment intent' not 'ExperimentIntent'

## Developer Reference:
 - https://github.com/informatics-isi-edu/echo_lab_assistant/blob/master/docs/Reference.md
