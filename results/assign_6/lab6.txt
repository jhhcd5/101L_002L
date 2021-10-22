##Brian Hare
##hareb@umkc.edu
##CS 101
##Program 4
##
##PROBLEM: Do Caesar Encryption/Decryption, including cracking a string w/
##  unknown Caesar key.
##
##Functions needed:
##  Encrypt(string_text, int_key): Takes a string and integer key, returns
##  the encryption of the string using that key. Note that for Caesar encryption,
##  an encryption with key k (k in 1 - 25) is decrypted by doing the same process
##  with key 26-k. Returns encrypted string using specified key.
##
##  Decrypt(string_text, int_key): Decrypts key by calling Encrypt with key
##    26-int_key and returning the result. Done this way to make for a cleaner
##    breakdown of the problem. Returns decrypted string using specified key.
##
##  Crack(string_text): Decrypts a string by repeatedly calling Decrypt with each
##    possible key (1 to 25) and remembering the one with a letter frequency
##    closest to English based on counts of E, T, O, A, I, N. Returns tuple:
##    decrypted string and decryption key.
##
##  Get_input(): Interacts with user, gets user choice of '1'-'4' and returns that
##  value. If user enters anything else, prints brief error message and tries again.
##
##  Print_menu(): Prints menu. No user interaction.

################################
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase


def encrypt_uppercase_character(character, key):
    ch_value = upper.find(character)
    new_index = (ch_value + key) % 26
    return upper[new_index]


def encrypt_lowercase_character(character, key):
    ch_value = lower.find(character)
    new_index = (ch_value + key) % 26
    return lower[new_index]


def decrypt_uppercase_character(character, key):
    ch_value = upper.find(character)
    new_index = (ch_value - key) % 26
    return upper[new_index]


def decrypt_lowercase_character(character, key):
    ch_value = lower.find(character)
    new_index = (ch_value - key) % 26
    return lower[new_index]


def Encrypt(string_text, key) -> str:
    '''Caesar-encrypts string using specified key.'''
    result = ''
    for character in string_text:
        if character in upper:
            encrypted_character = encrypt_uppercase_character(character, key)
        elif character in lower:
            encrypted_character = encrypt_lowercase_character(character, key)
        else:
            encrypted_character = character

        result += encrypted_character
    return result


def Decrypt(string_text, key) -> str:
    ''' Decrypts Caesar-encrypted string with specified key. '''
    result = ''
    for character in string_text:
        if character in upper:
            decrypted_character = decrypt_uppercase_character(character, key)
        elif character in lower:
            decrypted_character = decrypt_lowercase_character(character, key)
        else:
            decrypted_character = character

        result += decrypted_character
    return result


def Get_input(encrypt, decrypt, quit) -> str:
    '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
    selection = input('Enter your selection ==>')
    for value in selection:
        if selection == 1:
            return encrypt
        elif selection == 2:
            return decrypt
        elif selection == 3:
            return quit
        else:
            return 'invalid selection, please submit again'

def Print_menu(selection):
    '''Prints menu. No user interaction. '''
    print('MAIN MENU: ')
    print('1) Encode a sting')
    print('2) Decode a string')
    print('Q) Quit')
    print('Enter your selection ==>', selection)

def main():



    main()
