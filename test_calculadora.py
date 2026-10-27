import unittest
from unittest.mock import patch

from calculadora import ler_numero, main


class LerNumeroTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["dez", "10"])
    @patch("builtins.print")
    def test_retries_after_invalid_number(self, print_mock, input_mock):
        self.assertEqual(ler_numero("Numero: "), 10.0)
        self.assertEqual(input_mock.call_count, 2)
        print_mock.assert_called_once_with(
            "Entrada invalida. Digite um numero valido."
        )

    @patch("builtins.input", side_effect=["", "2"])
    @patch("builtins.print")
    def test_retries_after_empty_input(self, print_mock, input_mock):
        self.assertEqual(ler_numero("Numero: "), 2.0)
        self.assertEqual(input_mock.call_count, 2)
        print_mock.assert_called_once()


class MainTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["10", "2"])
    @patch("builtins.print")
    def test_divides_valid_numbers(self, print_mock, _input_mock):
        main()
        print_mock.assert_called_once_with("Quociente: 5.0")

    @patch("builtins.input", side_effect=["10", "0"])
    @patch("builtins.print")
    def test_handles_division_by_zero(self, print_mock, _input_mock):
        main()
        print_mock.assert_called_once_with(
            "Erro: nao e possivel dividir por zero."
        )

    @patch("builtins.input", side_effect=["dez", "10", "2"])
    @patch("builtins.print")
    def test_recovers_from_invalid_dividend(self, print_mock, _input_mock):
        main()
        print_mock.assert_any_call("Entrada invalida. Digite um numero valido.")
        print_mock.assert_called_with("Quociente: 5.0")


if __name__ == "__main__":
    unittest.main()
