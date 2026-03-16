def birdsong_draw():
    print("Draw and reveal an order card from the draw pile")


def craft_item():

    while True:
        answer = input("Is it a craftable, available item? Y/N ").upper()
        if answer == "Y":
            print("Craft it for 1 victory point. MEOW!")
            break
        elif answer == "N":
            print("Move on to Daylight")
            break
        else:
            print("Please enter Y for yes or N for no")

def order_card_suite ():
    order_suite = input("What suit is the order card? ")
    return order_suite
