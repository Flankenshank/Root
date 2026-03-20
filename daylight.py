def battle(order_suite):
    print(f'Initiate a battle in each {order_suite} clearing.\n'
          f'The defender is the player with the most pieces in the clearing of battle.\n'
          f'In the case of the tie, choose the player with the most victory points.')


def recruit(order_suite):
    while True:
        answer = input(f'Place 4 Warriors among {order_suite} clearings you rule.\n'
                       f'How many {order_suite} clearings do you rule? ')
        if answer == '1':
            print('Place 4 Warriors here')
            break
        elif answer == '2':
            print('Place 2 Warriors in each clearing')
            break
        elif answer == '3':
            print('Place 1 Warriors in each clearing, and 1 more in the highest priority clearing.')
            break
        elif answer == '0':
            print('Recruit not possible')
            break
        else:
            print('Yeah, right!')


def build(order_suite):
    match order_suite:
        case 'fox':
            order_building = 'sawmill'
        case 'mouse':
            order_building = 'recruiter'
        case 'rabbit':
            order_building = 'workshop'
        case _:
            order_building = 'unknown'
    print(f'Place a {order_building} in the clearing you rule with the most Marquise warriors.')

def move(order_suite):
    print(f'Move all but 3 of your warriors from each {order_suite} clearing to\n'
          f'the adjacent clearing with the most enemy pieces')
