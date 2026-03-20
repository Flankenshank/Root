import birdsong
import daylight
import evening

birdsong.birdsong_draw()
birdsong.craft_item()
order_suite = birdsong.order_card_suite()
daylight.battle(order_suite)
input('Press Enter to continue...')
daylight.recruit(order_suite)
input('Press Enter to continue...')
daylight.build(order_suite)
input('Press Enter to continue...')
daylight.move(order_suite)
input('Press Enter to continue...')