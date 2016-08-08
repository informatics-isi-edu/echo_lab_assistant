# GelElectrophoresis Class
Contains all the methods for the experiment intents.

## add_item(data,item) method
Adds an item to a string list that is held in the 'experiment_data' table.

examples:
	GelElectrophoresis.add_item('one,two','three')
	returns 'one,two,three'

## item_exists(data,item) method
Checks if the item provided is in the data. data is a string list like in add_item

examples:
	GelElectrophoresis('one,two,three','three')
	returns True

## Experiment_intents (group of methods)
Returns the proper phrase for Alexa to say and input data into the users experiment in 'experiment_data'. 
Updates 'states_completed' column 
