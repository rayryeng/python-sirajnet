# SirajNet
Using deep complicated NLP to turn your text into my text by arbitrarily swapping words for their synonyms. /s

# Usage
```
usage: main.py [-h] [--text TEXT] [--chance CHANCE] [--file FILE]

optional arguments:
  -h, --help       show this help message and exit
  --text TEXT      your original text
  --chance CHANCE  one in N swap chance
  --file FILE      path to text file containing text
```

# Examples

## Entering text in the command line
```
$ python3 main.py --chance 1 --text "Hello world, it's siraj!"
howdy world, it's siraj!
```

## Providing a text file
```
$ echo -en "hello world it's siraj and this week i'm\ngoing to show you how Gaussian gates and complex Hilbert\nspaces work. stay cool wizards" > file.txt
$ python3 main.py --chance 1 --file file.txt
how-do-you-do world it's siraj and this week Im
go to show you how Gaussian doors and hard David Hilbert
gaps work. check chill wizards
```

# Requirements
- TextBlob (`pip install textblob`)
- PhD in neural quantum blockchain
- 5 minutes
- extensive knowledge of residual capsule reservoir networks
- stargazing this repository

# If running the first time
To allow the Gaussian doors to shine through, you may need to download the `omw-1.4` corpus that is part of NLTK
which is a dependency of TextBlob.  If not, it will generate many complicated Hilbert space errors that
will show `Resource omw-1.4 not found` messages.  To resolve this, please do the following in your Python
REPL before running:

```
>>> import nltk
>>> nltk.download('omw-1.4')
```
