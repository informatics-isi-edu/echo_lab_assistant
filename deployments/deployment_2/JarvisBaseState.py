import abc
import logging
from ErmrestHandler import ErmrestHandler

class JarvisBaseState(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self):
		self._request = "request variable goes here" 
		self._session = "session variable goes here"
		self._speech_output = "Jarvis speech output"
		self._reprompt_text = "Sorry. I didn't get that"
		self._ermrest = "Ermrest Handler goes here" 
		self._EMPTY = [[],{},(),None]
	
	@abc.abstractmethod
	def handle_input(self):
		"""The handle_input method will be the method called by the StateHandler. 
			handle_input must return the name of the state to switch too.
			The only state which returns a value other than that is the ReturnState 
			which returns the text for Alexa to say to the user.""" 
		return
##=============================Helper Methods=============================================

	def _get_intent(self, intent_request):
		intent = None 
		if 'intent' in intent_request:
			intent =  intent_request['intent']
		
		return intent 

	def _get_intent_name(self, intent_request):
		intent_name = None
		intent = self._get_intent(intent_request)

		if intent not in self._EMPTY and 'name' in intent:
			intent_name = intent['name']

		return intent_name

	def _slot_exists(self, slot_name, intent_request):
		exists = False
		intent = self._get_intent(intent_request)

		if 'slots' in intent: 
			exists = slot_name in intent['slots']
		
		return exists

	def _get_slot_value(self, slot_name, intent_request):
		value = None

		if self._slot_exists(slot_name, intent_request):

			intent = self._get_intent(intent_request)
			if (intent not in self._EMPTY):
				value = intent['slots'][slot_name]['value']

        	return value
	
	def _get_current_user(self):
		current_user = None

		current_user = self._ermrest.get_data(7,"session_info")
		if (current_user not in self._EMPTY):
			current_user = current_user[0]['user']

		return current_user
	
	def _set_session_data(self,column,new_data):
		success = False
		current_data = self._ermrest.get_data(7,"session_info")[0]
		current_data[column] = new_data

		try:
			self._ermrest.delete_data(7,"session_info")
			self._ermrest.put_data(7,"session_info",current_data)
			success = True
		except Exception as exc:
			print("[!] ERROR: "+str(exc))
		
		return success

	def _set_completed_step(self,new_step):
		success = False
		data = {"completed_step":new_step}
		
		try:
			self._ermrest.delete_data(7,"step_completed")
		except:
			pass

		try:
			self._ermrest.put_data(7,"step_completed",data)
			success = True
		except Exception as exc:
			print('[!] ERROR: '+str(exc))
		
		return success

	def _clear(self,table_name):
		#clears a table
		success = False
		clean_data = self._ermrest.get_data(7,table_name)[0]

		for key in clean_data:
			clean_data[key] = None

		try:
			self._ermrest.delete_data(7,table_name)
			self._ermrest.put_data(7,table_name,clean_data)
			success = True
		except Exception as exc:
			print("[!] ERROR: "+str(exc))

		return success

	def _get_last_step(self,experiment_id):
		query = "/user="+str(self._get_current_user())+"/experiment_id="+str(experiment_id)
		experiment = self._ermrest.get_data(7,"experiment_data",query)[0]

		steps = experiment['states_completed'].split(",")
		last_step = steps[len(steps)-1]

		return last_step


	def _get_experiment(self,experiment_id):
		experiment = dict() 
		experiment_id = str(experiment_id)
		user = self._get_current_user()
		query = "/user="+user+"/experiment_id="+experiment_id

		try:
			experiment = self._ermrest.get_data(7,"experiment_data",query)
		except Exception as exc:
			print("[!] ERROR: "+str(exc))
		
		return experiment
	
