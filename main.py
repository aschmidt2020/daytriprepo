#day trip generator - due Monday 11/8 - using while loop (not a function)
import random

#lists for storage
destinations = ['Hawaii', 'Maui', 'Colorado']
restaurants = ['Fast Food', 'Mom and Pop Restaurant', 'Fancy Restaurant']
mode_of_transport = ['Bus', 'Car', 'Train']
entertainments = ['Movie', 'Play', 'Musical']

confirmed = False #will use for while loop until trip is 'confirmed'

#random choice/new choice generator
def random_choice_single(choice_list):
    random_choice = random.choice(choice_list)
    return random_choice

def get_new_choice(previous_value, choices):
    needs_new = True
    while needs_new == True:
            destination = random_choice_single(choices)
            if(previous_value != destination):
                needs_new = False
    return destination

#current selections/trip display
destination = random_choice_single(destinations)
restaurant = random_choice_single(restaurants)
transport = random_choice_single(mode_of_transport)
entertainment  = random_choice_single(entertainments)

def trip_display(destination, restaurant, transport, entertainment):
    if confirmed == False:
        print(f'\nThe following trip has been selected for you:\nDestination: {destination}, Restaurant: {restaurant}, Transport: {transport}, Entertainment: {entertainment} \n')
    else: 
        print (f'The following trip has been completed:\nDestination: {destination}, Restaurant: {restaurant}, Transport: {transport}, Entertainment: {entertainment} \n')

current_trip = trip_display(destination,restaurant, transport, entertainment)

#while loop through selections until confirmed by user

while confirmed == False:
    change = int(input('What would you like to change about your trip? 0-Nothing, confirm my trip!, 1-Destination, 2-Restaurant, 3-Transport, 4-Entertainment: '))
    if change == 0:
        print (f'\nThe following trip has been confirmed for you:\nDestination: {destination}, Restaurant: {restaurant}, Transport: {transport}, Entertainment: {entertainment} \n')
        confirmed = True
    elif change == 1:
        destination = get_new_choice(destination, destinations)

        trip_display(destination, restaurant, transport, entertainment)
    elif change == 2:
        restaurant = get_new_choice(restaurant, restaurants)
        trip_display(destination, restaurant, transport, entertainment)
    elif change == 3:
        transport = get_new_choice(transport, mode_of_transport)
        trip_display(destination, restaurant, transport, entertainment)
    elif change == 4:
        entertainment = get_new_choice(entertainment, entertainments)
        trip_display(destination, restaurant, transport, entertainment)

print('Going on trip...\n')

completed_trip = trip_display(destination, restaurant, transport, entertainment)    



