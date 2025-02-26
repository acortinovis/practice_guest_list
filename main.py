def print_invit(family: list):
    for person in family:
        print(f'Dear {person}, you are invited to my dinner.')

def replace(guest: str, index: int, family: list):
    family[index] = guest  
    return family

def sorting(family: list):
    family.sort()
    return family

while True:
    family = ['mom', 'dad', 'artu', 'cami', 'gabri', 'anya']
    new_family = sorting(family)
    print_invit(new_family) 
    answer = input('Would you like to change your list? (y/n) ')
    
    if answer == 'y':
        number = int(input("Which guest number do you want to change? (0-5) "))
        new_guest = input('Who is the new guest you want to invite? ')
        new_family = replace(new_guest, number, new_family)
        new_family = sorting(new_family)
        print_invit(new_family) 
        length = len(new_family)
        print(f'You have {length} people invited.')
        break
    else:
        print('Goodbye.')
        break
