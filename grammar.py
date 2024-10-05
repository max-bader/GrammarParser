from grammar_design import Grammar, Variable, Terminal, Option


def parse_grammar(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    grammar = Grammar()
    rule = None
    variable = None

    for line in lines:
        line = line.strip()

        if not line:
            continue
        if line == "{":
            rule = []
        elif line == "}":
            if variable and rule is not None:
                grammar.add(variable, rule)
                variable = None
        elif rule is not None:
            if variable is None:
                variable = line
            else:
                line_parts = line.split()
                probability = int(line_parts[0])
                symbols = line_parts[1:]

                symbol_objects = []
                for symbol in symbols:
                    if symbol.startswith('[') and symbol.endswith(']'):
                        symbol_objects.append(Variable(symbol[1:-1]))
                    else:
                        symbol_objects.append(Terminal(symbol))

                rule.append(Option(probability, symbol_objects))

    return grammar
