#!/usr/bin/env python3
# macro scripts for external keyboards
# remember to add your user to input group
# MIT License
# by Fran Sanchez May 2020

import os
import signal, sys # catch CTRL-C
import psutil # check running processes
import subprocess
from evdev import InputDevice, categorize, ecodes as e
import time, rtmidi, mido
import notify2

# init notification system
notify2.init('Deck controller')

# CONTROL-C
## def signal_handler(sig, frame):
    #print('You pressed Ctrl+C!')
    #exit()

# detect apple keyboard
try:
    dev = InputDevice('/dev/input/by-id/usb-Apple__Inc_Apple_Keyboard-event-kbd')
    dev.grab()
    os.system('clear') # clear console
    print ('Apple keyboard connected')
    notify2.Notification("Deck activated","Apple keyboard connected").show()
    #print('Press Ctrl+C to exit')
except:
    print ('Apple keyboard NOT connected or another program grabbing it!')
    sys.exit(0)

# os-system aliases
cable = 'sudo ip link set cable0 up && sudo dhcpcd cable0'
online='sudo wifi-menu'
loopcam='sudo modprobe v4l2loopback video_nr=9'
htop='uxterm -b 5 -e htop'
yetimic='alsa_in -j "Yeti" -d hw:Microphone -q 1 2>&1 1> /dev/null &'

# program launcher
def launch(program):
    try:
        subprocess.Popen(program, start_new_session=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print('Launching '+program)
    except:
        print('Cannot launch '+program)
    #if multiple == True:
        #runprocess
    #else:
        #process.wait()
        #for p in psutil.process_iter():
            #if (program in p.name()) and (p.status() != psutil.STATUS_ZOMBIE):
                #print (program + ' is already running')
        #else:
           #runprocess

#signal.signal(signal.SIGINT, signal_handler)
try:
  for event in dev.read_loop():
    if event.type == e.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            #
            # Spacebar
            #
            if key.keycode == 'KEY_SPACE':
                subprocess.call('xdotool key Super_L+space'.split())
            #
            # ESC-F1-F12    
            #
            if key.keycode == 'KEY_ESC':
                subprocess.call('xdotool key Super_L+f'.split())
                print('Toggle full screen')
            if key.keycode == 'KEY_BRIGHTNESSDOWN':
                subprocess.call('xdotool key Super_L+1'.split())
                print('Switch to workspace 1')
            if key.keycode == 'KEY_BRIGHTNESSUP':
                subprocess.call('xdotool key Super_L+2'.split())
                print('Switch to workspace 2')
            if key.keycode == 'KEY_SCALE':
                subprocess.call('xdotool key Super_L+3'.split())
                print('Switch to workspace 3')
            if key.keycode == 'KEY_DASHBOARD':
                subprocess.call('xdotool key Super_L+4'.split())
                print('Switch to workspace 4')
            if key.keycode == 'KEY_KBDILLUMDOWN':
                subprocess.call('xdotool key Super_L+5'.split())
                print('Switch to workspace 5')
            if key.keycode == 'KEY_KBDILLUMUP':
                subprocess.call('xdotool key Super_L+6'.split())
                print('Switch to workspace 6')
            if key.keycode == 'KEY_PREVIOUSSONG':
                subprocess.call('xdotool key Super_L+7'.split())
                print('Switch to workspace 7')
            if key.keycode == 'KEY_PLAYPAUSE':
                subprocess.call('xdotool key Super_L+8'.split())
                print('Switch to workspace 8')
            if key.keycode == 'KEY_NEXTSONG':
                subprocess.call('xdotool key Super_L+9'.split())
                print('Switch to workspace 9')
            if key.scancode == 113: # Mute Key has 2 keycodes
                subprocess.call('xdotool key Super_L+0'.split())
                print('Switch to workspace 0')
            if key.keycode == 'KEY_VOLUMEDOWN':
                subprocess.call('xdotool key Super_L+o'.split())
                print('Switch to previous workspace')
            if key.keycode == 'KEY_VOLUMEUP':
                subprocess.call('xdotool key Super_L+p'.split())
                print('Switch to next workspace')
            #
            # F13-F15
            #
            if key.keycode == 'KEY_F13':
                subprocess.call('xdotool key Super_L+Shift_L+space'.split())
                print('Toggle floating window')
            if key.keycode == 'KEY_F14':
                subprocess.call('xdotool key Super_L+Alt_Lspace'.split())
                print('Toggle focus tiling / floating')
            if key.keycode == 'KEY_F15':
                subprocess.call('xdotool key Super_L+Shift_L+x'.split())

            #
            # 1 .. 0
            #
            if key.keycode == 'KEY_1':
                subprocess.call('xdotool key Alt_L+Shift_L+1'.split())
                print('Switch to scene 1')
            if key.keycode == 'KEY_2':
                subprocess.call('xdotool key Alt_L+Shift_L+2'.split())
                print('Switch to scene 2')
            if key.keycode == 'KEY_3':
                subprocess.call('xdotool key Alt_L+Shift_L+3'.split())
                print('Switch to scene 3')
            if key.keycode == 'KEY_4':
                subprocess.call('xdotool key Alt_L+Shift_L+4'.split())
                print('Switch to scene 4')
            if key.keycode == 'KEY_5':
                subprocess.call('xdotool key Alt_L+Shift_L+5'.split())
                print('Switch to scene 5')
            if key.keycode == 'KEY_6':
                subprocess.call('xdotool key Alt_L+Shift_L+6'.split())
                print('Switch to scene 6')
            if key.keycode == 'KEY_7':
                subprocess.call('xdotool key Alt_L+Shift_L+7'.split())
                print('Switch to scene 7')
            if key.keycode == 'KEY_8':
                subprocess.call('xdotool key Alt_L+Shift_L+8'.split())
                print('Switch to scene 8')
            if key.keycode == 'KEY_9':
                subprocess.call('xdotool key Alt_L+Shift_L+9'.split())
                print('Switch to scene 9')
            if key.keycode == 'KEY_0':
                subprocess.call('xdotool key Alt_L+Shift_L+0'.split())
                print('Switch to scene 0')
            #
            # QWERTY...
            #
            if key.keycode == 'KEY_Q':
                msg = mido.Message("note_on", note=36, velocity=100, time=10)
                msg.copy(channel=1)
            #
            # PAGE UP DOWN
            #

            #
            # KEYPAD
            #
            if key.keycode == 'KEY_F16':
                subprocess.call('xdotool key Super_L+v'.split())
                print('Split vertically')
            if key.keycode == 'KEY_F17':
                subprocess.call('xdotool key Super_L+h'.split())
                print('Split horizontally')
            if key.keycode == 'KEY_F18':
                subprocess.call('xdotool key Super_L+q'.split())
            if key.keycode == 'KEY_F19':
                launch('xkill')
            if key.keycode == 'KEY_NUMLOCK':
                os.system(loopcam)
                print('Loopcam device on /dev/video9')
            if key.keycode == 'KEY_KPEQUAL':
                os.system(cable)
            if key.keycode == 'KEY_KPSLASH':
                os.system(yetimic)
            if key.keycode == 'KEY_KPASTERISK':
                os.system(htop) ## block keyboard
            if key.keycode == 'KEY_KPDOT':
                os.system(online)
            if key.keycode == 'KEY_KP9':
                os.system(loopcam)
            if key.keycode == 'KEY_KP7':
                launch('carla')
                subprocess.call('xdotool key Super_L+4'.split())
            if key.keycode == 'KEY_KP8':
                launch('obs')
                subprocess.call('xdotool key Super_L+5'.split())
            if key.keycode == 'KEY_KP9':
                launch('zoom')
                subprocess.call('xdotool key Super_L+7'.split())
            if key.keycode == 'KEY_KP3':
                launch('lightworks')
                subprocess.call('xdotool key Super_L+0'.split())
            if key.keycode == 'KEY_KP1':
                launch('inkscape')
            if key.keycode == 'KEY_KP2':
                launch('blender')
                subprocess.call('xdotool key Super_L+6'.split())
            if key.keycode == 'KEY_KP4':
                launch('firefox')
                subprocess.call('xdotool key Super_L+2'.split())
            if key.keycode == 'KEY_KP5':
                launch('thunderbird')
            if key.keycode == 'KEY_KP6':
                launch('thunar')
                subprocess.call('xdotool key Super_L+3'.split())
            if key.keycode == 'KEY_KPPLUS':
                launch('franz')
            if key.keycode == 'KEY_KPMINUS':
                subprocess.call('xdotool key Super_L+Return'.split())
                print('Open Terminal window')
            #
            # ARROW KEYS
            #
            if key.keycode == 'KEY_LEFT':
                subprocess.call('xdotool key Super_L+Left'.split())
            if key.keycode == 'KEY_RIGHT':
                subprocess.call('xdotool key Super_L+Right'.split())
            if key.keycode == 'KEY_UP':
                subprocess.call('xdotool key Super_L+Up'.split())
            if key.keycode == 'KEY_DOWN':
                subprocess.call('xdotool key Super_L+Down'.split())
except:
  print('Keyboard disconnected')
  notify2.Notification("Deck stopped","Apple keyboard disconnected").show()
  exit()
