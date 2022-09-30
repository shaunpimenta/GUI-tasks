try:
    def longest_words(f):
        with open(f, 'r') as infile:
            words = infile.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len]
    print(longest_words('test.txt'))
except:
    print('No such file!')