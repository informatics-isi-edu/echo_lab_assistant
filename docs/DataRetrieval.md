# DataRetrieval Class
Invoked when Retrieval/Get intent is returned. Contains methods for all Get intents

## _get_experiment_data(column) method
Gets data from the colum provided out of the 'experiment_data' table based on the experiment id and
username provided in the constructor.

## _epoch_to_time(timestamp) method
receives a timestamp created from 'time.asctime(time.localtime(time.time()))' and creates a 
speakable phrase for alexa to say. Uses the num2words library to turn numbers to words

## get_experiment_id_intent() method
returns the experiment id in alexa readable form

## get_start_date_intent() method
passes the timestamp from the experiment start time and returns it in 
alexa readable form by passing it to the _epoch_to_time method

## get_end_date_intent() method
passes the timestamp from the experiment end time and returns it in 
alexa readable form by passing it to the _epoch_to_time method

## get_sample_count_intent() method
Gets the amount of samples experimented with and returns it in an alexa
readable way

## get_well_sample_assignment_intent(well_number) method
Finds the sample that was assigned to the well_number variable during the experiment.
returns an alexa readable phrase telling what sample was assigned to that well

## get_sample_well_assignment_intent(sample) method
Finds the well that was assigned to a sample during the experiment. returns an alexa
readable phrase telling what well was assigned to that sample

