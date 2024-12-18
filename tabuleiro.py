# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        # Inicializa o tabuleiro 3x3 com todas as posições desconhecidas
        self.matriz = [[Tabuleiro.DESCONHECIDO] * 3 for _ in range(3)]

    def tem_campeao(self):
        #Verifica se há um vencedor no tabuleiro.
        
        #Retorna:
            #- JOGADOR_0 (1) se o jogador 0 venceu
            #- JOGADOR_X (4) se o jogador X venceu
            #- DESCONHECIDO (0) se não há vencedor

        # Verifica linhas, colunas e diagonais
        for i in range(3):
            # Linhas e colunas
            soma_linha = sum(self.matriz[i])
            soma_coluna = sum(self.matriz[j][i] for j in range(3))

            # Diagonal principal e secundária
            soma_diag_principal = sum(self.matriz[j][j] for j in range(3))
            soma_diag_secundaria = sum(self.matriz[j][2 - j] for j in range(3))

            # Checa as somas para determinar o vencedor
            for soma in [soma_linha, soma_coluna, soma_diag_principal, soma_diag_secundaria]:
                if soma == 3:  # Três células do JOGADOR_0
                    return Tabuleiro.JOGADOR_0
                elif soma == 12:  # Três células do JOGADOR_X
                    return Tabuleiro.JOGADOR_X

        # Nenhum vencedor encontrado
        return Tabuleiro.DESCONHECIDO
