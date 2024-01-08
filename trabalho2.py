# Foi importado a biblioteca heapq, que será usada para
# implementar filas de prioridade (heap).

# Foi importado o módulo os, que fornece funcionalidades
# relacionadas ao sistema operacional, caso seja necessário.

# Foi importado a classe defaultdict do módulo collections,
# para criar dicionários com valores padrões.

import heapq
import os
from collections import defaultdict

# Criei a função encode para realizar a codificação de 
# Huffman com base nas frequências dos símbolos.
def encode(frequency):
    # Irá criar uma lista de listas, onde cada lista contém
    # o peso e um símbolo.
    heap = [[weight, [symbol, ""]] for symbol, weight in
             frequency.items()]
    # Irá converter a lista em um heap (fila de prioridade).
    heapq.heapify(heap)
    
    # Irá construir a árvore de Huffman enquanto houver
    # mais de um elemento no heap.
    while len(heap) > 1:
        # Remove os dois elementos de menor peso do heap.
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        # Adiciona '0' ao código de cada símbolo na
        # subárvore de menor peso.
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        
        # Adiciona '1' ao código de cada símbolo na
        # subárvore de maior peso.
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        # Adiciona a subárvore resultante ao heap.
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    # Retorna os códigos de Huffman ordenados por
    # comprimento e ordem lexicográfica.
    return sorted(heapq.heappop(heap)[1:],
                   key=lambda p: (len(p[-1]), p))

# Criei essa função para comprimir uma string de dados
# usando codificação de Huffman.
def compress(data):
    # Divide a string em palavras.
    words = data.split(' ')
    
    # Irá calcular a frequência de cada palavra usando
    # defaultdict.
    frequency = defaultdict(int)
    for word in words:
        frequency[word] += 1
    
    # Obtém os códigos de Huffman usando a função encode.
    huff = encode(frequency)
    
    # Irá gerar a versão compactada da string de
    # entrada usando os códigos de Huffman.
    output = ""
    for word in words:
        for p in huff:
            if p[0] == word:
                output += p[1]
    
    # Por fim retorna a string compactada
    # e os códigos de Huffman.
    return output, huff

# Criei a função para descomprimir uma string de dados
# usando códigos de Huffman.
def decompress(data, huff):
    output = ""
    acc = ""
    
    # Irá iterar sobre a string compactada, reconstruindo
    # a string original.
    for d in data:
        acc += d
        for p in huff:
            if p[1] == acc:
                output += p[0] + ' '
                acc = ""
    
    # Por fim retorna a string descompactada.
    return output

# Criei uma função principal que será utilizada para
# implementar a interface de linha de comando.
def main():
    # Looping para o sistema ficar esperando a
    # opção selecionada pelo usuário.
    while True:
        print("1. Compactar")
        print("2. Descompactar")
        option = input("Escolha uma opção: ")
        
        # Irá compactar o arquivo escolhido pelo usuário e
        # escrever uma mensagem de sucesso.
        if option == '1':
            filename = input("Digite o nome do arquivo a ser compactado: ")
            with open(filename, 'r') as f:
                data = f.read()
            compressed_data, huff = compress(data)
            with open("saida.huf", 'w') as f:
                f.write(compressed_data)
            print("Arquivo compactado com sucesso.")
        
        # Irá descompactar o arquivo escolhido pelo
        # usuário e enviar uma mensagem de sucesso.
        elif option == '2':
            filename = input("Digite o nome do arquivo a ser descompactado: ")
            with open(filename, 'r') as f:
                data = f.read()
            decompressed_data = decompress(data, huff)
            with open("entrada.txt", 'w') as f:
                f.write(decompressed_data)
            print("Arquivo descompactado com sucesso.")
        
        # Irá sair do loop se o usuário escolher uma opção
        # diferente das oferecidas.
        else:
            break

# Executa a função main se o script estiver sendo
# executado como um programa principal.
if __name__ == "__main__":
    main()
