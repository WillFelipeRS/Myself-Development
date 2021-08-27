import random

# Enunciado do Jogo:
print('\nJogo da Forca:')
print('Nesse jogo você deverá adivinhar uma palavra sorteada pelo computador.')
print('Para isso, você deve ir inserindo letras e, para cada letra correta, a palavra vai sendo completada.')
print('Mas, para cada letra incorreta, uma parte de você vai para a forca!')
print('Após 7 letras erradas, o seu bonequinho será enforcado e você perde... mas se acertar, ele estará livre!')
print('Não se preocupe com acentos; se a palavra sorteada for \"AVIÃO\" e você digitar \"A\", o programa vai reconhecer')
print('tanto o \"A\" como o \"Ã\" como sendo letras corretas. A palavra vai ficar ao final como \"AVIAO\".')

# Abre o banco de palavras em txt que está na pasta do projeto:
arquivo = open("bancoPalavras.txt", "r", encoding="utf-8")
bancoPalavras = arquivo.read()
bancoPalavras = bancoPalavras.strip().split('\n')
arquivo.close()

# Validação de entrada:
def validacaoEntrada():
    letra = input('\nDigite uma letra qualquer: ').upper()
    while letra not in alfabeto:
        letra = input('\nEntrada inválida! Digite uma outra letra qualquer: ').upper()
    while letra in letrasUsadas:
        letra = input('\nEsta letra já foi utilizada! Digite uma outra letra qualquer: ').upper()
    letrasUsadas.append(letra)
    return letra

# Validação de resposta para jogar de novo:
def validacaoNovoJogo():
    respostaDeNovo = input('Você quer jogar de novo? Digite S ou N: ) ').upper()
    while respostaDeNovo not in ['S','N']:
        respostaDeNovo = input('Não entendi... você quer jogar de novo? Digite S ou N: ) ').upper()
    return respostaDeNovo

# Imprime o bonequinho livre em caso de vitória: 
def vitoria():
    print('\n----------')
    print('|/       |     VOCÊ VENCEU!!!')
    print('|')
    print('|                  (^.^)')
    print('|                   \|/')
    print('|                    |')
    print('|---                / \\')

# Imprime o bonequinho enforcado em caso de derrota:
def derrota():
    print('\n----------')
    print('|/       |')
    print('|      (x.x)')
    print('|       /|\\')
    print('|        |')
    print('|       / \\    Você perdeu...')
    print('|---')

# Imprime o bonequinho durante o jogo:
def bonequinho():
    if erros == 0:
        print('\n----------')
        print('|/       |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|---')
    elif erros == 1:
        print('\n----------')
        print('|/       |')
        print('|      (-.-) ...')
        print('|')
        print('|')
        print('|')
        print('|---')
    elif erros == 2:
        print('\n----------')
        print('|/       |')
        print('|      (-.-) ...')
        print('|       /')
        print('|')
        print('|')
        print('|---')
    elif erros == 3:
        print('\n----------')
        print('|/       |')
        print('|      (o.o)\"\"')
        print('|       /|')
        print('|')
        print('|')
        print('|---')
    elif erros == 4:
        print('\n----------')
        print('|/       |')
        print('|      (o.o)\"\"')
        print('|       /|\\')
        print('|')
        print('|')
        print('|---')
    elif erros == 5:
        print('\n----------')
        print('|/       |')
        print('|      (O.O) !!!!!!')
        print('|       /|\\')
        print('|        |')
        print('|')
        print('|---')
    elif erros == 6:
        print('\n----------')
        print('|/       |')
        print('|      (O.O) !!!!!!')
        print('|       /|\\')
        print('|        |')
        print('|       /')
        print('|---')

# Verifica se o chute está na palavra sorteada (palavraLista):
def acertou():
    indice = 0
    for elemento in palavraLista:
        if chute == elemento: palavraJogo[indice] = chute
        indice += 1 
    return print(''.join(palavraJogo))

# Variáveis iniciais:
novoJogo = 'S'
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Jogo:
while novoJogo == "S":
    palavra = random.choice(bancoPalavras)
    palavraLista = list(palavra)
    palavraJogo = list('_'*len(palavra))
    letrasUsadas = []
    tentativas = 7
    erros = 0
    print('\nVamos começar!\n')
    print(''.join(palavraJogo))
    bonequinho()

    while tentativas > 0 and palavraLista != palavraJogo:
        chute = validacaoEntrada()
        print(f'\nAs letras utilizadas foram: {" ".join(letrasUsadas)}')
        if chute in palavraLista:
            print(f'Você acertou! Tentativas restantes: {tentativas}\n')
            acertou() 
        else:
            tentativas -= 1
            erros += 1
            print(f'Você errou... Tentativas restantes: {tentativas}\n')
            print(''.join(palavraJogo))
        if palavraLista != palavraJogo: bonequinho() 
        
    if palavraLista == palavraJogo:
        vitoria()
    else:
        derrota()
        print(f'A palavra era: {("".join(palavraLista)).capitalize()}')
    novoJogo = validacaoNovoJogo()

print('\nAgradecimentos:')
print('Agradeço primeiramente à minha mãe, Ana Beatriz Silva Lopes, por me mandar uma notícia sobre Data Science')
print('e fazer com que eu me interessasse pelo assunto e começasse a estudá-lo;')
print('À minha irmã Daniele Rodrigues da Silva, por me apoiar incondicionalmente;')
print('Aos amigos Antenor Fischer, Saulo Gruginskie, Samara Menezes, Elisâmua Neris, Roque Prestes de Souza,')
print('Angelita Fraga, Naldine Corrêa, Paula Bueno e Juliana D A por me ajudarem com o banco de palavras.')
print('Ao meu professor Brian Nunes por me ajudar com esse código independentemente do horário, inclusive num domingo;')
print('E, por fim, à Let\'s Code, minha escola de programação, que me trouxe professores maravilhosos e que')
print('confirma todos os dias que escolhi a área certa, além de me dar todo o conhecimento que preciso para ser um ótimo profissional.')
print('Vos deixo meu muito obrigado a todos!!!')

print('\nProject made by Will')

print('\nFim do programa.')
