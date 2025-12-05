import argparse


class Produto:
    # -------------------------
    #       ATRIBUTOS
    # -------------------------
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = int(quantidade)

    # -------------------------
    #       MÉTODOS
    # -------------------------
    def adicionar_stock(self, quantidade):
        # Só adiciona se quantidade for positiva
        if quantidade > 0:
            self.quantidade += quantidade
            print(1)
        else:
            print(0)

    def vender(self, quantidade):
        # Só vende se houver stock suficiente
        if 0 < quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(1)
        else:
            print(0)

    def exibir_info(self):
        # Formato pedido: "[nome] [preco] [quantidade]"
        print(f"[{self.nome}] [{self.preco}] [{self.quantidade}]")


# ----------------------------------------------------------------------
#                     NÃO MEXER NO CÓDIGO ABAIXO
# ----------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerir um Produto")
    parser.add_argument(
        "-A",
        "--acao",
        required=True,
        choices=["adicionar", "vender", "info"],
        help="Ação a Executar",
    )
    parser.add_argument(
        "-Q", "--quantidade", type=int, help="Quantidade Para Adicionar ou Vender"
    )
    args = parser.parse_args()

    produto = Produto("Teclado", 49.90, 10)

    if args.acao == "adicionar":
        if args.quantidade is None:
            print("É Necessário Fornecer a Quantidade Para Adicionar.")
        else:
            produto.adicionar_stock(args.quantidade)

    elif args.acao == "vender":
        if args.quantidade is None:
            print("É Necessário Fornecer a Quantidade Para Vender.")
        else:
            produto.vender(args.quantidade)

    elif args.acao == "info":
        produto.exibir_info()

