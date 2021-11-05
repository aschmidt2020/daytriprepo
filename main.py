#day trip generator - due Monday 11/8 - using while loop (not a function)
import random
import itertools

#lists to store options
destinations = ['Hawaii', 'Maui', 'Colorado']
restaurants = ['Fast Food', 'Mom and Pop Restaurant', 'Fancy Restaurant']
mode_of_transport = ['Bus', 'Car', 'Train']
entertainments = ['Movie', 'Play', 'Musical']

destinations_cycle = itertools.cycle(destinations)
restaurants_cycle = itertools.cycle(restaurants)
mode_of_transport_cycle = itertools.cycle(mode_of_transport)
entertainments_cycle = itertools.cycle (entertainments)

#random choice generator
def random_choice_single(choice_list):
    random_choice = random.choice(choice_list)
    return random_choice

#current selections/trip display
destination = random_choice_single(destinations)
restaurant = random_choice_single(restaurants)
transport = random_choice_single(mode_of_transport)
entertainment  = random_choice_single(entertainments)

confirmed = False

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
        destination = next(destinations_cycle)
        trip_display(destination, restaurant, transport, entertainment)
    elif change == 2:
        restaurant = next(restaurants_cycle)
        trip_display(destination, restaurant, transport, entertainment)
    elif change == 3:
        transport = next(mode_of_transport_cycle)
        trip_display(destination, restaurant, transport, entertainment)
    elif change == 4:
        entertainment = next(entertainments_cycle)
        trip_display(destination, restaurant, transport, entertainment)

print('Going on trip...\n')

completed_trip = trip_display(destination, restaurant, transport, entertainment)    