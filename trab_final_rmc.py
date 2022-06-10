from hashlib import new
import math
import numpy as np
import matplotlib.pyplot as plt

def verificar_entrada(variavel, começo, fim, inteiro):
    if inteiro == True:
        valor = int(input("Informe o valor de "+variavel+" de "+str(começo)+" a "+str(fim)+": "))
        while valor < começo or valor > fim:
            valor = int(input("Informe um valor válido de "+variavel+" de "+str(começo)+" a "+str(fim)+": "))
    else:
        valor = float(input("Informe o valor de "+variavel+" de "+str(começo)+" a "+str(fim)+": "))
        while valor < começo or valor > fim:
            valor = float(input("Informe um valor válido de " + variavel + " de " + str(começo) + " a " + str(fim) + ": "))

    return valor

def gerar_grafico_2grau(x1, x2, a, b, c):
    eixo_x = []
    eixo_y = []
    zero = []

    variacao = abs(x1 - x2)
    if variacao < 3:
        variacao = 3
    print(variacao)

    for x in np.arange(x1 - variacao, x2 + variacao, variacao / 100):
        y = a * (x ** 2) + b * x + c
        eixo_x.append(x)
        eixo_y.append(y)
        zero.append(0.0)
    plt.plot(eixo_x, eixo_y, color="blue")
    plt.plot(eixo_x, zero, color="black")
    plt.show()

def calcular_delta(a, b, c):
    return b ** 2 - 4 * a * c

def func_segundograu(a, b, c):
    while True:
        print("\nBem vindo as funções de segundo grau.")
        print("Opção 0, voltar ao menu (reseta valores).\nOpção 1, calcular raízes.\nOpção 2, calcular função em x pedido\nOpção 3, calcular Vértice.\nOpção 4, gerar gráfico.")
        op = verificar_entrada("opção", 0, 4, True)

        if op == 0:
            break
        elif op == 1:
            delta = calcular_delta(a, b, c)
            if delta >= 0:
                x1 = (-b + math.sqrt(delta)) / 2 * a
                x2 = (-b - math.sqrt(delta)) / 2 * a
            else:
                x1 = complex(-b / 2 * a, math.sqrt(-delta) / 2 * a)
                x2 = complex(-b / 2 * a, - math.sqrt(-delta) / 2 * a)
            print("As raizes dessa função são:", x1, " e ", x2)

        elif op == 2:
            x = float(input("Informe o valor de x: "))
            resultado = a * x ** 2 + b * x + c
            print("O resultado de f(", x, ") é: ", resultado)

        elif op == 3:
            delta = calcular_delta(a, b, c)
            xv = - b / 2 * a
            yv = - delta / 4 * a
            print("Xv = ", xv, " e ", "Yv = ", yv)

        else:
            delta = calcular_delta(a, b, c)
            x1 = (-b + math.sqrt(delta)) / 2 * a
            x2 = (-b - math.sqrt(delta)) / 2 * a
            if delta >= 0:
                gerar_grafico_2grau(x1, x2, a, b, c)
            else:
                print("Número complexo.")

def func_exponencial(a, b):
    while True:
        print("\nBem vindo as funções exponenciais!")
        print("Opção 0, voltar ao menu (reseta valores).\nOpção 1, verificar se é crescente ou decrescente.\nOpção 2, calcular função em x pedido\nOpção 3, gerar gráfico.")
        op = verificar_entrada("opção", 0, 3, True)

        if op == 0:
            break

        elif op == 1:
            if b > 0 and b < 1:
                print("Função decrescente.")
            else:
                print("Função crescente.")

        elif op == 2:
            x = float(input("Informe o valor de x: "))
            resultado = a * b ** x
            print("O resultado de f(", x, ") é: ", resultado)

        elif op == 3:
            vetorX = np.arange(-7, 7, 0.1)

            vetorY = []

            for x in vetorX:
                vetorY.append(b ** x)

            fig = plt.figure(figsize=(5, 5))

            plt.plot(vetorX, vetorY, label = "Função exponencial", color = 'g')

            plt.title("f(x) = a^x")
            plt.xlabel("eixo x")
            plt.ylabel("eixo y")
            plt.legend()
            plt.grid(True, which=("both"))
            plt.axhline(y = 0, color = 'k')
            plt.axvline(x = 0, color = 'k')
            plt.show()

def gerar_matriz(linhas, colunas):
    matriz = []
    for linha in range(linhas):
        vetor = []
        for coluna in range(colunas):
            valor = float(input("Informe o valor da posição [" + str(linha) + "/" + str(coluna) + "]: "))
            vetor.append(valor)
        matriz.append(vetor)
    return matriz

def printar_matriz(matriz):
    linhas = len(matriz)
    print("\nMatriz: ")
    for linha in range(linhas):
        print(matriz[linha])

def matriz(matriz, linha, coluna):
    while True:
        print("\nBem vindo as matrizes!")
        print(
            "Opção 0, voltar ao menu (reseta valores).\nOpção 1, calcular o determinante.\nOpção 2, multiplicação\nOpção 3, matriz transposta.")
        op = verificar_entrada("opção", 0, 3, True)

        if op == 0:
            break

        elif op == 1:
            if linha == coluna:
                if linha == 1:
                    determinante = matriz[0]
                elif linha == 2:
                    determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
                elif linha == 3:
                    determinante = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][20] * matriz[2][0] + matriz[0][3] * matriz[1][0] * matriz[2][1] - matriz[0][2] * matriz[1][1] * matriz[2][0] - matriz[0][0] * matriz[1][2] * matriz[2][0] - matriz[0][1] * matriz[1][0] * matriz[2][2]
                else:
                    determinante = np.linalg.det(matriz)
                print("O determinante da matriz é ", determinante)
            else:
                print("Opção inválida, matriz não quadrática.")

        elif op == 2:
            linhas2 = int(input("Informe o número de linhas: "))
            while linhas2 <= 0:
                linhas2 = int(input("Informe um valor válido de linhas: "))

            colunas2 = int(input("Informe o número de colunas: "))
            while colunas2 <= 0:
                colunas2 = int(input("Informe um valor válido de colunas: "))

            if coluna == linhas2:
                matriz2 = gerar_matriz(linhas2, colunas2)
                printar_matriz(matriz2)

                matriz_multiplicada = []
                for l1 in range(linha):
                    vetor = []
                    for c2 in range(colunas2):
                        acumula = 0
                        for c1 in range(coluna):
                            acumula += matriz[l1][c1] * matriz2[c1][c2]
                        vetor.append(acumula)
                    matriz_multiplicada.append(vetor)
                print("Matriz multiplicada:")
                printar_matriz(matriz_multiplicada)
            else:
                print("Matrizes nao podem se multiplicar.")

        elif op == 3:
            matriz_transposta = [0] * coluna

            for c in range(coluna):
                matriz_transposta[c] = [0] * linha

            for l in range(linha):
                for c in range(coluna):
                    matriz_transposta[c][l] = matriz[l][c]

            printar_matriz(matriz_transposta)

while True:
    print("\nBem vindo a calculadora RMC.")
    print("Opção 0, sair.")
    print("Opção 1, funções do segundo grau.")
    print("Opção 2, funções exponenciais.")
    print("Opção 3, Matrizes.")
    opcao = verificar_entrada("opção", 0, 3, True)

    if opcao == 0:
        print("Obrigado por usar.")
        break

    elif opcao == 1:
        a = float(input("Informe o valor de a: "))
        b = float(input("Informe o valor de b: "))
        c = float(input("Informe o valor de c: "))
        func_segundograu(a, b, c)
    elif opcao == 2:
        a = float(input("Informe o valor de a: "))
        b = float(input("Informe o valor de b: "))
        while b <= 0:
            b = float(input("B menor ou igual a 0, informe um valor válido de b: "))
        func_exponencial(a, b)

    elif opcao == 3:

        linhas = int(input("Informe o número de linhas: "))
        while linhas <= 0:
            linhas = int(input("Informe um valor válido de linhas: "))

        colunas = int(input("Informe o número de colunas: "))
        while colunas <= 0:
            colunas = int(input("Informe um valor válido de colunas: "))

        matriz1 = gerar_matriz(linhas, colunas)
        printar_matriz(matriz1)
        matriz(matriz1, linhas, colunas)