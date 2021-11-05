#day trip generator - due Monday 11/8

import random

#lists for storage
destinations = ['Hawaii', 'Maui', 'Colorado']
restaurants = ['Fast Food Restaurant', 'Mom and Pop Restaurant', 'Fancy Restaurant']
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
            new_choice = random_choice_single(choices)
            if(previous_value != new_choice):
                needs_new = False
    return new_choice

#current selections/trip display
def trip_display(current_selections):
    if confirmed == False:
        print(f'\nThe following trip has been selected for you:\nDestination: {my_current_trip[0]}, Restaurant: {my_current_trip[1]}, Transport: {my_current_trip[2]}, Entertainment: {my_current_trip[3]}')
    else: 
        print('Going on trip...\n')
        print (f'The following trip has been completed: You traveled to {my_current_trip[0]} in a {my_current_trip[2]}. You ate at a {my_current_trip[1]} and saw a {my_current_trip[3]}. \n')

def get_current_selections(destination_list, restaurant_list, transport_list, entertainment_list):
    current_selections = []

    destination = random_choice_single(destination_list)
    restaurant = random_choice_single(restaurant_list)
    transport = random_choice_single(transport_list)
    entertainment = random_choice_single(entertainment_list)

    current_selections.append(destination)
    current_selections.append(restaurant)
    current_selections.append(transport)
    current_selections.append(entertainment)

    return current_selections

my_current_trip = get_current_selections(destinations, restaurants, mode_of_transport, entertainments)
trip_display(my_current_trip)

#while loop through selections until confirmed by user
while confirmed == False:
    change = int(input('\nWhat would you like to change about your trip?\n0-Nothing, confirm my trip!, 1-Destination, 2-Restaurant, 3-Transport, 4-Entertainment: '))
    if change == 0:
        print (f'\nThe following trip has been confirmed for you:\nDestination: {my_current_trip[0]}, Restaurant: {my_current_trip[1]}, Transport: {my_current_trip[2]}, Entertainment: {my_current_trip[3]} \n')
        confirmed = True
    elif change == 1:
        my_current_trip[0] = get_new_choice(my_current_trip[0], destinations)
        trip_display(my_current_trip)
    elif change == 2:
        my_current_trip[1] = get_new_choice(my_current_trip[1], restaurants)
        trip_display(my_current_trip)
    elif change == 3:
        my_current_trip[2] = get_new_choice(my_current_trip[2], mode_of_transport)
        trip_display(my_current_trip)
    elif change == 4:
        my_current_trip[3] = get_new_choice(my_current_trip[3], entertainments)
        trip_display(my_current_trip)

#completed trip display using above function
completed_trip = trip_display(my_current_trip) 



