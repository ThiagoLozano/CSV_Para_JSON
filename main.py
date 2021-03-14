import csv
import json


class Conversor:
    # Método construtor.
    def __init__(self):
        # Abre o arquivo JSON.
        try:
            with open("loja.csv", 'r', encoding='utf_8') as f:
                self.orders = csv.reader(f)
                next(self.orders)
                self.Retorna_JSON()
        except Exception as erro:
            print("Problema o ler o arquivo CSV: {}".format(erro))
            exit(0)

    def Retorna_JSON(self):
        # Cria um Dicionário. 
        dados = {"Orders": []}

        # Insere as informações do dicionário.
        for order in self.orders:
            dados['Orders'].append({"ID":order[0], "Name":order[1], "Description":order[2], "Quantity":order[3], "Value":order[4]})

        # Cria o JSON.
        with open("csv_to_json.json", "w") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)


usuario = Conversor()
