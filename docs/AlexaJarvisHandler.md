# AlexaJarvisHandler class
Concrete implementaion of AlexaBase Handler

## on_processing_error(event,context,exc) method
Invoked if Jarvis experiences problems. Can be cause by:
 - Undefined phrase 
 - Cannot understand question
 - If on_intent fails and returns an error

## on_launch(request,session) method
Invoked if Jarvis called with no specific intent. Sets the speech output
accordingly depending on if a user is logged in or not.

## on_session_started(request,session) method
Invoked if session is started with no specific intent. Calls on on_launch method

## on_intent(request,session method
Invoked if a specific intent was passed to Jarvis.
Creates the state machine(JarvisStateHandler) and runs it.
Returns proper response based on what state handler returned

## on_session_ended(request,session) method
Invoked if session is ending. Sets the proper speech output
and returns response.
