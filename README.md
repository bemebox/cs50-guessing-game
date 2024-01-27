# CS50 Guessing Game Solution
CS50’s Introduction to Programming with Python Guessing Game problem solution.

This program was developed according with Python's good practices and based on [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

### Version
1.0.0


## Resources
* [CS50 Guessing Game Problem](https://cs50.harvard.edu/python/2022/psets/4/game/)
* [random module](https://docs.python.org/3/library/random.html)


## Getting Started

These instructions will guide you to copy the project from the repository and run it.

### Prerequisites

Things you need to have installed:
* [Python](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

### Local Installation

Basically clone the project from the remote repository to the local machine, using the git commands.

```
$git clone [URL].git
```

### Run
To run the project run the python command.
```
$python game.py
```

### Test
To guess the generated random number, add a positive integer number to set the Level (max random number to be generated):
```
$python game.py
$Level: 1
```
Then write the positive integer number you think it was random generated:
```
$python game.py
$Level: 1
$Guess: 1
```
The output it will be ```Just right!```, if the user guess is the same as generated integer number, and end the program./
The output it will be ```Too small!```, if the user guess is smaller than the generated integer number, and prompt the user again./
The output it will be ```Too large!```, if the user guess is larger than the generated integer number, and prompt the user again./


## Authors

* **BEOM &copy; 2024**
