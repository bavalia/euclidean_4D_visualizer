#!/usr/bin/python3
'''
Only supports character passing, 
Not Supported Keys: Esc, Shift, Ctrl, Alt, Win, PrntScr, Caps 
'''

def getChar():
    try:
        # for Windows-based systems
        import msvcrt # If successful, we are on Windows
        return msvcrt.getch()

    except ImportError:
        # for POSIX-based systems (with termios & tty support)
        import tty, sys, termios  # raises ImportError if unsupported

        fd = sys.stdin.fileno()
        oldSettings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            answer = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

        #print ('hex:'+format(ord(answer),'x'))
        return answer

def getKey():
    key = getChar()
    keyHex = format(ord(key),'x')
    #print ("initial key recieved in hex: "+keyHex)
    if key == '\x1b':
        key2 = getChar()
        if key2 == '[' : 
            key3 = getChar()
            if key3 == 'A' : key = 'up'
            elif key3 == 'B': key = 'down'
            elif key3 == 'C': key = 'right'
            elif key3 == 'D': key = 'left'
            elif key3 == '5': 
                if getChar()=='~': key = 'pgup'
            elif key3 == '6': 
                if getChar()=='~': key = 'pgdn'
            elif key3 == '3': 
                if getChar()=='~': key = 'delete'
            elif key3 == '2': 
                key4 = getChar()
                if key4 == '~': key = 'insert'
                elif key4 == '0':
                    if getChar()=='~': key = 'f9'
                elif key4 == '1':
                    if getChar()=='~': key = 'f10'
                elif key4 == '4':
                    if getChar()=='~': key = 'f12'
            elif key3 == '1':
                key4 = getChar()
                if key4 == '5':
                    if getChar()=='~': key = 'f5'
                elif key4 == '7':
                    if getChar()=='~': key = 'f6'
                elif key4 == '8':
                    if getChar()=='~': key = 'f7'
                elif key4 == '9':
                    if getChar()=='~': key = 'f8'

        elif key2 == 'O': #letter MNO
            key3 = getChar()
            if key3 == 'H': key = 'home'
            elif key3 == 'F': key = 'end'
            elif key3 == 'P': key = 'f1'
            elif key3 == 'Q': key = 'f2'
            elif key3 == 'R': key = 'f3'
            elif key3 == 'S': key = 'f4'

    elif key == '\x0d': key = 'enter'
    elif key == '\x20': key = 'space'
    elif key == '\x00': key = 'NUL'
    elif key == '\x04': key = 'ctrl+d' #EOT, end of transmission #'ctrl+d'
    elif key == '\x03': key = 'ctrl+c' #ETX, end of text #'ctrl+c'
    elif key == '\x09': key = 'tab' #HT #horizontal tab #'\t'
    elif key == '\x20': key = 'space'
    elif key == '\x7f': key = 'backspace'

    return key

# Program starts
if __name__=='__main__':
    for i in range(10): print (getKey())
