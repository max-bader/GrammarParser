# project4.py
#
# ICS 33 Spring 2024
# Project 4: Still Looking for Something
from grammar import parse_grammar

def main() -> None:
    grammar_file = input()
    sentences = int(input())
    start_var = input()

    grammar = parse_grammar(grammar_file)
    for _ in range(sentences):
        print(grammar.generate(start_var))


if __name__ == '__main__':
    main()
