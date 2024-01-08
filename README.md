# Algoritmo baseado em código de Huffman para compactar e descompactar um texto por palavras.

Esse é um programa simples em Python que utiliza codificação em Huffman para compactar e descompactar arquivos de texto existentes.


# Requisitos para rodar o código

Para utilização do código foi instalado apenas o python3. Todos os módulos, bibliotecas e classes que foram importados sendo eles: "os", "heapq", e a classe defaultdict do módulo collections não necessitam de instalação, pois os mesmos já vem incluídas ao instalar o python3.

Para o código funcionar de acordo, é necessário ter um arquivo de entrada no formato .txt para compacta-lo, e após compactar, será possível realizar a descompactação do mesmo.

# Sistema Operacional

Para o desenvolvimento do trabalho foi utilizado o Linux Ubuntu.

# Ambiente de desenvolvimento

Para o desenvolvimento do trabalho foi utilizado o Visual Studio Code.

# Modo de utilização

Após todos os requisitos estarem de acordo, basta executar o código, feito isso, o programa irá apresentar um menu permitindo a escolha do usuário entre "1. Compactar" ou "2. Descompactar".

## Escolhendo a opção 1

Escolhendo essa opção, basta digitar o nome do arquivo com o final .txt para que o mesmo seja compactado. Ele será compactado com sucesso e criará o arquivo 'saida.huf'. 

Para se verificar se esta sendo compactado com sucesso, basta abrir em seu diretório o arquivo saida.huf, caso queira fazer novos testes basta excluir o arquivo 'saida.huf' e realizar o procedimento novamente.

## Escolhendo a opção 2

Para a escolha dessa opção é necessário ja possuir um arquivo já compactado, como por exemplo o arquivo que é criado na opção 1 'saida.huf'. Essa opção irá descompactar o arquivo após digitar o seu nome com o final .huf. Ele irá descompactar e irá salvar o arquivo como 'entrada.txt' assim como era antes.

Para verificar se esta descompactando com sucesso, o ideal seria apagar o arquivo entrada.txt antes de selecionar a opção para descompactar, assim você estaria confirmando que ele está sim criando um novo arquivo 'entrada.txt', pois caso não faça isso ele apenas substituirá o arquivo novo descompactado em cima do antigo arquivo.

## Digitando qualquer opção que não seja 1 ou 2

O sistema de compressão é encerrado.