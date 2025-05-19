import pyautogui, pydirectinput, time, signal, keyboard, sys, os

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
        pydirectinput.PAUSE=0.01
        if key == '=':
            needToType = not needToType
            time.sleep(1)
        if needToType: continue
        if key == 'p':
            time.sleep(1)
            os.system("start /min gameplayer.cmd -i 0")
            pydirectinput.click()
        if key == ']':
            def burn(k,bars,space):
                for _ in range(bars):
                    time.sleep(0.2)
                    pydirectinput.keyDown(k)
                    time.sleep(space)
                    pydirectinput.keyUp(k)
                time.sleep(0.3)
            def angle(k1,k2):
                pydirectinput.keyDown(k1)
                pydirectinput.keyDown(k2)
                time.sleep(0.1)
                pydirectinput.keyUp(k1)
                pydirectinput.keyUp(k2)
                time.sleep(0.3)

            pydirectinput.mouseDown()
            burn('d',5,0.195)
            angle('d','s')
            burn('s',6,0.215)
            angle('s','a')
            burn('a',5,0.195)
            angle('a','w')
            burn('w',6,0.215)
            pydirectinput.mouseUp()
        # if key == '[':
        #     sleeper = False
        #     if sleeper:
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
        #         char = 'd','s'
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
                pydirectinput.press(['enter','esc','esc'])

            if key == '-':
                pydirectinput.press(['down','down','enter','enter'])
                for _ in range(8): pydirectinput.press(['left','down','enter','up'])
                pydirectinput.press(['esc','esc','esc'])

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

if '-i' in sys.argv: game = sys.argv[2:]
else:
    print("Pick an action:")
    print("0: AFK Mouse wiggle")
    print("1: Kitty Claw game")
    print("2: Back and fourth")
    print("3: Pokemon Slots")
    print("repeat <key> <time> <times>: Repeater")
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
elif game[0] == "repeat" and len(game) == 4: repeater(game[1],float(game[2]),int(game[3]))
elif game[0] == "gta": gta_handler()
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
