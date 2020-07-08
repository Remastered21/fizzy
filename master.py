# TODO: Write a code that will wait for user input on keyboard. Create response for each keystroke.
# NOTE: I need to create a way to exit out of the infinite loop of waiting for keystroke, other than ctrl+c.

import keyboard 
import threading
import time

def key_struck():
    keyboard.wait('esc')
    print('esc pressed.')

def waiting_for_key():
    # Starting the thread
    thread = threading.Thread(target=key_struck)
    thread.start()

    # Wait for Esc key to terminate program
    thread.join()
    print('Terminated successfully.')

waiting_for_key()