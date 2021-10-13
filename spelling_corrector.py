import re
import numpy as np


with open("english_words_list.txt") as v:
    text = v.read()
    # To separate the 10,000 word list into separate strings
    # Note: can replace this txt with better list for better results
    words = text.splitlines()

with open("random_text.txt") as b:
    # Note: can replace this txt with your own corrupted text
    book = b.read()

    # To find all the 'words' in my text using all alphanumerics (without "_")
    pattern = r"[^\W_]+"
    strings = re.findall(pattern, book)

    # To find all the non-words in my text to stitch my output together later (including "_")
    splitpattern = r"[\W_]+"
    punctuation = re.findall(splitpattern, book)


def levenshtein(source: str, target: str):
    """Takes two words and calculates Levenshtein's distance between them"""
    n = len(source)
    m = len(target)
    min_distance = np.zeros((n + 1, m + 1))
    # Initialize the zeroth row and column is the distance from the empty string.
    for i in range(1, n + 1):
        min_distance[i, 0] = min_distance[i - 1, 0] + 1  # 1 for deletion cost
    for j in range(1, m + 1):
        min_distance[0, j] = min_distance[0, j - 1] + 1  # 1 for insertion cost

    # Reccurence relation:
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if source[i - 1] == target[j - 1]:
                subcost = 0
            else:
                subcost = 2
            min_distance[i, j] = min(
                min_distance[i - 1, j] + 1,
                min_distance[i - 1, j - 1] + subcost,
                min_distance[i, j - 1] + 1,
            )

    return min_distance[n, m]


def getbest(corrupt: str):
    """Takes a corrupt word and uses Levenshtein's distance to find the closest word in word list"""
    was_title = corrupt.istitle()
    was_upper = corrupt.isupper()

    lower_corrupt = corrupt.lower()

    current_best = (levenshtein(lower_corrupt, words[0]), words[0])

    for _, w in enumerate(words):
        candidate = (levenshtein(lower_corrupt, w), w)
        if current_best[0] > candidate[0]:
            current_best = candidate

    if was_title:
        current_best = (current_best[0], current_best[1].title())
    if was_upper:
        current_best = (current_best[0], current_best[1].upper())

    return current_best


output = []
for s in strings:
    # To not make changes to a word if it already exists in our word list
    if s in words:
        output.append(s)
    # To check for numbers and leave them as is
    elif s.isdigit():
        output.append(s)
    # To not make changes to a word if the Levenshtein distance is too large
    # Note: the definition of too large is arbitrarily determined to be half of the word length + 2
    # To take into account short words
    elif getbest(s)[0] > len(s) // 2 + 1:
        output.append(s)
    # Update words using our word list
    else:
        output.append(getbest(s)[1])


result = []
# To account for cases text inputs begin or end with punctuations
if book[0] in punctuation and book[-1] in punctuation:
    output.append("")
    for n in range(len(punctuation)):
        result.append(punctuation[n])
        result.append(output[n])
else:
    if len(strings) > len(punctuation):
        punctuation.append("")

    for m in range(len(strings)):
        result.append(output[m])
        result.append(punctuation[m])

final = "".join(result)
print(final)
