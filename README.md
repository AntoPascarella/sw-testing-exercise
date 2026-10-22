# Software Testing Exercise: Hangman

Class exercise from the Software Testing course. We got a compiled, buggy Hangman program and had **1 hour to find as many bugs as possible**.

## Files

- `hangman_buggy_2`: the compiled buggy Hangman executable (macOS binary). Source code is not available, so it can only be tested as a black box.
- `hangman_donghi.py`: the test suite. It starts the executable as a subprocess, sends input and checks the output.

## Test suite

Tests are grouped in three areas:

1. Secret word validation (length, lowercase only, no digits, output format)
2. Letter and word guesses (input errors, revealing letters, wrong guesses)
3. Win/lose conditions (winning, losing after 5 mistakes, game stops at the end)

## Usage

```
python3 hangman_donghi.py
```

Each test prints `PASS` or `FAIL` (with the actual output). A `FAIL` points to a bug in the executable.

Note: the `APP` path at the top of `hangman_donghi.py` is hardcoded. Change it to the location of `hangman_buggy_2` on your machine.
