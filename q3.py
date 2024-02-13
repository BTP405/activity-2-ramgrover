def wordCount(t):
    wordDictionary = {}#This line initializes an empty dictionary called wordDictionary. This dictionary will store words as keys and corresponding line numbers as values.
    with open(t, 'r') as file:#This line opens the file in read mode. with statement states that file is successfully closed after reading.
        for lineNum, line in enumerate(file, 1):#The enumerate function starts counting line numbers from 1.
            words = line.split()#This line splits the current line into a list of words using the split() method. By default, it splits the line based on spaces.
            for word in words:
                if word in wordDictionary:
                    wordDictionary[word].append(lineNum)
                else:
                    wordDictionary[word] = [lineNum]
    return wordDictionary

file_path = 'q3.txt'
result = wordCount(file_path)

# Print the result
for word, lineNumbers in result.items():
    print(f"{word}: {lineNumbers}")
