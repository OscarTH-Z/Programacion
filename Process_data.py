
import requests
import json

class Process_Data:

	def get_data_from_link(self, url):
		try:
			r = requests.get(url)
			data = r.json()
			final_data = data['items']
			return final_data
		except Exception as e:
			print(e)
			return None 

	def get_answers(self, data):
		answer_is_true = 0
		answer_is_false = 0
		response = {}
		for element in data:
			is_answered = element['is_answered'] 
			if is_answered is True:
				answer_is_true += 1
			if is_answered is False:
				answer_is_false += 1
			else:
				pass
		response['True'] = answer_is_true
		response['False'] = answer_is_false
		return response

	def get_answer_with_least_number_of_views(self, data):
		cont = 0
		response = None
		for element in data:
	                if cont is 0:
	                        response = element
	                else:
	                        if (element['view_count']  < response['view_count']):
	                                response = element
	                cont +=1
		return response


	def get_owner_with_the_highest_reputation(self, data):
		cont = 0
		response = None
		for element in data:
			if cont is 0:
				response = element
			else:
				if (element['owner']['reputation'] > response['owner']['reputation']):
					response = element
			cont+=1
		return response

	def get_the_oldest_and_most_recent_response(self, data):
		cont = 0
		oldest_response = None
		recent_response = None 
		response ={}
		for element in data:
			if cont is 0:
				oldest_response = element 
				recent_response = element
			else:
				if (element['creation_date'] > oldest_response ['creation_date']):
					oldest_response = element
					#print("Mas grande: ", element['creation_date'])
				if (element['creation_date'] < recent_response ['creation_date']):
					recent_response = element
					#print("Mas Chica: ", element['creation_date'])
			cont+=1
		response['oldest_response'] = oldest_response
		response['recent_response'] = recent_response 
		return response 

