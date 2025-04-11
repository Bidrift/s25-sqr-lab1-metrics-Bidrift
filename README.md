# Hangman Game

Python console app hangman game based on the [code](https://github.com/markpatterson27/hangman-game) by [Mark Patterson](https://github.com/markpatterson27)

## Install dependencies and run

1. `pip install poetry`
2. `poetry install`
3. `poetry run python app/hangman.py`

# Lab "Static analysis and Metrics" Assignment

### Important instructions
1. do not move/delete the source files from the folders
1. you may refactor functions, but you **must** keep the signatures of the all original functions (e.g. _hangman()_, _splash_screen()_, _get_random_word()_)
1. the orginal functionality **must** remain
1. Submission: _commit_ and _push_ your changes to the current project to GitHub
1. do not edit _autograding_ or _classroom_ files
> :warning: **Note:** the autograding is simplified on purpose, it will be overwritten after the submission deadline with additional tests

> :warning: **Note:** if you add tests, all tests should pass for final submission

## Style check

1. Install _flake8_
1. Analyse the `app/hangman.py`
1. Correct all errors
1. All default _flake8_ checks **must pass**
1. Add _flake8_ check to the GitHub CI as an action to `.github/workflows/main.yaml`

> :warning: **Note:** all the source code files in the project must pass the the default flake8 check.

## Complexity analysis
Cyclomatic complexity is a part of maintainability index. The recommended complexity for functions is 10.

1. Analyse complexity of `app/hangman.py`, 
1. Refactor as needed.
1. Add complexity threashold check (i.e. 10 for max complexity) to GitHub CI as an action to `.github/workflows/main.yaml`

> :warning: **Note:** autograding will check the complexity of all the source code files **after** the submission deadline in postprocessing.

# Hints
* Check the [code quality tutorial](https://testdriven.io/blog/python-code-quality/)
* Flake rules https://www.flake8rules.com/
