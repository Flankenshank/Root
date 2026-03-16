def battle(order_suite):
    print(f'Initiate a battle in each {order_suite} clearing.\n'
          f'The defender is the player with the most pieces in the clearing of battle.\n'
          f'In the case of the tie, choose the player with the most victory points.')

def recruit(order_suite):
    while True:
        answer = input(f'Place four Warriors among {order_suite} clearings you rule. How many {order_suite} clearings do you rule? ')
        if answer == '1':
            print('Place four Warriors here')
            break
        elif answer == '2':
            print('Place two Warriors in each clearing')
            break
        elif answer == '3':
            print('Place three Warriors in each clearing, and one more in the highest priority clearing.')
            break
        else:
            print('Yeah, right!')