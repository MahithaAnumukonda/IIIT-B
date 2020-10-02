from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

# from rasa_core.actions.action import Action
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset

from rasa_sdk.events import Restarted
# from rasa_core.events import SlotSet
import json
#from send_mail import email
from zomato_slots import results
from city_check import check_location
from contextlib import contextmanager

import smtplib
from email.mime.text import MIMEText as text


# ------------------- ACTION SEARCH RESTAURANTS -------------------

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')

		global restaurants

		restaurants = results(loc, cuisine, price)
		top_5 = restaurants.head(5)

		# top 5 results to display
		if not top_5.empty:
			response = 'Showing you top results:' + "\n"
			msg_template = 'Restaurant: {} in Address: {} has been rated: {}\n with cost for two of: {}\n'
			for _, row in top_5.iterrows():
				response += msg_template.format(
					row["restaurant_name"],
					row['restaurant_address'],
					row['restaurant_rating'],
					row['budget_for2people'])
		else:
			response = 'No restaurants found'

		dispatcher.utter_message(str(response))

		if not (price or cuisine):
			print('Location only reset')
			return [SlotSet("location", None)]

		return [AllSlotsReset()]



# ------------------- ACTION SEND EMAIL -------------------

class ActionSendEmail(Action):

	def __init__(self):
		self.sender_email_id = 'mailforchatbot29@gmail.com'
		self.sender_email_id_password = 'MAHEe@29'

	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		global restaurants
		receiver_email_id = tracker.get_slot('email')
		print(f'sending email to: {receiver_email_id}')
		top_10 = restaurants.head(10)
		message = 'Showing you top Restaurant search results:\n\n'
		linebreak = '{}\n'.format('*'*20)
		msg_template = 'Restaurant: {} in Address: {} has been rated: {}\n with cost for two of: {}\n'
		for _, row in top_10.iterrows():
			message += msg_template.format(
				row["restaurant_name"],
				row['restaurant_address'],
				row['restaurant_rating'],
				row['budget_for2people'])
		message += linebreak
		self.send_email(receiver_email_id, message)
		response = "We have emailed you list of top rated restaurants in your area!!"
		dispatcher.utter_message("-----"+response)
		return [AllSlotsReset()]

	def send_email(self, receiver_email_id, message):
	    with self.open_mail_connection() as conn:
	        email_message = self.format_message(message, receiver_email_id)
	        conn.sendmail(self.sender_email_id, receiver_email_id, email_message.as_string())

	def format_message(self, message, receiver_email_id):
	    msg = text(message)
	    msg['Subject'] = 'Restaurant details from Foodie'
	    msg['From'] = self.sender_email_id
	    msg['To'] = receiver_email_id
	    return msg

	@contextmanager
	def open_mail_connection(self):
	    conn = smtplib.SMTP('smtp.gmail.com', 587)
	    conn.starttls()
	    conn.login(self.sender_email_id, self.sender_email_id_password)
	    yield conn
	    conn.quit()

# ------------------- ACTION VALIDATE LOCATION -------------------

class Check_location(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		check = check_location(loc)
		return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]

# ------------------- ACTION RESTART CONVERSTATION -------------------
class ActionRestarted(Action):
	def name(self):
		return 'action_restart'
	def run(self, dispatcher, tracker, domain):
		return[Restarted()]
