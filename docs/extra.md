# Extra

## requirements.txt
This file is the standard Python requirements file.  This file is used by the
create_deployment.py script to install the necessary 3rd party libraries that
your Alexa skill might need.  Any library specified in the requirements.txt
file will be installed into your deployment directory.

## create_deployment.py
Creates the properly formatted zip file to give to the lambda function. If any extra files are needed
they must be added to 'deployment_files' list in the create_deployment script.

## Tables Folder
The tables folder contains all the .json files for creating the tables used by Jarvis. 
