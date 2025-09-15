# 🌳 🟦 🚁 🟩 🔥 🏥 ♥️ 💧 my_map = Map(20, 10)

from map import Map
import time
import os

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

my_map = Map(MAP_W, MAP_H)
my_map.generate_forest(3, 10)
my_map.generate_river(10)
my_map.generate_river(10)
my_map.print_map()

tick = 1

while True:
    os.system("cls")
    print("Tick", tick)
    my_map.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        my_map.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        my_map.update_fires()