# main.py
This file contains the main entry point of the lambda function that is called
for the Alexa skill.

## lamda_handler(event,context) function
This function ( which can be called anything, you just need to configure it in
the lambda handler ), is the function that is called with the 2 parameters.

This function will typically instantiate an concrete implementation of the
AlexaBaseHandler and delegate to the process_request method.
