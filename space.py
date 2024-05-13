print('press ENTER key to proceed')

input('???- Wa.. u...')
input('???- Wake... p..')
input('???- Wake up!')
input('???- You finally woke up! I was worried about you.')
input('SyD- Hi this is SyD. I am a program designed to help the crews to navigate this space ship safely.')
input('SyD- I actually cannot contect any other sector... I assume that there is some kind of malfunction happening.')

#Set player's name here
name = input('SyD- Let me ask a question. Who am I speaking to?\nName: ')
while name == '':
    name = input('SyD- Please tell me your name.\nName: ')

#Confirm player's name
confirm_name = input(f'SyD- Is your name {name}?')
while confirm_name != 'yes':
    name = input('SyD- Tell me what your name is\nName: ')
    confirm_name = input(f'\"Is your name {name}?\"')

input(f'SyD- Great {name}! Remembering your name after waking up from the hibernation chamber is a good sign.')
input(f'SyD- ')