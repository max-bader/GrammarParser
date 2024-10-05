# Module that holds all the classes needed to help design a combination
# of objects to represent a grammar.
import random


class Terminal:
    def __init__(self, value):
        self.value = value

    def generate(self, grammar):
        return self.value


class Rule:
    def __init__(self, variable, options):
        self.variable = variable
        self.options = options

    def generate(self, grammar):
        probability = 0
        for option in self.options:
            probability += option.prob

        choice = random.randint(1, probability)
        current_prob = 0

        for option in self.options:
            current_prob += option.prob
            if choice <= current_prob:
                return option.generate(grammar)


class Grammar:
    def __init__(self):
        self.rules = {}

    def add(self, variable, options):
        self.rules[variable] = Rule(variable, options)

    def generate(self, start_variable):
        rule = self.rules[start_variable]
        result = rule.generate(self)
        return result


class Variable:
    def __init__(self, name):
        self.name = name

    def generate(self, grammar):
        rule = grammar.rules[self.name]
        return rule.generate(grammar)


class Option:
    def __init__(self, prob, symbols):
        self.prob = prob
        self.symbols = symbols

    def generate(self, grammar):
        result = []
        for symbol in self.symbols:
            result.append(symbol.generate(grammar))

        return ' '.join(result)
