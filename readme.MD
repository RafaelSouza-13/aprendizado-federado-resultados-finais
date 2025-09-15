# Projeto MNIST - Resultados FedAvg
Este projeto contém os resultados de treinamento de modelos FedAvg no dataset MNIST, incluindo cenários com e sem ataques. Ele permite visualizar métricas como acurácia, perda, matriz de confusão e recall por classe.

## Cenário
Conjunto de dados MNIST, foi realizado os testes com 20 clientes, sendo 40%, 8 clientes, envenenando o modelo. Também foi realizado com 60%, 12 clientes, mas não está inserido no código ainda. O número total de rounds foi de 100 com os dados iid e balanceados.
Foi feito o flipping normal, onde os alvo e a fonte eram fixos, flipping onde o alvo era fixo porém a fonte era aleatória ao decorrer dos rounds e alvo e fonte aleatórias ao decorrer dos rounds.

## Pré-requisitos

- Python 3.10 ou superior
- Virtualenv (recomendado)
- Pip

## Instalação

1. Clone o repositório:

    ```bash
    git git@github.com:RafaelSouza-13/aprendizado-federado-resultados-finais.git
    cd <NOME_DO_REPOSITORIO>

2. Crie e ative um ambiente virtual a depender do seu sistema operacional
    ```bash
    python -m venv .venv

3. Instale as dependências
    ```bash
    pip install -r requirements.txt

4. Execute o MAIN.ipynb