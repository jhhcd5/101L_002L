import csv


def month_from_number(n):
    calendar = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    return calendar[str(n)]


def read_in_file(fname):
    data = []
    try:
        f = open(fname, 'r', encoding='UTF-8')
    except:
        return -1
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
    f.close()
    return data


def create_dict_column(data, name):
    dict_ex = {}
    n = data[0].index(name)
    for sub in data[1:]:
        if sub[n] in dict_ex:
            dict_ex[sub[n]] += 1
        else:
            dict_ex[sub[n]] = 1
    return dict_ex


def create_reported_date_dict(data):
    dict_t = {}
    for i, entry in enumerate(data):
        if i == 0:
            continue
        if not entry[1] in dict_t:
            dict_t[entry[1]] = 1
        else:
            dict_t[entry[1]] += 1
    return dict_t


def create_offense_dict(data):
    dict_t = {}
    for i, entry in enumerate(data):
        if i == 0:
            continue
        if not entry[7] in dict_t:
            dict_t[entry[7]] = 1
        else:
            dict_t[entry[7]] += 1
    return dict_t


def create_reported_month_dict(data):
    dict_t = {}
    for i, entry in enumerate(data):
        if i == 0:
            continue
        date = entry[1]
        month = int(date[:2])
        if not month in dict_t:
            dict_t[month] = 1
        else:
            dict_t[month] += 1
    return dict_t


def create_offense_by_zip(data):
    dict_t = {}
    for i, entry in enumerate(data):
        if i == 0:
            continue
        offense = entry[7]
        zip = entry[13]
        if not offense in dict_t:
            dict_t[offense] = {}
            dict_t[offense][zip] = 1
        else:
            if not zip in dict_t[offense]:
                dict_t[offense][zip] = 1
            else:
                dict_t[offense][zip] += 1

    return dict_t

def main():
    fileName = input('Enter the name of the crime data file ==> ')
    data = read_in_file(fileName)
    while (data == -1):
        print('Could not find the file specified. not exists not found')
        fileName = input('Enter the name of the crime data file ==> ')
        data = read_in_file(fileName)


    month_dict = create_reported_month_dict(data)
    numCrimes = 0
    monthCrimes = 0
    for key, value in month_dict.items():
        if value > numCrimes:
            numCrimes = value
            monthCrimes = key
    print()
    strMonth = month_from_number(monthCrimes)
    print('The month with the highest # of crime is', strMonth, 'with', numCrimes, 'offenses')


    offense_dict = create_offense_dict(data)
    numOffense = 0
    offense = ''
    for key, value in offense_dict.items():
        if value > numOffense:
            numOffense = value
            offense = key

    print('The offense with the highest # of crimes is', offense, 'with', numOffense, 'offenses')
    print()

    nameOffense = input('Enter an offense: ')
    while not nameOffense in offense_dict:
        print('Not a valid offense found, please try again')
        nameOffense = input('Enter an offense: ')

    
    offenseZip = create_offense_by_zip(data)
    print(nameOffense, 'offenses by Zip Code')
    print('{:<10}{:>10}'.format('Zip code', '# Offenses'))
    print("=========================")
    dict_t = offenseZip[nameOffense]
    for zip, value in dict_t.items():
        print('{:<10}{:>10}'.format(zip, value))




if __name__ == "__main__":
    main()