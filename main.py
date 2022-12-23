import tello
import time

tello = tello.Tello('',8889)

while True:
    tello.send_command('command')
    time.sleep(5)
