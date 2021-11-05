#day trip generator - due Monday 11/8 - using loop function
import random
import itertools

#list to store options
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

random_choice_destination = random_choice_single(destinations)
random_choice_restaurants = random_choice_single(restaurants)
random_choice_transport = random_choice_single(mode_of_transport)
random_choice_entertainment  = random_choice_single(entertainments)

#def loop to validate each choice
def random_choice_correct(random_choice, choice_list):
    print(f'Current choice is {random_choice}.')
    final_choice = random_choice
    correct = input('Is this choice okay? Yes/No: ')
    while correct != 'Yes':
        new_choice = next(choice_list)
        final_choice = new_choice
        print(f'This is your new choice: {new_choice}')
        correct = input('Is new choice okay? Yes/No: ')
    if correct == 'Yes':
        print (f'{final_choice} has been confirmed.\n')
    return final_choice

final_destination = random_choice_correct(random_choice_destination, destinations_cycle)
final_restaurant = random_choice_correct(random_choice_restaurants, restaurants_cycle)
final_transport = random_choice_correct(random_choice_transport, mode_of_transport_cycle)
final_entertainment = random_choice_correct(random_choice_entertainment, entertainments_cycle)

#print completed trip
def trip_complete (destination, restaurant, transport, entertainment):
    print (f'The following trip has been completed for you:\nDestination: {destination}, Restaurant: {restaurant}, Transport: {transport}, Entertainment: {entertainment} \n')

print('Going on trip...\n')

final_selections = trip_complete(final_destination, final_restaurant, final_transport, final_entertainment)





