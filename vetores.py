print('\033[1;34mOperações com vetores\033[0m')
# escolha da dimensão 2D ou 3D
dimensao = int(input('Escolha a dimensão dos vetores (2 ou 3): '))

if dimensao not in [2, 3]:
    print('Dimensão inválida')
else:
    # lê os vetores
    vetor_1 = list(map(float, input('Digite as coordenadas do primeiro vetor: ').split()))
    vetor_2 = list(map(float, input('Digite as coordenadas do segundo vetor: ').split()))

    if len(vetor_1) != dimensao or len(vetor_2) != dimensao:
        print('Número de coordenadas não corresponde com a dimensão que foi escolhida')
    else:
        print('Qual operação deseja realizar: ')
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação por escalar')
        print('4 - Produto interno')
        if dimensao == 3:
            print('5 - Produto vetorial')
            print('6 - Produto misto')

        operacao = int(input('Escolha a operação (1-6): '))

        if operacao == 1:
            resultado = [vetor_1[i] + vetor_2[i] for i in range(dimensao)]
            print(f'Resultado da Adição: \033[1;32m{resultado}\033[0m')
        elif operacao == 2:
            resultado = [vetor_1[i] - vetor_2[i] for i in range(dimensao)]
            print(f'Resultado da Subtração: \033[1;32m{resultado}\033[0m')
        elif operacao == 3:
            escalar = float(input('Digite o valor do escalar: '))
            resultado = [componente * escalar for componente in vetor_1]
            print(f'Resultado da Multiplicação por escalar: \033[1;32m{resultado}\033[0m')
        elif operacao == 4:
            resultado = sum(vetor_1[i] * vetor_2[i] for i in range(dimensao))
            print(f'Resultado do Produto interno: \033[1;32m{resultado}\033[0m')
        elif operacao == 5 and dimensao == 3:
            i = vetor_1[1] * vetor_2[2] - vetor_1[2] * vetor_2[1]
            j = vetor_1[2] * vetor_2[0] - vetor_1[0] * vetor_2[2]
            k = vetor_1[0] * vetor_2[1] - vetor_1[1] * vetor_2[0]
            print(f'Resultado do Produto vetorial: vetor \033[1;32m({i}, {j}, {k})\033[0m')
        elif operacao == 6 and dimensao == 3:
            vetor_3 = list(map(float, input('Digite as coordenadas do terceiro vetor: ').split()))
            if len(vetor_3) != 3:
                print('O vetor precisa ter 3 coordenadas')
            else:
                i = vetor_2[1] * vetor_3[2] - vetor_2[2] * vetor_3[1]
                j = vetor_2[2] * vetor_3[0] - vetor_2[0] * vetor_3[2]
                k = vetor_2[0] * vetor_3[1] - vetor_2[1] * vetor_3[0]
                resultado = vetor_1[0] * i + vetor_1[1] * j + vetor_1[2] * k
                print(f'Resultado do Produto misto: \033[1;32m{resultado}\033[0m')
        else:
            print('Operação inválida')
