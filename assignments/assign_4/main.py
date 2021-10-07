import random
random.seed()

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        response = input('Do you want to play again? ==>').lower()
        if response in ['y', 'yes']:
            return True
        if response in ['n', 'no']:
            return False
        print('You must enter Y/Yes/N/No to continue. Please try again')

def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        try:
            wager = int(input('How many chips do you want to wager? ==>'))
        except:
            print('please enter an integer')
            continue
        if 0 < wager <= bank:
            return wager
        elif wager > bank:
            print(f'The wager amount cannot be greater than how much you have. {bank}')
        elif wager < 0:
            print('The wager amount must be greater than 0. Please enter again.')


def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reela = random.randint(1, 10)
    reelb = random.randint(1, 10)
    reelc = random.randint(1, 10)
    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reelb == reelc:
        return 3
    elif reela == reelb or reelb == reelc or reelc == reela:
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        try:
            bank = int(input('How many chips do you want to start with? ==>'))
        except:
            print('please enter an integer')
            continue
        if 0 < bank <= 100:
            return bank
        elif bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
        elif bank <= 0:
            print('Too low a value, you can only choose 1 - 100 chips')

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

        print('You lost all', 0, 'in', 0, 'spins')
        print(f'The most chips you had was, {bank}')
        playing = play_again()
