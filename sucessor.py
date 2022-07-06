def sucessor(estado):
    listSucessores = []

    posicao = estado.find('_')

    if (posicao != 2 and posicao != 5 and posicao != 8):
        caracter = estado[posicao + 1]
        posicaoSucessor = estado[:posicao] + caracter + '_' + estado[posicao + 2:]
        strSucessor = '(direita, "' + posicaoSucessor + '")'
        listSucessores.append(strSucessor)

    if (posicao != 0 and posicao != 3 and posicao != 6):
        caracter = estado[posicao - 1]
        posicaoSucessor = estado[:posicao-1] + '_' + caracter + estado[posicao + 1:]
        strSucessor = '(esquerda, "' + posicaoSucessor + '")'
        listSucessores.append(strSucessor)

    if (posicao != 0 and posicao != 1 and posicao != 2):
        caracter = estado[posicao - 3]
        posicaoSucessor = estado[:posicao - 3] + '_' + estado[posicao - 2:posicao] + caracter + estado[posicao + 1:]
        strSucessor = '(acima, "' + posicaoSucessor + '")'
        listSucessores.append(strSucessor)

    if (posicao != 6 and posicao != 7 and posicao != 8):
        caracter = estado[posicao + 3]
        posicaoSucessor = estado[:posicao] + caracter + estado[posicao + 1:posicao + 3] + '_' + estado[posicao + 4:]
        strSucessor = '(abaixo, "' + posicaoSucessor + '")'
        listSucessores.append(strSucessor)

    return listSucessores


def main():
    n = sucessor("2435_1687")
    print(n)

    return 0

if __name__ == "__main__":
    main()