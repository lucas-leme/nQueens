import numpy as np

# Funcao recursiva, que testa por meio do metodo BackTracking todas as posicoes;
# Este metodo foi implementado colocando-se uma rainha por coluna, da esquerda
# Para a direita, e assim ajustando o tabuleiro conforme as verificacoes de ataque/defesa
def backTracking(tabuleiro, coluna, dimensao):

    # Caso base da recursao
    if coluna >= dimensao:
        return True

    # Verificacao das linhas, incrementa-se 1 na linha, se a posicao nao for valida
    for linha in range(dimensao):

        if verificaPosicao(tabuleiro, linha, coluna, dimensao):
            tabuleiro[linha][coluna] = "R"
            

            if backTracking(tabuleiro, coluna + 1, dimensao):
                return True
            # Caso futuros backTracking nao deem certo, altera-se a linha, atribuindo caracter nula para a linha invalida
            else:
                tabuleiro[linha][coluna] = ""

    return False


# Funcao que verifica se a posicao da rainha e valida, ou seja,
# Se a posicao nao esta em risco de sofrer um ataque
def verificaPosicao(tabuleiro, linha, coluna, dimensao):

    # retira-se a rainha para a verificacao do tabuleiro
    tabuleiro[linha][coluna] = ""

    # Verificacao Horizontal (Fixa-se a linha)
    for j in range(dimensao):
        if tabuleiro[linha][j] == "R":
            return False

    # Verificacao de Diagonal Principal
    # Utilizando a funcao da biblioteca numpy, diagonal, que dado um offset de uma array 2D
    # Ela retorna um array 1D da diagonal
    tabDiagPrinc = np.diagonal(tabuleiro, coluna - linha)
    for i in range(np.size(tabDiagPrinc)):
        if tabDiagPrinc[i] == "R":
            return False

    # Verificacao da Diagonal Secundaria
    # Utiliza-se a funcao fliplr, que transpoe a matriz, para facilitar a obtencao da diagonal secundaria
    # offset calculado como complemento em relacao a dimensao da matriz, alem do vetor (1, 1) da diagonal
    tabAux = np.fliplr(tabuleiro)
    tabDiagSec = np.diagonal(tabAux, dimensao - 1 - (coluna + linha))
    for i in range(np.size(tabDiagSec)):
        if tabDiagSec[i] == "R":
            return False

    # recolocacao da rainha, apos a verificacao
    tabuleiro[linha][coluna] = "R"

    # Verificacao concluida
    return True


def main():
    N = int(input("Insira a dimensao do tabuleiro: "))

    # Criacao do Tabuleiro
    tabuleiro = np.zeros((N, N), dtype=str)

    coluna = 0
    backTracking(tabuleiro, coluna, N)

    print(tabuleiro)


main()
