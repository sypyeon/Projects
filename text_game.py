#New project for text game

name = input('\"Welcome to the Grindel, the world of adventure!\"\n\"What is your name?\"\nName :')
confirm_name = input(f'\"Is your name {name}?\"')
while confirm_name != 'yes':
    name = input('\"Tell me what your name is\"')
    confirm_name = input(f'\"Is your name {name}?\"')


gender = input(f'\"Great! Your name is {name}! And... I suppose you are...\"\n Gender :')

