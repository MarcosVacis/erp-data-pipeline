import logging

from extract.extract import(carregar_clientes)

def main ():
    logging.basicConfig(level= logging.INFO, format="%(Asctime) s - %(levelname)s- %(message)s")


dados = carregar_clientes()

print(dados)

if __name__ == "__main__":
    main
