import time, sys
indent = 0 # how many spaces to indent
indentIncreasing = True # whether the indentation is/n't increasing

try:
    while True: # main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause for 1/10th of a second

        if indentIncreasing: # increase the number of spaces:
            indent = indent + 1
            if indent == 20: # change direction:
                indentIncreasing = False

        else: # decrease number of spaces
            indent = indent - 1
            if indent == 0: # change direction:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit() 
