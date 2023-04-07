import pyautogui
import pydirectinput
import time
import signal

END = False

def end(sig, frame):
    global END
    END = True
    print('ending...')

def kittyClaw():
    global END
    piece = input("Who do you want? PBR, Master, Humpy, Muffy, Poopy, Saki, Smokie or Grindy\n"
                  "SWK requires dislodging and experimentation or you can try your luck\n").lower()
    if piece == "pbr": w,d = 3.8,1.8
    elif piece == "master": w,d = 2.6,3.2
    elif piece == "grindy": w,d = 3.8,.2
    elif piece == "smokie": w,d = 2,.2
    elif piece == "poopy": w,d = 2.7,1.4
    elif piece == "saki": w,d = 1.5,3.8
    elif piece == "muffy": w,d = .1,3.5
    elif piece == "humpy": w,d = .1, 1.7
    else:
        print("Not an option")
        return kittyClaw()
    tries = 0
    time.sleep(5)
    while not END:
        pydirectinput.press('e')
        time.sleep(4)
        pydirectinput.keyDown('w')
        time.sleep(w)
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('d')
        time.sleep(d)
        pydirectinput.keyUp('d')
        pydirectinput.press('enter')
        tries += 1
        print("Tries:",tries,end='\r')
        time.sleep(d+w+6)
    print("Total tries:",tries)

print("Pick an action:")
print("0: AFK Mouse wiggle")
print("1: Kitty Claw game")

try:
    game = int(input().strip())
    signal.signal(signal.SIGINT, end)

    if game == 0:
        time.sleep(5)
        while not END:
            pydirectinput.move(20,0)
            time.sleep(5)
            if END: break
            pydirectinput.move(-20,0)
            time.sleep(5)

    elif game == 1: kittyClaw()

except:
    print("Not an option")
