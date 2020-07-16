# TODO: Write a code that will play an audio file when a key is pressed.  ! done
# * C++ issue has been resolved. Continue searching for appropriate library to play audio file.

# for keyboard input detection and threading
import keyboard as kb
import threading

# For audio playback
from playsound import playsound

# For directory of the script being run
import os  
CURENT_PATH = os.getcwd()


filename = 'starwars_slowdown.mp3'
print(f'{CURENT_PATH}/{filename}\n')
playsound(f'{CURENT_PATH}/{filename}')