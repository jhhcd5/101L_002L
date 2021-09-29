print('Welcome to the Flarsheim guesser!')
print()
print('Please think of a number between and including 1 and 100.')
def get_mod(base):
    mod = None
    while True:
        mod = int(input(f'What is the remainder when your number is divided by {base} ?'))
        if mod < 0:
            print('The value entered must be 0 or greater')
            continue
        if mod >= base:
            print(f'The value entered must be less than {base}')
            continue
        return mod
play_again = True
while play_again:
    mod3 = get_mod(3)
    mod5 = get_mod(5)
    mod7 = get_mod(7)

    print(f'{mod3 = }, {mod5= }, {mod7 =}')
    for i in range(1,101):
        if (i % 3 == mod3) and (i % 5 == mod5) and (i % 7 == mod7):
            print(f'Your number was {i}')
            break
    print('How amazing is that')
    while True:
        play_again = input('Do you want to play again? Y to continue, N to quit ==>').lower()
        if play_again == 'y':
            play_again = True
            break
        if play_again == 'n':
            play_again = False
            break
