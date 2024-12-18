from random import choice
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        def verifica_vitoria_ou_bloqueio(tipo, alvo):
            #Verifica linhas, colunas e diagonais para uma possível vitória ou bloqueio.
            for i in range(3):
                if sum(self.matriz[i][j] for j in range(3)) == alvo:  #Linha
                    for j in range(3):
                        if self.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                            return (i, j)
                if sum(self.matriz[j][i] for j in range(3)) == alvo:  #Coluna
                    for j in range(3):
                        if self.matriz[j][i] == Tabuleiro.DESCONHECIDO:
                            return (j, i)

            # Diagonais
            if sum(self.matriz[j][j] for j in range(3)) == alvo:
                for j in range(3):
                    if self.matriz[j][j] == Tabuleiro.DESCONHECIDO:
                        return (j, j)
            if sum(self.matriz[j][2 - j] for j in range(3)) == alvo:
                for j in range(3):
                    if self.matriz[j][2 - j] == Tabuleiro.DESCONHECIDO:
                        return (j, 2 - j)
            return None

        def cria_duas_sequencias(tipo):
            #Identifica uma jogada que cria duas sequências de duas marcações.
            for l in range(3):
                for c in range(3):
                    if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                        # Simula a jogada
                        self.matriz[l][c] = tipo
                        count = 0
                        if verifica_vitoria_ou_bloqueio(tipo, 2 * tipo):
                            count += 1
                        # Restaura o tabuleiro
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        if count >= 2:  # Se criar duas sequências, retorna a jogada
                            return (l, c)
            return None

        #Regra 1: Vitória ou bloqueio
        jogada = verifica_vitoria_ou_bloqueio(self.tipo, 2 * self.tipo)  #Tentar vencer
        if jogada:
            return jogada

        oponente = Tabuleiro.JOGADOR_0 if self.tipo == Tabuleiro.JOGADOR_X else Tabuleiro.JOGADOR_X
        jogada = verifica_vitoria_ou_bloqueio(oponente, 2 * oponente)  #Bloquear oponente
        if jogada:
            return jogada

        #Regra 2: Criar duas sequências
        jogada = cria_duas_sequencias(self.tipo)
        if jogada:
            return jogada

        #Regra 3: Marcar o centro
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        #Regra 4: Marcar canto oposto
        cantos_opostos = [((0, 0), (2, 2)), ((0, 2), (2, 0)), ((2, 0), (0, 2)), ((2, 2), (0, 0)),]
        for canto, oposto in cantos_opostos:
            if self.matriz[canto[0]][canto[1]] == oponente and self.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                return oposto

        #Regra 5: Marcar qualquer canto vazio
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        cantos_disponiveis = [canto for canto in cantos if self.matriz[canto[0]][canto[1]] == Tabuleiro.DESCONHECIDO]
        if cantos_disponiveis:
            return choice(cantos_disponiveis)

        #Regra 6: Marcar qualquer posição vazia
        disponiveis = [(l, c) for l in range(3) for c in range(3) if self.matriz[l][c] == Tabuleiro.DESCONHECIDO]
        if disponiveis:
            return choice(disponiveis)

        return None
