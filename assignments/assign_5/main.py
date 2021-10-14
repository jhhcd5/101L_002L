from typing import Tuple

def get_school(library_card: str) -> str:
    school = library_card[5]
    if school == '1':
        return 'School of Computing and Engineering SCE'
    elif school == '2':
        return 'School of Law'
    elif school == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'

def get_grade(library_card: str) -> str:
    grade = library_card[6]
    if grade == '1':
        return 'Freshman'
    elif grade == '2':
        return 'Sophomore'
    elif grade == '3':
        return 'Junior'
    elif grade == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'

def character_value(character: str) -> int:
    return ord(character) - ord('A')

def get_check_digit(library_card: str) -> int:
    sum =0
    for index, character in enumerate(library_card[:9]):
        if index < 5:
            sum += (index + 1) * character_value(character)
        else:
            sum += (index + 1) * (ord(character) - ord('0'))
    return sum % 10


def verify_check_digit(library_card: str) -> Tuple[bool, str]:
    if len(library_card) != 10:
        return False, 'The length of the number given must be 10'
    for index, character in enumerate(library_card[:5]):
        if ord(character) < ord('A') or ord('Z') < ord(character):
            return False, f'The first five characters must be A-Z, the invalid character is at {index} is {character}'
    for index, character in enumerate(library_card[7:10]):
        if ord(character) < ord('0') or ord('9') < ord(character):
            return False, f'The first five characters must be 0-9, the invalid character is at {index} is {character}'
    if library_card[5] not in ['1', '2', '3']:
        return False, ' The sixth character must be 1, 2, or 3'
    if library_card[6] not in ['1', '2', '3', '4']:
        return False, ' The seventh character must be 1, 2, 3, or 4'
    check_digit = get_check_digit(library_card)
    if check_digit == library_card[-1]:
        return False, f'Check digit {library_card[-1]}, does not match calculated value {check_digit}'
    else:
        return True, 'Library card is valid'


if __name__ == "__main__":
    print('                         Linda Hall                         ')
    print('                     Library Card Check                     ')
    print('============================================================')

    library_card = input('Enter library card. Hit enter to exit ==>')

















