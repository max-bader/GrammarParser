import random
import unittest
from unittest.mock import patch, Mock
from grammar_design import Terminal, Grammar, Rule, Option, Variable


class TestGrammarDesign(unittest.TestCase):
    def test_terminal_generate(self):
        terminal = Terminal("test")
        result = terminal.generate(None)
        self.assertEqual(result, "test")

    def setUp(self):
        self.option = Option(1, [Terminal("option")])
        self.option2 = Option(1, [Terminal("option2")])
        self.options = [self.option, self.option2]

    @patch('random.randint', return_value=1)
    def test_rule_gen_opt(self, mock_randint):
        rule = Rule("var", self.options)
        result = rule.generate(None)
        self.assertEqual(result, "option")

    @patch('random.randint', return_value = 2)
    def test_rule_gen_opt2(self, mock_randint):
        rule = Rule("var", self.options)
        result = rule.generate(None)
        self.assertEqual(result, "option2")

    def test_grammar_add(self):
        grammar = Grammar()
        start = "StartVariable"
        options = [Option(1, [Terminal("option")]), Option(2, [Terminal("option2")])]

        grammar.add(start, options)
        self.assertIn(start, grammar.rules)

        new_rule = grammar.rules[start]
        self.assertIsInstance(new_rule, Rule)
        self.assertEqual(new_rule.variable, start)
        self.assertEqual(new_rule.options, options)

    def test_grammar_generate(self):
        grammar = Grammar()
        mock_rule = Mock(spec=Rule)
        mock_rule.generate.return_value = "sentence"

        grammar.rules["StartVariable"] = mock_rule
        result = grammar.generate("StartVariable")

        mock_rule.generate.assert_called_once_with(grammar)
        self.assertEqual(result, "sentence")

    def test_variable_generate(self):
        grammar = Grammar()
        mock_rule = Mock(spec = Rule)
        mock_rule.generate.return_value = "sentence"

        grammar.rules["Variable"] = mock_rule
        var = Variable("Variable")
        result = var.generate(grammar)

        mock_rule.generate.assert_called_once_with(grammar)
        self.assertEqual(result, "sentence")
