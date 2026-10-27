def ler_numero(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada invalida. Digite um numero valido.")


def main() -> None:
    dividendo = ler_numero("Digite o dividendo: ")
    divisor = ler_numero("Digite o divisor: ")

    try:
        quociente = dividendo / divisor
    except ZeroDivisionError:
        print("Erro: nao e possivel dividir por zero.")
    else:
        print(f"Quociente: {quociente}")


if __name__ == "__main__":
    main()
