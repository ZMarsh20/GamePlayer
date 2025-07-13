import pyautogui, pydirectinput, time, signal, keyboard, sys, os, threading, queue

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
        pydirectinput.PAUSE=0.02
        if key == '=':
            needToType = not needToType
            time.sleep(1)
        if needToType: continue
        if key == 'p':
            time.sleep(1)
            os.system("start /min gameplayer.cmd -i gtaafk")
            pydirectinput.click()
        if key == '}': #Launch Cayo
            pydirectinput.press(['e','e','right','enter','right','enter'])
            time.sleep(1)
            for _ in range(2):
                pydirectinput.press(['up','enter'])
                time.sleep(.2)
            pydirectinput.press('enter')
            time.sleep(5)
            pydirectinput.press(['enter','enter','esc','down','enter','up','enter','esc','down','enter','enter','esc','down','enter','down','enter','esc','down','enter','enter','right','enter'])
            time.sleep(.2)
            pydirectinput.press('enter')
        if key == ']': #Cut grate Cayo
            def wiggle(k):
                if k == 'd': back = 'a'
                if k == 'w': back = 's'
                if k == 's': back = 'w'
                if k == 'a': back = 'd'
                pydirectinput.keyDown(back)
                time.sleep(.06)
                pydirectinput.keyUp(back)
                pydirectinput.keyDown(k)
                time.sleep(.06)
                pydirectinput.keyUp(k)

            def burn(k,bars,space):
                pydirectinput.keyDown(k)
                time.sleep(.03)
                for _ in range(bars):
                    pydirectinput.keyDown(k)
                    time.sleep(space)
                    pydirectinput.keyUp(k)
                    wiggle(k)
            def angle(k1,k2):
                pydirectinput.keyDown(k1)
                pydirectinput.keyDown(k2)
                time.sleep(0.06)
                pydirectinput.keyUp(k1)
                pydirectinput.keyUp(k2)
                wiggle(k2)

            pydirectinput.mouseDown()
            time.sleep(.2)
            burn('d',5,0.165)
            angle('d','s')
            burn('s',6,0.2)
            angle('s','a')
            burn('a',5,0.165)
            angle('a','w')
            burn('w',6,0.2)
            pydirectinput.mouseUp()

            if False: #incase I want to try arbitrary timing for grate cut WIP
                locations = [
                    #top
                    (1125, 230), (1180, 390),
                    (1275, 230), (1305, 390),
                    (1350, 230), (1440, 390),
                    (1495, 230), (1560, 390),
                    (1620, 230), (1680, 390),
                    (1755, 230), (1830, 390),
                    # right
                    (1795, 280), (1890, 480),
                    (1795, 430), (1890, 590),
                    (1795, 530), (1890, 690),
                    (1795, 675), (1890, 835),
                    (1795, 800), (1890, 960),
                    (1795, 905), (1890, 1065),
                    (1795, 1000), (1890, 1160),
                    # bottom
                    (1660, 1110), (1720, 1320),
                    (1530, 1110), (1610, 1320),
                    (1420, 1110), (1500, 1320),
                    (1300, 1110), (1360, 1320),
                    (1150, 1110), (1220, 1320),
                    (1020, 1110), (1100, 1320),
                    # left
                    (950, 1030), (1020, 1220),
                    (950, 900), (1020, 1090),
                    (950, 800), (1020, 990),
                    (950, 670), (1020, 860),
                    (980, 560), (1070, 730),
                    (980, 420), (1070, 590),
                    (980, 300), (1070, 470)
                ]
                def movement(q, stop_event):
                    while not stop_event.is_set():
                        try:
                            bullet = q.get()
                            movePenetrator(bullet[0], bullet[1], bullet[2], bullet[3])
                            time.sleep(.2)
                        except:
                            pass

                bulletQueue = queue.Queue()
                stop_event = threading.Event()
                movementThread = threading.Thread(target=movement, args=(bulletQueue, stop_event))
                movementThread.start()


                while not END:
                    screen = pyautogui.screenshot()
                    for i in range(0,len(locations),2):
                        x, y = locations[i]
                        x2,y2 = locations[i+1]
                        if screen.getpixel((x, y))[1] > 100:
                            pos1, pos2 = i // 4 + 1, i % 4 + 1
                    time.sleep(1)
                stop_event.set()
                movementThread.join()
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

        if key == '~':
            pydirectinput.PAUSE=.01
            pydirectinput.press(['q','up','up'])
            time.sleep(1)
            pydirectinput.keyDown('w')
            time.sleep(1)
            pydirectinput.press('space')
            pydirectinput.keyUp('w')
            time.sleep(1)
            pydirectinput.press(['up','up'])
            time.sleep(1.5)
            pydirectinput.press('esc')
            time.sleep(1)
            pydirectinput.PAUSE=.1
            pydirectinput.press(['down','left'])
            pydirectinput.PAUSE=.01
            for _ in range(5):
                pydirectinput.press('enter')
                time.sleep(1.5)
                pydirectinput.press('esc')
                time.sleep(2)

        if key in "hjklc'-":
            pydirectinput.press(['m','down','down'])
            if key in "hj":
                pydirectinput.press(['down','enter','up','up','enter','down'])

                if key == 'j': pydirectinput.press(['down','down','enter','up','up'])
                pydirectinput.press('enter')

            elif key in "kl'c":
                if key in "'l": pydirectinput.press(['enter','down','down'])
                elif key == 'k': pydirectinput.press('enter')

                if key == "'":
                    for i in range(5): pydirectinput.press('right')
                    while key not in ['esc','enter']:
                        key = keyboard.read_key()
                        time.sleep(.15)
                        if key == 'right':
                            for _ in range(5): pydirectinput.press('right')

                elif key == "l":
                    pydirectinput.press(['down','down','down'])

                elif key == 'c':
                    time.sleep(2)
                    pydirectinput.press(['down','down','down','enter','down','down','down','left','left'])
                pydirectinput.press(['enter','m'])

            if key == '-':
                pydirectinput.press(['down','down','enter','enter'])
                for _ in range(8): pydirectinput.press(['left','down','enter','up'])
                pydirectinput.press('m')

        elif key == ";":
            pydirectinput.press('up')
            time.sleep(.6)
            pydirectinput.PAUSE=.2
            pydirectinput.press(['right','up','enter','enter'])
            pydirectinput.PAUSE=0.01
            time.sleep(5)
            pydirectinput.press(['down','enter'])

        elif key == "n":
            pydirectinput.PAUSE=.15
            pydirectinput.press('esc')
            time.sleep(.3)
            pydirectinput.press('right')
            time.sleep(.65)
            pydirectinput.press(['enter','enter','down','enter','enter'])
            time.sleep(.35)
            pydirectinput.press(['up','up','up','enter'])

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
    time.sleep(10)
    for _ in range(times):
        pydirectinput.press(key)
        time.sleep(timer)

def spammer(key, stopKey):
    pydirectinput.PAUSE=0.01
    while not END:
        K = keyboard.read_key()
        if K == stopKey: pydirectinput.press(key)

def gtaafk():
    time.sleep(5)
    pydirectinput.press('esc')
    time.sleep(5)
    while True:
        pydirectinput.PAUSE = .2
        pydirectinput.press('up')
        time.sleep(.6)
        pydirectinput.press(['right', 'enter'])
        time.sleep(1)
        pydirectinput.press(['enter','enter'])
        pydirectinput.PAUSE = .01
        for _ in range(8):
            time.sleep(2)
            pydirectinput.press(['down','enter'])
        pydirectinput.press(['backspace','backspace'])
        for _ in range(48):
            time.sleep(60)
            pydirectinput.move(20,0)


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
    print("repeat <key> <time> <times>: Repeater")
    print("spam <key> <trigger key>: Spam key on trigger key hold")
    print("gta: gta quick keys")
    print("bl3: reset helper")
    print("core <app> <count>: Core Reduce")

    game = input().strip().split()
signal.signal(signal.SIGINT, end)

if game[0] == "0":
    time.sleep(5)
    while not END:
        pydirectinput.move(20,0)
        time.sleep(5)
        if END: break
        pydirectinput.move(-20,0)
        time.sleep(5)
elif game[0] == "1": kittyClaw()
elif game[0] == "2": back_and_fourth()
elif game[0] == "3": pokeSlots()
elif game[0] == "4": professorOfLove()
elif game[0] == "5": grogJump()
elif game[0] == "6": penetrator()
elif game[0] == "7": autoPenetrator()
elif game[0] == "repeat" and len(game) == 4: repeater(game[1],float(game[2]),int(game[3]))
elif game[0] == "spam" and len(game) == 3: spammer(game[1],game[2])
elif game[0] == "gta": gta_handler()
elif game[0] == "gtaafk": gtaafk()
elif game[0] == "bl3": bl3_farmer()
elif game[0] == "core":
    if len(game) == 1:
        try:
            gamesList = [ 'GTA5',
                          'HogwartsLegacy',
                          'Overwatch2',
                          'Valorant',
                          'Borderlands3',
                          'Witcher3',
                          'Minecraft',
                          ]
            for gameName in gamesList: core_reduce(gameName,16)
            core_reduce('Cyberpunk2077',18)
        except: pass
    else: core_reduce(game[1],game[2])

else: print("Not an option")