punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
word_counts = dict()

while True:
    file_name = input('Enter the name of the file to open ')
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
        break

    except:
        print('Could not open file ', file_name)
        print('Please Try again')

for line in lines:
    for x in line:
        if x in punctuations:
            line = line.replace(x, '')

    words = line.lower().split()

    for word in words:

        if len(word) > 3:

            if word not in word_counts.keys():
                word_counts[word] = 1
            else:
                word_counts[word] += 1

sorted_freq = sorted(word_counts, key=word_counts.get, reverse=True)
print('{:<6}{:>15}{:>15}'.format("#", "Word", "Freq."))
print("========================================")
count = 1
for key in sorted_freq:
    print('{:<6}{:>15}{:>15}'.format(count , key, word_counts[key]))
    count += 1

word_occur_once = 0
for key in word_counts:
    if word_counts[key] == 1:
        word_occur_once += 1

print('There are', word_occur_once, 'words that occur only once')
print('There are', len(word_counts), 'unique words in the document')
