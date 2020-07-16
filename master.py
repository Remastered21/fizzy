# TODO: Write a code that will wait for user input on keyboard. Create response for each keystroke. ! done
# NOTE: I need to create a way to exit out of the infinite loop of waiting for keystroke, other than ctrl+c. 

# TODO: Create an audio player.

import keyboard as kb
import threading

def key_struck():
    kb.wait('esc')
    print('Esc pressed.\n')

def waiting_for_key():
    # Starting the thread
    thread = threading.Thread(target=key_struck)
    thread.start()

    # Monitor keystroke
    kb.add_hotkey(' ', print, args=['space was pressed'])
    
    # Wait for Esc key to terminate program
    thread.join()
    print('Terminated successfully.')

waiting_for_key()