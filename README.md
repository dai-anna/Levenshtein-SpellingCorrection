# SpellingCorrector
NLP project to leverage Levenshtein distance to spell correct text in a corpus. Tokenization and de-tokenization uses RegEx

## Simple Setup

`make install` to install the only package we need: Numpy.

## How it Works
`random_text.txt` contains the corrupted body of text as a single string.

`english_words_list.txt` contains a list of words to use as a dictionary to correct to. The list I am using contains 10,000 frequently used words in descending order of frequency.

`spelling_corrector.py`uses Levenshtein distance to correct spellings of words in `random_text.txt`.


## In Action

**Corrupt text:**
![Screen Shot 2021-10-13 at 12 13 19 AM](https://user-images.githubusercontent.com/89488845/137066137-f4440226-e7c4-4aef-bae0-e8b027123994.png)
**Corrected text:**
![Screen Shot 2021-10-13 at 12 09 26 AM](https://user-images.githubusercontent.com/89488845/137065855-75b3562f-e39b-4e55-b364-2706cc38cf4d.png)
