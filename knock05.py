def n_gram(content, n):
    for i in range(len(content) - n + 1):
        result = ""
        for j in range(n):
            result += content[i + j]
        yield result


string = "I am an NLPer"

letter_bi_gram = []
for i in n_gram(string, 2):
    letter_bi_gram.append(i)

list = [i + " " for i in string.split(" ")]
word_bi_gram = []
for i in n_gram(list, 2):
    word_bi_gram.append(i)

print(letter_bi_gram)
print(word_bi_gram)
