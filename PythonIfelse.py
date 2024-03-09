x = int(input("Please enter an integer: "))

# An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.
# ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation and looping

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')