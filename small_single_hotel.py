hotel = {
    '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
        }
    },
    '105': {},
}

def is_vacant(hotel, room):
    if 'guest' in hotel[room]:
        return 'Room is occupied'
    else:
        return 'Room is empty'

print(is_vacant(hotel, '101'))






# the goal of the small excercise is to get practice with the syntax for querying and manipulating the data in a single, nested dictionary.

hotel = {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}

def check_in(desired_room, guest_info_dictionary, dictionary):
    for room in dictionary:
        if room == desired_room:
            dictionary[room]['guest'] = guest_info_dictionary
    
    return dictionary

example_dictionary_guest_info = {
            'name': 'John Doe',
            'phone': 8675309
        }

hotel = check_in("102", example_dictionary_guest_info, hotel)

print(hotel)

