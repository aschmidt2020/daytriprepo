#day trip generator - due Monday 11/8 - using while loop (not a function)
import random

#lists to store options
destinations = ['Hawaii', 'Maui', 'Colorado']
restaurants = ['Fast Food', 'Mom and Pop Restaurant', 'Fancy Restaurant']
mode_of_transport = ['Bus', 'Car', 'Train']
entertainments = ['Movie', 'Play', 'Musical']

#random choice generator
def random_choice_single(choice_list):
    random_choice = random.choice(choice_list)
    return random_choice

#current selections/trip display
destination = random_choice_single(destinations)
restaurant = random_choice_single(restaurants)
transport = random_choice_single(mode_of_transport)
entertainment  = random_choice_single(entertainments)

def trip_display(destination, restaurant, transport, entertainment):
    print(f'\nThe following trip has been selected for you:\nDestination: {destination}, Restaurant: {restaurant}, Transport: {transport}, Entertainment: {entertainment} \n')

current_trip = trip_display(destination,restaurant, transport, entertainment)

#while loop through selections until confirmed by user
confirmed = False

while confirmed == False:
    change = int(input('What would you like to change about your trip? 0-Nothing, confirm my trip!, 1-Destination, 2-Restaurant, 3-Transport, 4-Entertainment: '))
    if change == 0:
        print (f'\nThe following trip has been confirmed for you:\nDestination: {destination}, Restaurant: {restaurant}, Transport: {transport}, Entertainment: {entertainment} \n')
        confirmed = True
    elif change == 1:
        destination = random_choice_single(destinations)
        trip_display(destination, restaurant, transport, entertainment)
    elif change == 2:
        restaurant = random_choice_single(restaurants)
        trip_display(destination, restaurant, transport, entertainment)
    elif change == 3:
        transport = random_choice_single(mode_of_transport)
        trip_display(destination, restaurant, transport, entertainment)
    elif change == 4:
        entertainment = random_choice_single(entertainments)
        trip_display(destination, restaurant, transport, entertainment)

#display for completed trip
def completed_trip_display(destination, restaurant, transport, entertainment):
    print(f'The following trip has been completed:\nDestination: {destination}, Restaurant: {restaurant}, Transport: {transport}, Entertainment: {entertainment} \n')

print('Going on trip...\n')

completed_trip = completed_trip_display(destination, restaurant, transport, entertainment)    