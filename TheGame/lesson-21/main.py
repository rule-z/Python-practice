# 🌳 🟦 🚁 🟩 🔥 🏥 ♥️ 💧 🏪 ☁️ ⚡️ 🏆
from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter as Helico

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

my_map = Map(MAP_W, MAP_H)

helico = Helico(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def process_key(key):
    global helico
    c = key.char
    if c in MOVES.keys():
        print("OK")
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    else:
        print("not ok")

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

tick = 1

while True:
    os.system("cls")
    print("Tick", tick)
    helico.print_stats()
    my_map.process_helicopter(helico)
    my_map.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        my_map.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        my_map.update_fires()