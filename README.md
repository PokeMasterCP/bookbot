# BookBot

A small command-line tool that reads a plain-text book and reports how many
words it contains and how often each letter appears, sorted from most to least
common.

This was my first [boot.dev](https://www.boot.dev) project.

## Requirements

Python 3 — no third-party packages.

## Usage

```sh
python3 main.py books/frankenstein.txt
```

Three public-domain books are included in `books/` to try it on:
`frankenstein.txt`, `mobydick.txt`, and `prideandprejudice.txt`.

## Example output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
---------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
```

## How it works

The text is split on whitespace to count words. For the letter counts, every
character is lowercased and tallied into a dictionary, which is then converted
to a list of `{"char": ..., "num": ...}` entries and sorted by count in
descending order. Non-alphabetic characters are counted but filtered out at
print time, so punctuation and digits don't clutter the report.

## Project layout

```
main.py    argument handling, file reading, and output formatting
stats.py   the counting and sorting functions
books/     sample public-domain texts
```
