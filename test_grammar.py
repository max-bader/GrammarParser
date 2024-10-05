import unittest
import os
from grammar_design import Variable
from grammar import parse_grammar



class TestParseGrammar(unittest.TestCase):
    def test_parse_grammar(self):
        grammar_string = """
        {
        GrinStatement
        1 [Label] [UnlabeledGrinStatement]
        5 [UnlabeledGrinStatement]
        }
        {
        UnlabeledGrinStatement
        10 [LetStatement]
        5 [PrintStatement]
        2 [InNumStatement]
        2 [InStrStatement]
        2 [AddStatement]
        2 [SubStatement]
        2 [MultStatement]
        2 [DivStatement]
        5 [GotoStatement]
        5 [GosubStatement]
        5 [ReturnStatement]
        1 [EndStatement]
        }
        {
        Label
        1 A:
        1 B:
        1 C:
        }
        {
        Variable
        1 A
        1 B
        1 C
        }
        {
        LetStatement
        1 LET [Variable] [Value]
        }
        {
        PrintStatement
        1 PRINT [Value]
        }
        """

        temp_file_name = "grammar.txt"

        try:
            with open(temp_file_name, 'w') as temp_file:
                temp_file.write(grammar_string)

            grammar = parse_grammar(temp_file_name)

            self.assertIn("GrinStatement", grammar.rules)
            self.assertIn("UnlabeledGrinStatement", grammar.rules)
            self.assertIn("Label", grammar.rules)
            self.assertIn("LetStatement", grammar.rules)
            self.assertIn("PrintStatement", grammar.rules)

            grin_statement_rule = grammar.rules["GrinStatement"]
            self.assertEqual(len(grin_statement_rule.options), 2)

            unlabeled_grin_statement_rule = grammar.rules["UnlabeledGrinStatement"]
            self.assertEqual(len(unlabeled_grin_statement_rule.options), 12)

            label_rule = grammar.rules["Label"]
            self.assertEqual(len(label_rule.options), 3)

            variable_rule = grammar.rules["Variable"]
            self.assertEqual(len(variable_rule.options), 3)

            let_statement_rule = grammar.rules["LetStatement"]
            self.assertEqual(len(let_statement_rule.options), 1)

            print_statement_rule = grammar.rules["PrintStatement"]
            self.assertEqual(len(print_statement_rule.options), 1)

            option = grin_statement_rule.options[0]
            self.assertEqual(option.prob, 1)
            self.assertIsInstance(option.symbols[0], Variable)
            self.assertEqual(option.symbols[0].name, "Label")
            self.assertIsInstance(option.symbols[1], Variable)
            self.assertEqual(option.symbols[1].name, "UnlabeledGrinStatement")

        finally:
            os.unlink(temp_file_name)

if __name__ == '__main__':
    unittest.main()
