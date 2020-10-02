## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - utter_ask_mail
* email_restaurant_deatils{"email": "ahluwaliamridul@gmail.com"}
    - slot{"email": "ahluwaliamridul@gmail.com"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_check_location
    - slot{"location": "Pune"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "mahitha.anumukonda@ymail.com"}
    - slot{"email": "mahitha.anumukonda@ymail.com"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - action_check_location
    - slot{"location": "Prayagraj"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "mahitha.anumukonda@ymail.com"}
    - slot{"email": "mahitha.anumukonda@ymail.com"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "chandigarh"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "ahluwaliamridul@gmail.com"}
    - slot{"email": "ahluwaliamridul@gmail.com"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_ask_location
    - utter_location_notfound
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "jalebi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "jalebi"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_check_location
    - slot{"location": "Jaipur"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - action_check_location
    - slot{"location": "Dehradun"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Argra"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Argra"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location": "Amritsar"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "test@123.com"}
    - slot{"email": "test@123.com"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Argra"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Argra"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location": "Amritsar"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"location": "Kasol"}
    - slot{"location": "Kasol"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Bombay"}
    - slot{"location": "Bombay"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_check_location
    - slot{"location": "hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"location": "Tokyo"}
    - slot{"location": "Tokyo"}
    - action_check_location
    - utter_location_notfound
* restaurant_search{"location": "Calcutta"}
    - slot{"location": "Calcutta"}
    - action_check_location
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "humpty@haha.co.in"}
    - slot{"email": "humpty@haha.co.in"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_check_location
    - slot{"location": "Gurgaon"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - utter_ask_location
* restaurant_search{"location": "Paris"}
    - slot{"location": "Paris"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"location": "Bengaluru"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "mahitha.anumukonda@ymail.com"}
    - slot{"email": "mahitha.anumukonda@ymail.com"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Delhi", "price": "between 300 to 700"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Delhi"}
    - slot{"price": "between 300 to 700"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_found": "found"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"location": "patiala", "price": "lesser than 300"}
    - slot{"location": "patiala"}
    - slot{"price": "lesser than 300"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - action_check_location
    - slot{"location": "Varanasi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_restaurant
    - utter_do_you_want_email
* deny
    - utter_final_bye
    - action_restart

## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Delhi", "price": "between 300 to 700"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Delhi"}
    - slot{"price": "between 300 to 700"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_found": "found"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "mahitha.anumukonda@ymail.com"}
    - slot{"email": "mahitha.anumukonda@ymail.com"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - utter_ask_location
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - action_check_location
    - slot{"location": "Noida"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "hawa.23@jojo.so"}
    - slot{"email": "hawa.23@jojo.so"}
    - action_send_email
    - utter_final_bye
    - action_restart

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"location": "Kasol"}
    - slot{"location": "Kasol"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_check_location
    - slot{"location": "vijayawada"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"price": "lesser than 300", "cuisine": "Mexican", "location": "Chennai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Chennai"}
    - slot{"price": "lesser than 300"}
    - action_check_location
    - slot{"location": "chennai"}
    - slot{"location_found": "found"}
    - action_restaurant
    - reset_slots
    - utter_do_you_want_email
* email_restaurant_deatils{"email": "abcd@yahoo.com"}
    - slot{"email": "abcd@yahoo.com"}
    - action_send_email
    - reset_slots
    - utter_final_bye
    - action_restart

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_location
    - slot{"location": "mysore"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - utter_do_you_want_email
* affirm
    - utter_ask_mail
* email_restaurant_deatils{"email": "mahitha.anumukonda@ymail.com"}
    - slot{"email": "mahitha.anumukonda@ymail.com"}
    - action_send_email
    - utter_final_bye
    - action_restart
