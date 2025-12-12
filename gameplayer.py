import pyautogui, pydirectinput, time, signal, keyboard, sys, os, threading, queue, psutil, win32api, win32con
from multiprocessing import Process

END = False

def end(sig, frame):
    global END
    END = True
    print('ending...')

def gta_handler():
    global END
    needToType = False
    while not END:
        key = keyboard.read_key()
        pydirectinput.PAUSE=0.025
        if key == '=':
            needToType = not needToType
            time.sleep(1)
        if needToType: continue
        def gtapause(m):
            time.sleep(5)
            pydirectinput.press('esc')
            os.system('start "pause" /min cmd /c gameplayer.cmd -i ' + m)
            pydirectinput.click()
            # while True:
            #     key = keyboard.read_key()
            #     if key == 'P':
            #         os.system('start /min cmd /c taskkill /f /im powershell.exe>nul')
            #         return
        if key == 'p': gtapause("0")
        if key == 'P': gtapause("gtaafk")
        if key == '}':
            pydirectinput.PAUSE = 0.05
            pydirectinput.press(['enter','enter','enter','down','enter','esc','enter'
                                    ,'enter','enter','enter','enter','esc','esc','esc'
                                    ,'enter','enter','enter','enter','enter','down'
                                    ,'enter','esc','esc','esc','esc','enter'])
            pydirectinput.PAUSE = 0.025
        # if key == '}': #Launch Cayo
        #     pydirectinput.press(['e','e','right','enter','right','enter'])
        #     time.sleep(1)
        #     for _ in range(2):
        #         pydirectinput.press(['up','enter'])
        #         time.sleep(.2)
        #     pydirectinput.press('enter')
        #     time.sleep(5)
        #     pydirectinput.press(['enter','enter','esc','down','enter','up','enter','esc','down','enter','enter','esc','down','enter','down','enter','esc','down','enter','enter','right','enter'])
        #     time.sleep(.2)
        #     pydirectinput.press('enter')
        if key == '~': #Cut grate Cayo
            order = [
                ('d', [(.2, .19), (.2, .185), (.2, .17), (.2, .17), (.2, .17), (.2, .08)]),
                ('s', [(0, .07), (.2, .2), (.2, .23), (.2, .2), (.2, .2), (.2, .2), (.2, .23), (.2, .08)]),
                ('a', [(0, .07), (.2, .17), (.2, .185), (.2, .185), (.2, .18), (.2, .18), (.2, .07)]),
                ('w', [(0, .05), (.2, .2), (.2, .23), (.2, .2), (.2, .19), (.2, .22), (.2, .24)])
            ]

            pydirectinput.keyDown('w')
            pydirectinput.keyDown('a')
            time.sleep(.2)
            pydirectinput.keyUp('w')
            pydirectinput.keyUp('a')
            pydirectinput.keyDown('d')
            pydirectinput.keyDown('s')
            time.sleep(.15)
            pydirectinput.keyUp('s')
            time.sleep(.04)
            pydirectinput.keyUp('d')
            pydirectinput.mouseDown()
            for direction, ord in order:
                for tim, timer in ord:
                    time.sleep(tim)
                    pydirectinput.keyDown(direction)
                    time.sleep(timer)
                    pydirectinput.keyUp(direction)
            time.sleep(.3)
            pydirectinput.mouseUp()
        # if key == '~': #wall buffer
        #     pydirectinput.PAUSE=.01
        #     pydirectinput.press(['q','up','up'])
        #     time.sleep(1)
        #     pydirectinput.keyDown('w')
        #     time.sleep(1)
        #     pydirectinput.press('space')
        #     pydirectinput.keyUp('w')
        #     time.sleep(1)
        #     pydirectinput.press(['up','up'])
        #     time.sleep(1.5)
        #     pydirectinput.press('esc')
        #     time.sleep(1)
        #     pydirectinput.PAUSE=.1
        #     pydirectinput.press(['down','left'])
        #     pydirectinput.PAUSE=.01
        #     for _ in range(5):
        #         pydirectinput.press('enter')
        #         time.sleep(1.5)
        #         pydirectinput.press('esc')
        #         time.sleep(2)

        if key == ']':
            pydirectinput.keyDown('shift')
            time.sleep(.5)
            continue
        # if key == ']': #Find new session
        #     pydirectinput.PAUSE = .1
        #     for _ in range(7):
        #         pydirectinput.press('esc')
        #         time.sleep(.3)
        #         pydirectinput.press('right')
        #         time.sleep(.65)
        #         pydirectinput.press('enter')
        #         time.sleep(.3)
        #         pydirectinput.press(['up', 'up', 'up', 'up', 'up', 'enter'])
        #         time.sleep(.35)
        #         pydirectinput.press(['down', 'enter', 'enter'])
        #         time.sleep(20)
        # if key == '[': #Gang Wars automation
        #     sleeper = False
        #     if sleeper: #Do one less than main and tap '[' when main starts game
        #         for _ in range(20):
        #             pydirectinput.press('e')
        #             time.sleep(20)
        #             pydirectinput.press('enter')
        #             time.sleep(70)
        #             pydirectinput.keyDown('del')
        #             time.sleep(2)
        #             pydirectinput.keyUp('del')
        #             time.sleep(5.75)
        #     else:
        #         pydirectinput.PAUSE=0.35
        #         char = 'd','s' #Hoods: 'd','w' for Punks ; Yokels: 'd','s' for Bikers ; and opposite directions for opposites
        #         char2 = 'a' if char[0] == 'd' else 'd','s' if char[1] == 'w' else 'w'
        #         for _ in range(21):
        #             pydirectinput.press(['e','e','e'])
        #             time.sleep(25)
        #             pydirectinput.press('enter')
        #             time.sleep(9)
        #             pydirectinput.press([char[0],char[0],char[0],char[0],char[1],char[1],char[0],char[0],char[0],char[0],char[0],char[0],char2[1],char2[1],char2[0]])
        #             pydirectinput.press(['space','space','space','space'])
        #             time.sleep(14)
        #             pydirectinput.press([char[0],char[0],char[0],char[0],char[1],char[1],char[0],char[0],char[0],char[0],char[0],char[0],char2[1],char2[1],char2[0]])
        #             pydirectinput.press(['space','space','space','space'])
        #             pydirectinput.keyDown('del')
        #             time.sleep(2)
        #             pydirectinput.keyUp('del')
        #             time.sleep(15)

        if key in "hHjJkKlC'-":
            pydirectinput.press(['m','down','down'])
            if key in "hjHJ":
                pydirectinput.press(['down','enter','up'])
                if key in "hj": pydirectinput.press(['up','enter','down'])
                if key == 'j': pydirectinput.press(['down','down','enter','up','up'])
                if key in 'HJ': pydirectinput.press(['enter','down'])
                if key == 'J': pydirectinput.press(['down','enter','down'])
                pydirectinput.press('enter')

            elif key in "Kkl'C":
                if key in "'l": pydirectinput.press(['enter','down','down'])
                if key == 'k': pydirectinput.press('enter')
                if key == 'K':
                    pydirectinput.press(['enter','down','left','enter'])
                    continue
                if key == "'":
                    for i in range(5): pydirectinput.press('right')
                    while key not in ['esc','enter']:
                        key = keyboard.read_key()
                        time.sleep(.15)
                        if key == 'right':
                            for _ in range(5): pydirectinput.press('right')

                elif key == "l":
                    pydirectinput.press(['down','down','down'])

                elif key == 'C':
                    time.sleep(2)
                    pydirectinput.press(['down','down','down','enter','down','down','down','left','left'])
                pydirectinput.press(['enter','m'])

            if key == '-':
                pydirectinput.press(['down','down','enter','enter'])
                for _ in range(8): pydirectinput.press(['left','up','enter','down'])
                pydirectinput.press('m')

        elif key == ";":
            pydirectinput.press('up')
            time.sleep(.6)
            pydirectinput.PAUSE=.2
            pydirectinput.press(['right','up','enter','enter'])
            pydirectinput.PAUSE=0.01
            time.sleep(5)
            pydirectinput.press(['down','enter'])
        elif key == ":":
            pydirectinput.press(['m','enter','up','up','up','enter','up','up','enter'])

        elif key == "n":
            time.sleep(.25)
            key = keyboard.read_key()
            pydirectinput.PAUSE = .06
            pydirectinput.press('p')
            time.sleep(.3)
            pydirectinput.press('right')
            time.sleep(.65)
            pydirectinput.press('enter')
            time.sleep(.1)
            pydirectinput.press('enter')
            time.sleep(.2)
            pydirectinput.press('down')
            time.sleep(.1)
            pydirectinput.press('enter')
            time.sleep(.1)
            pydirectinput.press('enter')
            time.sleep(.6)
            pydirectinput.press(['up', 'up', 'up','up'])
            time.sleep(.1)
            pydirectinput.press('enter')
            time.sleep(.25)
            pydirectinput.PAUSE = .01
            if key in 'abcv':
                val = 4
                if key in 'bcv': val += 4
                if key in 'cv': val += 5
                if key == 'v': val += 3
                pydirectinput.press(['down' for _ in range(val)])
            elif key in 'fhnom':
                val = 5
                if key in 'hfnm': val += 1
                if key in 'hfm': val += 4
                if key in 'hf': val += 2
                if key == 'f': val += 3
                pydirectinput.press(['up' for _ in range(val)])

            while True:
                time.sleep(.2)
                key = keyboard.read_key()
                if key == 'enter':
                    time.sleep(.2)
                    key = keyboard.read_key()
                    if key == 'enter':
                        time.sleep(4)
                        while True:
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
                            time.sleep(.01)
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
                            time.sleep(.1)
                            if pyautogui.pixel(200, 200) == (0, 0, 0): break
                        pydirectinput.press('enter')
                        break
                    elif key == 'esc':
                        continue
                elif key == 'esc':
                    break

        elif key == '"':
            if "AutoHotkey.exe" in (p.name() for p in psutil.process_iter()):
                time.sleep(1)
                pydirectinput.keyDown('ctrl')
                pydirectinput.keyDown('f12')
                time.sleep(.2)
                pydirectinput.keyUp('ctrl')
                pydirectinput.keyUp('f12')
                time.sleep(5)
                os.system("start /min cmd /c taskkill /f /im AutoHotkey.exe>nul")
            else:
                os.system("start /min cmd /c V1.1_nosavingmethod.ahk")
                time.sleep(1)
                pydirectinput.keyDown('ctrl')
                pydirectinput.keyDown('f9')
                time.sleep(.2)
                pydirectinput.keyUp('ctrl')
                pydirectinput.keyUp('f9')

def bl3_farmer():
    global END
    while not END:
        key = keyboard.read_key()
        pydirectinput.PAUSE=0.01
        if key == "up":
            pydirectinput.press('esc')
            time.sleep(.1)
            pydirectinput.click(300,900)
            time.sleep(.3)
            for _ in range(5):
                time.sleep(.1)
                pydirectinput.click(700,850)
            time.sleep(1)
            for _ in range(5):
                pydirectinput.moveTo(200,250)
                pydirectinput.press('enter')
                time.sleep(.4)

def raceAndChase():
    for _ in range(40):
        for _ in range(10):
            pydirectinput.press('enter')
            time.sleep(0.5)
        pydirectinput.keyDown('shift')
        time.sleep(40)
        pydirectinput.keyUp('shift')
        time.sleep(30)

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
    elif piece == "SWK":
        while True:
            try:
                w = float(input("Enter value to try for back: "))
                d = float(input("Enter value to try for right: "))
                break
            except: print("Must be a float value")
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

def professorOfLove():
    time.sleep(5)
    # set up Nazar left of game and have sleeper repeat 'e' every second for very long. Main needs first person
    while not END:
        for _ in range(4):
            pydirectinput.press(['e','e','e'])
            time.sleep(30)
        pydirectinput.keyDown('d')
        time.sleep(.5)
        pydirectinput.keyUp('d')
        pydirectinput.keyDown('w')
        time.sleep(1)
        pydirectinput.keyUp('w')
        pydirectinput.press(['e', 'e', 'e'])
        time.sleep(25)
        pydirectinput.keyDown('a')
        time.sleep(.5)
        pydirectinput.keyUp('a')

def grogJump():
    pydirectinput.PAUSE=0.01
    while not END:
        space = keyboard.read_key()
        if space == 'space':
            pydirectinput.press('left')

def movePenetrator(num,slot,pos1,pos2):
    wall = num-pos1
    flip = not num <3
    right = True
    slotDiff = slot - pos2
    if abs(wall) == 2:
        distance = 5
        if pos2 in [2,3] and slot in [2,3]: distance += 2
        distance += abs(slot-pos2)

        if pos2 <3:
            right = not right
            if pos2 == 2 and slot == 4: right = not right
        elif pos2 == 3 and slot == 1: right = not right
        if num < pos1: right = not right
    elif wall == 0:
        right = slotDiff > 0
        if flip: right = not right
        distance = abs(slotDiff)
    else:
        if abs(wall) > 2: right = not right
        if wall < 0: right = not right
        if abs(pos1-num) == 3: distance = pos2+slot-1
        elif pos1+num == 5: distance = 9-pos2-slot
        elif (pos1 == 1 and num == 2) or (pos1 == 4 and num == 3): distance = 4 - pos2 + slot
        else: distance = 4 + pos2 - slot
    direction = 'd' if right else 'a'

    pydirectinput.press([direction for _ in range(distance)])
    time.sleep(.2)
    pydirectinput.press(['space'])

def penetrator():
    print("  1  2  3  4  ")
    print("1  ---------  1")
    print("2 |         | 2")
    print("3 |         | 3")
    print("4  ---------  4")
    print("  1  2  3  4  ")

    pos1, pos2 = 1, 1
    pydirectinput.PAUSE=0.03
    while not END:
        key = keyboard.read_key()
        if key == "up":
            while key == "up": key = keyboard.read_key()
            if key in "1234":
                movePenetrator(1,int(key),pos1,pos2)
                pos1,pos2 = 1,int(key)

        elif key == "right":
            while key == "right": key = keyboard.read_key()
            if key in "1234":
                movePenetrator(2,int(key),pos1,pos2)
                pos1,pos2 = 2,int(key)

        elif key == "down":
            while key == "down": key = keyboard.read_key()
            if key in "1234":
                movePenetrator(3,int(key),pos1,pos2)
                pos1,pos2 = 3,int(key)

        elif key == "left":
            while key == "left": key = keyboard.read_key()
            if key in "1234":
                movePenetrator(4,int(key),pos1,pos2)
                pos1,pos2 = 4,int(key)

        elif key == "enter": pos1,pos2 = 1,1

def autoPenetrator():
    pos1,pos2 = 1,1
    locations = [
        (1645,660),(1685,660),(1750,660),(1790,660),
        (1840,700),(1840,750),(1840,810),(1840,850),
        (1645,900),(1685,900),(1750,900),(1790,900),
        (1600,700),(1600,750),(1600,810),(1600,850)
    ]
    pydirectinput.PAUSE=0.01
    time.sleep(5)
    pydirectinput.press('enter')

    def movementQueue(q,stop_event):
        while not stop_event.is_set() or not q.empty():
            try:
                bullet = q.get()
                movePenetrator(bullet[0],bullet[1],bullet[2],bullet[3])
                time.sleep(.2)
            except: pass

    bulletQueue = queue.Queue()
    stop_event = threading.Event()
    movementThread = threading.Thread(target=movementQueue,args=(bulletQueue,stop_event))
    movementThread.start()

    while not END:
        screen = pyautogui.screenshot()
        if screen.getpixel((1730,765))[0] > 100 and screen.getpixel((1730,765))[1] > 100:
            pos1,pos2 = 1,1

            time.sleep(4)
            continue
        for i in range(len(locations)):
            x,y = locations[i]
            if screen.getpixel((x,y))[1] > 100:
                bulletQueue.put((i//4+1,i%4+1,pos1,pos2))
                pos1,pos2 = i//4+1,i%4+1
        time.sleep(1)
    stop_event.set()
    movementThread.join()

def back_and_fourth():
    time.sleep(5)
    backFourth = ['','left','right']
    val = 1
    while not END:
        pydirectinput.keyDown(backFourth[val])
        for i in range(12):
            pydirectinput.press('z')
            time.sleep(.5)
        pydirectinput.keyUp(backFourth[val])
        val = -val

def pokeSlots():
    while not END:
        pydirectinput.PAUSE=0.5
        pydirectinput.press(['down', 'down', 'down'])
        pydirectinput.press(['x', 'x', 'x'])
        time.sleep(2)

def core_reduce(app, core):
    cmd = 'powershell "ForEach($PROCESS in GET-PROCESS '
    cmd += app
    cmd += ') { $PROCESS.ProcessorAffinity='
    cmd += str(int('1'*int(core),2)) + '"}'
    os.system(cmd)

def repeater(key,timer,times):
    def repeats():
        time.sleep(10)
        for _ in range(times):
            if key == 'lclick': pydirectinput.leftClick()
            elif key == 'rclick': pydirectinput.rightClick()
            else: pydirectinput.press(key)
            time.sleep(timer)
    execute_program_process = Process(target=repeats)
    execute_program_process.start()
    while True:
        if keyboard.is_pressed('ctrl+c') or not execute_program_process.is_alive():
            execute_program_process.terminate()
            break

def spammer(key, stopKey):
    pydirectinput.PAUSE=0.01
    while not END:
        K = keyboard.read_key()
        if K == stopKey: pydirectinput.press(key)

def newSession():
    pydirectinput.PAUSE = .01
    pydirectinput.press('esc')
    while True:
        time.sleep(.3)
        pydirectinput.press('right')
        time.sleep(.65)
        if pyautogui.pixel(1190, 270) != (240, 240, 240):
            pydirectinput.press('esc')
            time.sleep(5)
            pydirectinput.press('esc')
            continue
        pydirectinput.press('enter')
        time.sleep(.5)
        for i in range(5):
            pydirectinput.keyDown('up')
            time.sleep(.05)
            pydirectinput.keyUp('up')
            time.sleep(1)
        if pyautogui.pixel(1180, 1050) == (240, 240, 240): break
        pydirectinput.press(['esc', 'left'])
    pydirectinput.press('enter')
    time.sleep(.35)
    for _ in range(10):
        pydirectinput.keyDown('down')
        time.sleep(.05)
        pydirectinput.keyUp('down')
        time.sleep(.5)
        if pyautogui.pixel(1180, 400) == (240, 240, 240): break
    else:
        pydirectinput.press('esc')
        time.sleep(4)
        pydirectinput.press('esc')
        newSession()
        return
    time.sleep(.1)
    pydirectinput.press(['enter', 'enter','enter'])
    time.sleep(17)

def gtaafk():
    time.sleep(3)
    pydirectinput.PAUSE = .1
    Casino = False
    Claim = False
    Bunker = False
    Staff = True
    # Hangar = True

    while True:
        if Claim or Staff:
            while True:
                pydirectinput.PAUSE = .2
                pydirectinput.press('up')
                time.sleep(.6)
                pydirectinput.press(['right', 'enter'])
                time.sleep(1)
                if Claim:
                    pydirectinput.press(['enter','enter'])
                    pydirectinput.PAUSE = .01
                    for _ in range(8):
                        time.sleep(2)
                        pydirectinput.press(['down', 'enter'])
                    pydirectinput.press('backspace')
                    time.sleep(.5)
                    pydirectinput.press(['backspace','backspace'])
                if Staff:
                    pydirectinput.PAUSE = .01
                    for _ in range(20):
                        pydirectinput.keyDown('up')
                        time.sleep(.05)
                        pydirectinput.keyUp('up')
                        if sum(pyautogui.pixel(840, 490)) > 550: break
                        time.sleep(.2)
                    else:
                        pydirectinput.press(['backspace','backspace','backspace'])
                        continue
                    pydirectinput.press('enter')
                    time.sleep(.5)
                    pydirectinput.press('enter')
                    time.sleep(.2)
                    for _ in range(20):
                        pydirectinput.keyDown('down')
                        time.sleep(.05)
                        pydirectinput.keyUp('down')
                        if sum(pyautogui.pixel(840, 300)) > 550: break
                        time.sleep(.2)
                    else:
                        pydirectinput.press(['backspace', 'backspace', 'backspace'])
                        continue
                    pydirectinput.press('enter')
                    time.sleep(.5)
                    for _ in range(5):
                        pydirectinput.press('enter')
                        time.sleep(1)
                        pydirectinput.keyDown('down')
                        time.sleep(.05)
                        pydirectinput.keyUp('down')
                        time.sleep(.2)
                    pydirectinput.press('backspace')
                    time.sleep(.5)
                    pydirectinput.press(['down', 'enter'])
                    time.sleep(.5)
                    for _ in range(2):
                        pydirectinput.press('enter')
                        time.sleep(1)
                        pydirectinput.keyDown('down')
                        time.sleep(.05)
                        pydirectinput.keyUp('down')
                        time.sleep(.2)
                    pydirectinput.press(['backspace','backspace'])
                pydirectinput.press(['backspace','backspace'])
                break
        if Casino:
            pydirectinput.press(['e','tab','enter','enter'])
            time.sleep(1)
            pydirectinput.press('esc')
        elif Bunker:
            pydirectinput.press('e')
            time.sleep(5)
            pydirectinput.press('enter')
            time.sleep(5)
            pydirectinput.moveTo(1680,850)
            pydirectinput.press('enter')
            time.sleep(.4)
            pydirectinput.moveTo(1050,660)
            pydirectinput.press('enter')
            time.sleep(.4)
            pydirectinput.moveTo(1680,1050)
            pydirectinput.press('enter')
            time.sleep(.4)
            pydirectinput.moveTo(1850,830)
            pydirectinput.press('enter')
            time.sleep(.4)
            pydirectinput.press('esc')
            time.sleep(.4)
            pydirectinput.press('esc')
            time.sleep(8)

            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            time.sleep(.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        # elif Hangar:
        #     while True:
        #         newSession()
        #         pydirectinput.PAUSE = .1
        #         pydirectinput.keyDown('w')
        #         time.sleep(.2)
        #         for _ in range(5):
        #             pydirectinput.keyDown('a')
        #             time.sleep(.2)
        #             pydirectinput.keyUp('a')
        #         time.sleep(.65)
        #         pydirectinput.keyUp('w')
        #         pydirectinput.keyDown('d')
        #         pydirectinput.keyDown('s')
        #         time.sleep(3)
        #         pydirectinput.keyUp('d')
        #         pydirectinput.keyUp('s')
        #         pydirectinput.keyDown('w')
        #         time.sleep(.45)
        #         pydirectinput.keyUp('w')
        #         pydirectinput.keyDown('d')
        #         time.sleep(3)
        #         pydirectinput.keyUp('d')
        #         pydirectinput.keyDown('s')
        #         time.sleep(2)
        #         pydirectinput.keyUp('s')
        #         pydirectinput.keyDown('a')
        #         time.sleep(3)
        #         pydirectinput.keyUp('a')
        #         time.sleep(.1)
        #         pydirectinput.keyDown('w')
        #         time.sleep(.2)
        #         pydirectinput.keyDown('d')
        #         time.sleep(1)
        #         pydirectinput.keyUp('w')
        #         time.sleep(2)
        #         pydirectinput.keyUp('d')
        #         pydirectinput.keyDown('w')
        #         time.sleep(1.5)
        #         pydirectinput.keyUp('w')
        #         pydirectinput.keyDown('a')
        #         time.sleep(.3)
        #         pydirectinput.keyUp('a')
        #         pydirectinput.keyDown('w')
        #         time.sleep(2.1)
        #         pydirectinput.keyUp('w')
        #         pydirectinput.keyDown('d')
        #         time.sleep(1.2)
        #         pydirectinput.keyUp('d')
        #         for _ in range(3):
        #             pydirectinput.keyDown('w')
        #             time.sleep(.15)
        #             pydirectinput.keyUp('w')
        #             time.sleep(.5)
        #             pydirectinput.press('e')
        #             time.sleep(.2)
        #             if pyautogui.pixel(850,60) == (0,0,0):
        #                 pydirectinput.press(['enter','enter'])
        #                 break
        #         else: continue
        #         break
        #     def changespawn(direction):
        #         pydirectinput.PAUSE = .01
        #         while True:
        #             time.sleep(1)
        #             pydirectinput.press('m')
        #             time.sleep(.3)
        #             for _ in range(3):
        #                 pydirectinput.keyDown('up')
        #                 time.sleep(.05)
        #                 pydirectinput.keyUp('up')
        #                 time.sleep(.1)
        #             if sum(pyautogui.pixel(800,425)) > 550: break
        #             else: pydirectinput.press('m')
        #         time.sleep(.5)
        #         pydirectinput.press('enter')
        #         time.sleep(.5)
        #         pydirectinput.keyDown(direction)
        #         time.sleep(.01)
        #         pydirectinput.keyUp(direction)
        #         time.sleep(.5)
        #         pydirectinput.press('m')
        #         time.sleep(2)
        #     changespawn('left')
        #     newSession()
        #     changespawn('right')
        #     pydirectinput.PAUSE = .1

        for _ in range(50):
            time.sleep(60)
            pydirectinput.move(20,0)
def run_gtaafk():
    execute_program_process = Process(target=gtaafk)
    execute_program_process.start()
    while True:
        if keyboard.is_pressed('ctrl+c') or not execute_program_process.is_alive():
            execute_program_process.terminate()
            break

# def golfta():
#     while not END:
#         key = keyboard.read_key()
#         pydirectinput.PAUSE=0.1
#         if key == 'right':
#             time.sleep(.5)
#             pydirectinput.press(['enter','down','enter','down','enter','down','down','enter'])
#             time.sleep(.3)
#             pydirectinput.press(['up','enter','enter'])

# def gtaclubber():
#     pydirectinput.PAUSE = .2
#     time.sleep(5)
#     owner = True
#     if owner:
#         while not END:
#             while True:
#                 time.sleep(1)
#                 pydirectinput.press('p')
#                 time.sleep(1.5)
#                 pydirectinput.press(['right','enter'])
#                 time.sleep(1)
#                 r,g,b = pyautogui.pixel(1180, 340)
#                 if r > 200 and g > 200 and b > 200: break
#                 else: pyautogui.press('p')
#             pydirectinput.press(['up','up','up','up','up','enter'])
#             time.sleep(.5)
#             pydirectinput.press(['down','enter','enter'])
#             time.sleep(10)
#             pydirectinput.press(['p','right','right','right'])
#             time.sleep(2)
#             pydirectinput.press(['enter','enter','enter','p'])
#             time.sleep(1)
#             pydirectinput.press(['m','enter','enter'])
#             while pyautogui.pixel(633, 224)[0] < 50: time.sleep(.1)
#             pydirectinput.press('enter')
#             time.sleep(2)
#             pydirectinput.press('m')
#             time.sleep(5)
#     else:
#         while not END:
#             while True:
#                 r,g,b = pyautogui.pixel(2325, 57)
#                 if [r,g,b] == [255,255,0]: break
#                 else: time.sleep(.1)
#             pydirectinput.press(['p','right','right','right'])
#             time.sleep(2)
#             pydirectinput.press(['enter','enter','enter','enter'])
#             time.sleep(1)
#             pydirectinput.press('enter')
#             while True:
#                 pydirectinput.press('up')
#                 r,g,b = pyautogui.pixel(2285, 1150)
#                 if [r,g,b] == [255,0,0]: break
#                 else: time.sleep(.1)
#             pydirectinput.press(['esc','up','enter','enter','enter'])

def mouseCursorInfo():
    while not END:
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)
        print(f"Mouse at: ({x}, {y}) | RGB Color: ({r}, {g}, {b})           ",end='\r')
        time.sleep(0.1)

def wiggle():
    while True:
        pydirectinput.move(20, 0)
        time.sleep(5)
        if END: break
        pydirectinput.move(-20, 0)
        time.sleep(5)

def vipWait():
    time.sleep(5)
    while True:
        key = keyboard.read_key()
        if key == 'z':
            newSession()
            time.sleep(5*60)
            pydirectinput.press('up')
            time.sleep(.6)
            pydirectinput.PAUSE=.2
            pydirectinput.press(['right','up','enter','up','enter'])
            pydirectinput.PAUSE=0.01
            time.sleep(5)
            pydirectinput.press('enter')


if __name__ == '__main__':
    if '-i' in sys.argv: game = sys.argv[2:]
    else:
        print("Pick an action:")
        print("0: AFK Mouse wiggle")
        print("1: Kitty Claw game")
        print("2: Back and fourth")
        print("3: Pokemon Slots")
        print("4: Professor of Love")
        print("5: Grog Jump always kick")
        print("6: Penetrator input")
        print("7: Auto Penetrator")
        print("8: Mouse Curser location")
        print("repeat <key> <time> <times>: Repeater")
        print("spam <key> <trigger key>: Spam key on trigger key hold")
        print("gta: gta quick keys")
        print("gtaafk: claim business earnings afk")
        # print("bl3: reset helper")
        print("core <app> <count>: Core Reduce")

        game = input().strip().split()
    signal.signal(signal.SIGINT, end)

    if game[0] == "0":
        execute_program_process = Process(target=wiggle)
        execute_program_process.start()
        while True:
            if keyboard.is_pressed('ctrl+c') or not execute_program_process.is_alive():
                execute_program_process.terminate()
                break

    elif game[0] == "1": kittyClaw()
    elif game[0] == "2": back_and_fourth()
    elif game[0] == "3": pokeSlots()
    elif game[0] == "4": professorOfLove()
    elif game[0] == "5": grogJump()
    elif game[0] == "6": penetrator()
    elif game[0] == "7": autoPenetrator()
    elif game[0] == "8": mouseCursorInfo()
    elif game[0] == "repeat" and len(game) == 4: repeater(game[1],float(game[2]),int(game[3]))
    elif game[0] == "spam" and len(game) == 3: spammer(game[1],game[2])
    elif game[0] == "gta": gta_handler()
    elif game[0] == "gtaafk": run_gtaafk()
    elif game[0] == "vip": vipWait()
    # elif game[0] == "golfta": golfta()
    # elif game[0] == "gtaclubber": gtaclubber()
    # elif game[0] == "bl3": bl3_farmer()
    # elif game[0] == "core":
    #     if len(game) == 1:
    #         try:
    #             gamesList = [ 'GTA5',
    #                           'HogwartsLegacy',
    #                           'Overwatch2',
    #                           'Valorant',
    #                           'Borderlands3',
    #                           'Witcher3',
    #                           'Minecraft',
    #                           ]
    #             for gameName in gamesList: core_reduce(gameName,16)
    #             core_reduce('Cyberpunk2077',18)
    #         except: pass
    #     else: core_reduce(game[1],game[2])
    else: print("Not an option")