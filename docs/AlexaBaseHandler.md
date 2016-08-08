# AlexaBaseHandler class
The AlexaBaseHandler class is an abstract class that provides the necessary
framework to build the necessary response hooks for an Alexa application.

All of the abstract methods of this class must be implemented by the
concrete implementation class.  See the base class for details on the
abstract methods.

## process_request method
This method will take the 2 parameters that are sent to the lambda function
and determine which of the Alexa handlers to invoke.

## _build_speechlet_response method
This method ( from the Alexa color example ) will put together the speechlet portion
into a properly formatted json message.  This is typically called by the
concrete implementations of the AlexaBaseHandler.

## _build_response
This method (from the Alexa color example ) will construct a properly formatted
response message so the Amazon Echo knows what to respond with.
