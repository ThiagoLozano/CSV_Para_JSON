# PROJETO PYTHON: Converter CSV para JSON

> Script que pega um arquivo CSV e converte para o formato JSON.

# Tecnologias Utilizadas

* **_VScode_**;

* **_Python3;_** 

# Bibliotecas e Configurações

### Bibliotecas Utilizadas

```python
import csv
import json
```

### Configurações

> O script foi feito com base na estrutura POO.

```python
class Conversor:
    def __init__(self):

usuario = Conversor()
```

> Caso o CSV venha com separação em '|' (pipeline), use o parâmetro __delimiter='|'__

```python
self.orders = csv.reader(f, delimiter='|')
```

# Arquivo CSV

| ID   | Name        | Description         | Quantity | Value  |
| ---- | ----------- | ------------------- | -------- | ------ |
| 1    | Camisa      | Camisa Social       | 3        | 56.50  |
| 2    | Regata      | Regada 100% Algodão | 6        | 9.99   |
| 3    | Saia Rodada | Saia Rodada Rosa    | 2        | 29.00  |
| 4    | Meia        | Meia Branca         | 3        | 5.00   |
| 5    | Gorro       | Gorro Preto         | 1        | 12.00  |
| 6    | Moletom     | Moletom Adidas      | 1        | 119.95 |
| 7    | Bermuda     | Bermuda Ciclone     | 3        | 35.00  |
| 8    | Tênis       | Tênis Nike Shox     | 1        | 450.00 |

ID,Name,Description,Quantity,Value

1,Camisa,Camisa Social Preta,3,56.50

2,Regata,Regata 100% Algodão,6,9.99

3,Saia Rodada,Saia Rodada Rosa,2,29.90

4,Meia,Meia branca,3,5.00

5,Gorro,Gorro Preto,1,12.00

6,Moletom,Moletom Adidas,1,119.95

7,Bermuda,Bermuda Ciclone,3,35.00

8,Tênis,Tênis Nike Shox,1,450.00

### Leitura do CSV

```python
1. try:
2.    with open("loja.csv", 'r', encoding='utf_8') as f:
3.        self.orders = csv.reader(f)
4.        next(self.orders)
5.        self.Retorna_JSON()
6. except Exception as erro:
7.     print("Problema o ler o arquivo CSV: {}".format(erro))
8.     exit(0)
```

> Linha 1:  Chama a função Try.
>
> Linha 2:  Abre o arquivo CSV e atribui a vaiável __f__
>
> Linha 3: Cria um a variável que recebe os dados no formado de leitura CSV.
>
> Linha 4: Retorna uma linha pra baixo, desconsiderando o nome das colunas.
>
> Linha 5: Chama a função __Retorna_JSON()__
>
> Linha 6: Chama uma Exceção
>
> Linha 7: Retorna uma mensagem da tela.
>
> Linha 8: Fecha o Programa.

# Criar JSON

```python
1. def Retorna_JSON(self):
2.    dados = {"Orders": []}
3.
4.    for order in self.orders:
5.        dados['Orders'].append({"ID":order[0], "Name":order[1], "Description":order[2], "Quantity":order[3], "Value":order[4]})
6.
7.    with open("csv_to_json.json", "w") as f:
8.        json.dump(dados, f, ensure_ascii=False, indent=4)
```

> Linha 1: Cria a função __Retorna_JSON()__
>
> Linha 2: Cria um dicionário.
>
> Linha 4, 5: Cria um laço que passa pelo CSV e insere os valores no dicionário.
>
> Linha 7, 8: Cria um arquivo JSON e insere o dicionários com endentação já formatada.



# JSON

```json
{
    "Orders": [
        {
            "ID": "1",
            "Name": "Camisa",
            "Description": "Camisa Social Preta",
            "Quantity": "3",
            "Value": "56.50"
        },
        {
            "ID": "2",
            "Name": "Regata",
            "Description": "Regata 100% Algodão",
            "Quantity": "6",
            "Value": "9.99"
        },
        {
            "ID": "3",
            "Name": "Saia Rodada",
            "Description": "Saia Rodada Rosa",
            "Quantity": "2",
            "Value": "29.90"
        },
        {
            "ID": "4",
            "Name": "Meia",
            "Description": "Meia branca",
            "Quantity": "3",
            "Value": "5.00"
        },
        {
            "ID": "5",
            "Name": "Gorro",
            "Description": "Gorro Preto",
            "Quantity": "1",
            "Value": "12.00"
        },
        {
            "ID": "6",
            "Name": "Moletom",
            "Description": "Moletom Adidas",
            "Quantity": "1",
            "Value": "119.95"
        },
        {
            "ID": "7",
            "Name": "Bermuda",
            "Description": "Bermuda Ciclone",
            "Quantity": "3",
            "Value": "35.00"
        },
        {
            "ID": "8",
            "Name": "Tênis",
            "Description": "Tênis Nike Shox",
            "Quantity": "1",
            "Value": "450.00"
        }
    ]
}
```

