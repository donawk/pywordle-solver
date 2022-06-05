# pywordle-solver
Code to solve wordle games, through word suggestions and tracking possible answers.

## Limitation
The Dictionary in use, [english_words](https://pypi.org/project/english-words/), although sufficient is not as extensive or wholly similar to dictionaries used in other popular implementations of the wordle game. Make a pull request if you have a more comprehensive dictionary source available to you, or if you have one more suited to the popular wordle implementations.

## Setup
To start, install [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) initially, and then run `pip install english_words` before running the program.

## Usage
The code provides queries to understand the current state of the game. Provide responses (or leave blank in case no new useful data) to update the code's understanding of what the hidden word may be. 

In queries about the format, input the response as `*_*__`, where `*` represents a character and `_` a blank space. Remaining blank space may be left if useful data is only in the first four or less character spaces (eg. `*_*`). 

In queries about tested letters, list as many letters as desired consequetively, without a separator.

## Implementaiton Details
Code uses details in the form of what's known about character spaces and tried letter to narrow down possible solutions. As per the game rules, letters in certain character spaces either display as correct or wrong. And tried letters may display as either present in the word or not.

As for word suggestions, the solver aims to reduce the total number of possible words, for more likely guesses in the future. It tallies the character occurences for each character and leans towards words with the most character occurences (for example: in the first character space **_** _ _ _ _ 'c' may occur twice while 'g' occurs only once. So words beginning with 'c' have a higher score and this occurs for the following space). As most wordle implementations (including my own) don't _seemigly_ rely on a word's usage outside the game, no reason to account for that.
