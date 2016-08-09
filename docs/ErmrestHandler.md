# ErmrestHandler Class
A class that allows a user to easily create new tables,schemas,catalogs in an ermrest database.
Allows user to put, delete and retireve data in a specified table. 

## Constructor(username,password)
 - Takes in the username for login
 - Takes in the password for login

## get_cookie(username,password) method
starts a session and returns a cookie for future interaction. Called in constructor

## create_catalog() method
creates a catalog and returns the id assigned to that catalog

## create_schema(catalog_id,name) method
creates a new schema in the catalog you assign it. Names it the name you provide

## create_table(catalog_id,schema_name,table) method
Creates a table in the specified catalog and schema using the table argument. 
Table should be of python dict type. see examples in the tables folder.

## delete_catalog(catalog_id) method
Deletes the catalog you specify

## delete_schema(catalog_id,schema_name) method
deletes the schema you specify

## delete_table(catalog_id,schema_name,table_name) method
deletes the table you specify

## get_data(catalog_id,table_name,extra_info="") method
Gets data from the table specified. returns all info in the 
specified table if no extra_info is passed in. extra info must be of type string.

examples:
 - ErmrestHandler.get_data(7,"experiment_data","/user=Joe/experiment_id=5")
 - ErmrestHandler.get_data(7,"session_info","/current_user=Bob/jarvis_response=Hello")

## delete_data(catalog_id,table_name,extra_info="") method
Deletes the specified data. Will clear the whole tables if no extra info 
is passed in. Extra info rules from get_data apply.

## put_data(catalog_id,table_name,data) method
Inputs data into the specified table. Data must be of type dict()

examples:
 - ErmrestHandler.put_data(7,"session_info",{"user":"Joe","jarvis_response":"Hi Joe","current_experiment_id":4})
 - ErmrestHandler.put_data(7,"step_completed",{"completed_step":"exp-start"})
 
