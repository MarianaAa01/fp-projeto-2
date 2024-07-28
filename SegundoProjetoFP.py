#Segundo projeto de FP
#Mariana Silva de Carvalho
#109974

def cria_intersecao(col, lin):
    """
    cria intersecao: str x int → intersecao
    Esta função recebe um caracter e um inteiro correspondentes 
    à coluna col e à linha lin e devolve a interseção correspondente.
    """
    if not isinstance(col, str) or type(lin)!=int or len(col)!=1 or not 65<=ord(col)<=83 or not 1<=lin<=19:
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (col, lin)

def obtem_col(i):
    """
    obtem col: intersecao → str
    Esta função devolve a coluna col da interseção i.
    """
    return i[0]

def obtem_lin(i):
    """
    obtem lin: intersecao → int
    Esta função devolve a linha lin da interseção i.
    """
    return i[1]

def eh_intersecao(arg):
    """
    eh intersecao: universal → booleano
    Esta função devolve True caso o argumento seja um 
    TAD intersecao e False caso contrário.
    """
    #Verifica-se que a interseção é um tuplo.
    if not isinstance(arg,tuple):
        return False
    #Verifica-se que a interseção é constituída por dois elementos(uma letra e um número).
    elif len(arg) != 2:
        return False
    #Verifica-se que o primeiro elemento(letra) é uma string e que o segundo elemento(numero) é um inteiro.
    elif (not isinstance (obtem_col(arg), str)) or type(obtem_lin(arg))!=int:
        return False
    elif len(obtem_col(arg))!=1: 
        return False
    #Verifica-se que a letra vai de A a S e que o numero vai de 1 a 19.
    elif not (65<=ord(obtem_col(arg))<=83) or not (1<= obtem_lin(arg)<= 19): 
        return False    
    else:
        return True

def intersecoes_iguais(i1, i2):
    """
    intersecoes iguais: universal x universal → booleano
    Esta função devolve True apenas se i1 e i2 forem 
    interseções e iguais, e False caso contrário.
    """
    #Verifica-se que são duas interseções.
    if not eh_intersecao(i1) or not eh_intersecao(i2):
        return False
    #Verifica-se que a letra da primeira interseção é igual à letra da segunda e que o número da primeira interseção é igual ao número da segunda.
    elif obtem_col(i1)==obtem_col(i2) and obtem_lin(i1)== obtem_lin(i2):
        return True

def intersecao_para_str(i):
    """
    intersecao para str : intersecao → str
    Esta função devolve a cadeia de caracteres que representa o seu argumento.
    """
    return str(obtem_col(i))+str(obtem_lin(i))

def str_para_intersecao(s):
    """
    str para intersecao: str → intersecao
    Esta função devolve a interseção representada pelo seu argumento.
    """
    return (s[0],int(s[1:]))

def obtem_intersecoes_adjacentes(i,l):
    """
    obtem intersecoes adjacentes: intersecao x intersecao → tuplo
    Esta função devolve um tuplo com as interseções adjacentes à interseção i 
    de acordo com a ordem de leitura, sendo que l corresponde à interseção superior direita do tabuleiro de Go.
    """
    #O numero maximo de linhas no tabuleiro é dado por obtem_lin(l) e o numero maximo de colunas é dado por obtem_col(l).
    letra = ord(i[0])-65
    tuplo_com_intersecoes=()
    #É sempre necessário verificar que as interseções seguintes são válidas antes de adicionar ao tuplo_com_intersecoes que vai acumulando as interseções adjacentes.
    #É também necessário verificar que a coluna e a linha de cada interseção é sempre menor do que a coluna e linha da interseção no canto superior direito.
    cima = ((chr(letra+65)), (obtem_lin(i)-1))
    if eh_intersecao(cima) and obtem_lin(cima)<=obtem_lin(l) and obtem_col(cima)<=obtem_col(l): 
        tuplo_com_intersecoes += (cima,)
    esquerda = ((chr(letra+64)), obtem_lin(i))
    if eh_intersecao(esquerda) and obtem_lin(esquerda)<=obtem_lin(l) and obtem_col(esquerda)<=obtem_col(l):
        tuplo_com_intersecoes += (esquerda, )
    direita = ((chr(letra+66)), obtem_lin(i))
    if eh_intersecao(direita) and obtem_lin(direita)<=obtem_lin(l) and obtem_col(direita)<=obtem_col(l):
        tuplo_com_intersecoes += (direita,)
    baixo = ((chr(letra+65)),(obtem_lin(i)+1))
    if eh_intersecao(baixo) and obtem_lin(baixo)<=obtem_lin(l) and obtem_col(baixo)<=obtem_col(l):
        tuplo_com_intersecoes += (baixo,)
    return ordena_intersecoes(tuplo_com_intersecoes)

def ordena_intersecoes(t):
    """
    ordena intersecoes: tuplo → tuplo
    Esta função devolve um tuplo de interseções com as mesmas interseções de t 
    ordenadas de acordo com a ordem de leitura do tabuleiro de Go.
    """
    return tuple(sorted(t, key=lambda i: (obtem_lin(i), obtem_col(i))))

def cria_pedra_branca():
    """
    cria pedra branca: {} → pedra
    Esta função devolve uma pedra pertencente ao jogador branco.
    """
    return 'O'

def cria_pedra_preta():
    """
    cria pedra preta: {} → pedra
    Esta função devolve uma pedra pertencente ao jogador preto.
    """
    return 'X'

def cria_pedra_neutra():
    """
    cria pedra neutra: {} → pedra
    Esta função devolve uma pedra neutra.
    """
    return '.'

def eh_pedra(arg):
    """
    eh pedra: universal → booleano
    Esta função devolve True caso o seu argumento seja um TAD pedra 
    e False caso contrário.
    """
    if arg==cria_pedra_branca() or arg==cria_pedra_preta() or arg==cria_pedra_neutra():
        return True
    else:
        return False

def eh_pedra_branca(p):
    """
    eh pedra branca: pedra → booleano
    Esta função devolve True caso a pedra p seja do jogador branco 
    e False caso contrário.
    """
    if p == cria_pedra_branca():
        return True
    else:
        return False

def eh_pedra_preta(p):
    """
    eh pedra preta: pedra → booleano
    Esta função devolve True caso a pedra p seja do jogador preto 
    e False caso contrário.
    """
    if p == cria_pedra_preta():
        return True
    else:
        return False

def pedras_iguais(p1, p2):
    """
    pedras iguais: universal x universal → booleano
    Esta função devolve True apenas se p1 e p2 forem pedras e iguais.
    """
    if eh_pedra(p1) and eh_pedra(p2) and p1==p2:
        return True
    else:
        return False

def pedra_para_str(p):
    """
    pedra para str : pedra → str
    Esta função devolve a cadeia de caracteres que representa o jogador dono da pedra, 
    isto é, 'O', 'X' ou '.' para pedras do jogador branco, preto ou neutra respetivamente.
    """
    if eh_pedra_branca(p):
        return 'O'
    elif eh_pedra_preta(p):
        return 'X'
    else:
        return '.'

def eh_pedra_jogador(p):
    """
    eh pedra jogador : pedra → booleano
    Esta função devolve True caso a pedra p seja de um jogador 
    e False caso contrário.
    """
    return eh_pedra_branca(p) or eh_pedra_preta(p)

def cria_goban_vazio(n):
    """
    cria goban vazio: int → goban
    Esta função devolve um goban de tamanho nxn, sem interseções ocupadas. 
    """
    if type(n)!=int or (n!=9 and n!=13 and n!=19):
        raise ValueError('cria_goban_vazio: argumento invalido')

    indices_de_linhas_e_colunas= list(range(n))
    letras= []
    numeros= []
    lista_do_goban=[]
    #Adiciona-se à lista inicial vazia as letras e os números.
    for indice in indices_de_linhas_e_colunas:
        letras+= [chr(indice+65)]
        numeros+= [indice+1]
    #As letras e os números são percorridos e as intersecoes vão sendo adicionadas à lista final.
    #A identificação será um ponto, pois o goban será vazio.
    for letra in letras:
        for numero in numeros:
            lista_do_goban += [[(letra, numero), cria_pedra_neutra()]]
    return lista_do_goban

def cria_goban(n, ib, ip):
    """
    cria goban: int x tuplo x tuplo → goban
    Esta função devolve um goban de tamanho n x n, com as interseções do tuplo ib 
    ocupadas por pedras brancas e as interseções do tuplo ip ocupadas por pedras pretas.
    """
    if type(ib)!=tuple or type(ip)!=tuple or len(ib) != len(set(ib)) or len(ip) != len(set(ip)) or type(n)!=int or (n != 9 and n != 13 and n != 19):
        raise ValueError('cria_goban: argumentos invalidos')

    for intersecao in ip:
        for intersecao2 in ib:
            if intersecoes_iguais(intersecao,intersecao2):
                raise ValueError('cria_goban: argumentos invalidos')
    #Se as interseções estiverem no tuplo das pedras brancas(ib) será colocada uma pedra branca no local indicado.
    goban_final=cria_goban_vazio(n)
    for intersecao in ib:
        if not eh_intersecao_valida(goban_final,intersecao):
            raise ValueError('cria_goban: argumentos invalidos')
        else:
            coloca_pedra(goban_final, intersecao, cria_pedra_branca())
    #Se as interseções estiverem no tuplo das pedras pretas(ip) será colocada uma pedra preta no local indicado.
    for intersecao2 in ip:
        if not eh_intersecao_valida(goban_final,intersecao2):
            raise ValueError('cria_goban: argumentos invalidos')
        else:
            coloca_pedra(goban_final, intersecao2, cria_pedra_preta())
    return goban_final

def cria_copia_goban(t):
    """
    cria copia goban: goban → goban
    Esta função recebe um goban e devolve uma cópia do goban.
    """
    copia_do_goban=[]
    for sublista in t:
        copia_do_goban+=[[sublista[0], sublista[1]]]
    return copia_do_goban

def obtem_ultima_intersecao(g):
    """
    obtem ultima intersecao: goban → intersecao
    Esta função devolve a interseção que corresponde ao canto superior direito do goban g.
    """
    return g[len(g)-1][0]

def obtem_pedra(g, i):
    """
    obtem pedra: goban x intersecao → pedra
    Esta função devolve a pedra na interseção i do goban g.
    Se a posição não estiver ocupada, devolve uma pedra neutra.
    """
    for sublista in g:
        if intersecoes_iguais(sublista[0], i):
            return sublista[1]

def obtem_cadeia(g,i):
    """
    obtem cadeia: goban x intersecao → tuplo
    Esta função devolve o tuplo formado pelas interseções (em ordem de leitura) das pedras da cadeia que passa pela interseção i. 
    Caso a posição não esteja ocupada, devolve a cadeia de posições livres.
    """
    tuplo_final = (i,)  #Tuplo criado para armazenar o resultado final ao longo do ciclo.
    valor = obtem_pedra(g, i)
    lista_temporaria = [i] #É criada uma lista com o elemento inicial, onde vão ser armazenadas as interseções que ainda não estejam no tuplo final e que sejam iguais à interseção dada (livre ou ocupada).

    while len(lista_temporaria) != 0:  #O ciclo vai correr enquanto não estiver vazio. O mesmo vai percorrer as interseções e verificar se as mesmas se encontram na cadeia.
        for intersecao_da_lista in lista_temporaria:
            for intersecao in obtem_intersecoes_adjacentes(intersecao_da_lista, obtem_ultima_intersecao(g)):
                if intersecao not in tuplo_final and pedras_iguais(obtem_pedra(g, intersecao), valor):
                    lista_temporaria.append(intersecao)
                    tuplo_final += (intersecao,)
            lista_temporaria.remove(intersecao_da_lista)  #O elemento atual da lista é sempre removido para que o ciclo eventualmente acabe.
    if len(tuplo_final) == 1:  #Condição para verificar que se o tuplo final tiver apenas uma interseção, a função devolverá apenas essa interseção.
        return (i,)
    return tuple(ordena_intersecoes(tuplo_final))

def coloca_pedra(g, i, p):
    """
    coloca pedra: goban x intersecao x pedra → goban
    Esta função modifica destrutivamente o goban g colocando a pedra do jogador 
    p na interseção i, e devolve o próprio goban.
    """
    #De sublista em sublista do goban, verifica-se se a interseção dada é igual à que se encontra na sublista.
    #Após essa verificação, é alterado o símbolo que identifica a cor da pedra.
    for sublista in g:
        if intersecoes_iguais(i, sublista[0]):
            sublista[1] = p
    return g           

def remove_pedra(g, i):
    """
    remove pedra: goban x intersecao → goban
    Esta função modifica destrutivamente o goban g removendo 
    a pedra da interseção i, e devolve o próprio goban.
    """
    #De sublista em sublista do goban(a partir do indice de cada sublista), verifica-se se a interseção dada é igual à que se encontra na sublista.
    #Após essa verificação, altera-se o símbolo que identifica a cor da pedra para um ponto, que indica que a interseção é livre.
    for index in range(len(g)):
        sublista=g[index]
        if intersecoes_iguais(i, sublista[0]):
            g[index][1] = '.'
    return g

def remove_cadeia(g, t):
    """
    remove cadeia: goban x tuplo → goban
    Esta função modifica destrutivamente o goban g removendo a
    s pedras nas interseções do tuplo t, e devolve o próprio goban.
    """
    #As interseções do tuplo t são percorridas e a pedra de cada uma é removida no goban g.
    for intersecao in t:
        remove_pedra(g, intersecao)
    return g

def eh_goban(arg):
    """
    eh goban: universal → booleano
    Esta função devolve True caso o seu argumento seja um TAD goban e False caso contrário.
    """
    #Verificar se o argumento é uma lista e o seu comprimento correspondente à sua dimensão.
    if not isinstance(arg, list) or (len(arg)!=9*9 and len(arg)!=13*13 and len(arg)!=19*19):
        return False
    #Percorre-se o goban de sublista em sublista.
    for sublista in arg:
        #Verifica-se se cada sublista tem dois elementos(uma interseção e um símbolo).
        if len(sublista) != 2:
            return False  
        #Verifica-se se o primeiro elemento da sublista é uma interseção.
        elif not eh_intersecao(sublista[0]):
            return False
        #Verifica-se se o segundo elemento da sublista é um símbolo válido.
        elif not eh_pedra(obtem_pedra(arg, sublista[0])):
            return False
        #Verifica-se que o goban será quadrangular, ou seja, que seria 9x9, 13x13 ou 19x19 e não 9x13 por exemplo.
        elif ord(obtem_col(obtem_ultima_intersecao(arg)))-64 != obtem_lin(obtem_ultima_intersecao(arg)):
            return False
    return True

def eh_intersecao_valida(g, i):
    """
    eh intersecao valida: goban x intersecao → booleano
    Esta função devolve True se i é uma interseção válida dentro
    do goban g e False caso contrário
    """
    #Verifica-se se a interseção é realmente uma interseção.
    if not eh_intersecao(i):
        return False
    #Verifica-se que as colunas e as linhas se encontram dentro dos limites do goban.
    if ord(obtem_col(i)) > ord(obtem_col(obtem_ultima_intersecao(g))):
        return False
    elif obtem_lin(i) > obtem_lin(obtem_ultima_intersecao(g)):
        return False
    #Se todas as condições se verificarem a função devolve True.
    return True

def gobans_iguais(g1, g2):
    """
    gobans iguais: universal x universal → booleano
    Esta função devolve True apenas se g1 e g2 forem gobans e se forem iguais.
    """
    #Verifica-se se g1 e g2 são gobans e se têm o mesmo tamanho.
    if not eh_goban(g1) or not eh_goban(g2):
        return False
    if len(g1) != len(g2):
        return False
    #verifica-se se as sublistas são todas iguais.
    for sublista in g1:
        letra= sublista[0][0]
        linha= sublista[0][1]
        intersecao=cria_intersecao(letra, linha)
        pedra1=obtem_pedra(g1, intersecao)
        pedra2=obtem_pedra(g2, intersecao)
        if not pedras_iguais(pedra1, pedra2):
            return False
    #Se todas as condições se verificarem a função devolve True.
    return True

def goban_para_str(g):
    """
    goban_para_str: goban -> str
    Esta função retorna uma representação em string do goban.
    """
    n = obtem_lin(obtem_ultima_intersecao(g))
    indices_de_linhas_e_colunas = tuple(range(n))
    primeira_linha = '  '  #Inicia-se a tabela e vai-se adicionando todas as letras.
    ultima_linha = '  '  #Inicia-se a ultima linha e vai-se adicionando todas as letras da ultima linha.
    resto_da_tabela = ''  #Inicia-se a parte do meio da tabela onde vai-se adicionando as peças.
    pecas_brancas=()
    pecas_pretas=()
    pecas_neutras=()
    #São criados tuplos e neles são armazenadas as interseções consoante sejam pretas, brancas ou neutras.
    for sublista in g:
        if pedras_iguais(sublista[1], cria_pedra_branca()):
            pecas_brancas+= (sublista[0],)
        elif pedras_iguais(sublista[1], cria_pedra_preta()):
            pecas_pretas+= (sublista[0],)
        else:
            pecas_neutras+= (sublista[0],)
    #Percorre-se o tuplo de coluna a coluna, adicionando-se sempre um espaço e uma letra.
    for coluna in range(len(indices_de_linhas_e_colunas)):
        primeira_linha += ' ' + chr(coluna + 65)
    #Troca-se de linha.
    primeira_linha += '\n'
    while n > 0:
        # Verifica-se o numero de dígitos de um número e caso o número tenha apenas um dígito acrescenta-se um espaço inicialmente(objetivo: alinhar a tabela).
        if len(str(n)) < 2:
            resto_da_tabela += ' ' + f'{n}'
        else:
            resto_da_tabela += f'{n}'
        #acrescentamos as interseções consoante sejam locais de pedras brancas, pretas ou livres.
        for elemento in indices_de_linhas_e_colunas:
            if (chr(elemento+65), n) in pecas_brancas:
                resto_da_tabela += ' O'
            elif (chr(elemento+65), n) in pecas_pretas:
                resto_da_tabela += ' X'
            elif (chr(elemento+65), n) in pecas_neutras:
                resto_da_tabela += ' .'
        #No final de cada linha da tabela é necessário acrescentar um espaço antes de um número com um dígito(objetivo: alinhar a tabela).
        if len(str(n)) < 2:
            resto_da_tabela += '  ' + f'{n}' + '\n'
        else:
            resto_da_tabela += ' ' + f'{n}' + '\n'
        n -= 1
    #No final acrescenta-se uma linha com todas as letras de maneira idêntica à primeira linha.
    for coluna in range(len(indices_de_linhas_e_colunas)):
        ultima_linha += ' ' + chr(coluna + 65)
    return primeira_linha + resto_da_tabela + ultima_linha

def obtem_territorios(g):
    """
    obtem territorios: goban → tuplo
    Esta função devolve o tuplo formado pelos tuplos com as interseções de cada território de g.
    A função devolve as interseções de cada território ordenadas em ordem de leitura do tabuleiro de Go, 
    e os territórios ordenados em ordem de leitura da primeira interseção do território.
    """
    numero_de_linhas=obtem_lin(obtem_ultima_intersecao(g))
    todas_as_cadeias_vazias=() #Tuplo criado onde serão adicionados todos os territórios
    cadeia=()#Por cada interseção visitada todas as intersecoes da cadeia serão adicionadas a este tuplo. Assim, caso uma cadeia tenha mais do que uma intersecao não será necessário verificar a mesma cadeia inumeras vezes desnecessariamente.
    #As colunas e as linhas são percorridas.
    for coluna in range(numero_de_linhas):
        for linha in range(numero_de_linhas):
            intersecao=cria_intersecao(chr(coluna+65), linha+1)
            cadeia_guardada=obtem_cadeia(g, intersecao)
            #Se por cada interseção a sua pedra correspondente for neutra, se ainda não tiver sido visitada e se a mesma cadeia ainda não tiver sido verificada serão adicionadas aos respetivos tuplos.
            if pedras_iguais(obtem_pedra(g, intersecao),cria_pedra_neutra()) and intersecao not in cadeia and cadeia_guardada not in todas_as_cadeias_vazias:
                cadeia+=cadeia_guardada
                todas_as_cadeias_vazias+=(cadeia_guardada,)   #São obtidas todas as cadeias vazias existentes no goban e são armazenadas num tuplo.
    todas_as_cadeias_vazias= list(todas_as_cadeias_vazias)
    #Os territórios são ordenados pela ordem de leitura
    return tuple(sorted(todas_as_cadeias_vazias, key=lambda cadeia: (obtem_lin(cadeia[0]), obtem_col(cadeia[0]))))

def obtem_adjacentes_diferentes(g, t):
    """
    obtem adjacentes diferentes: goban x tuplo → tuplo
    Esta função devolve o tuplo ordenado formado pelas interseções adjacentes às interseções do tuplo t:
    (a) livres, se as interseções do tuplo t estão ocupadas por pedras de jogador(liberdades de uma cadeia);
    (b) ocupadas por pedras de jogador, se as interseções do tuplo t estão livres(fronteira de um territorio).
    """
    #Percorre-se o goban de sublista em sublista.
    tuplo_final=()
    intersecao_maxima= obtem_ultima_intersecao(g)
    for intersecao in t:  
        #Caso a interseção seja vazia, as interseções adjacentes ocupadas(quer sejam peças brancas ou pretas) vão ser adicionadas à resposta final.
        for adjacente in obtem_intersecoes_adjacentes(intersecao, intersecao_maxima):
            if pedras_iguais(obtem_pedra(g, intersecao),cria_pedra_neutra()):
                if not pedras_iguais(obtem_pedra(g, adjacente),cria_pedra_neutra()) and adjacente not in tuplo_final:
                    tuplo_final+= (adjacente,)
            #Caso a interseção seja ocupada, as interseções adjacentes vazias vão ser adicionadas à resposta final.
            else:
                if pedras_iguais(obtem_pedra(g, adjacente),cria_pedra_neutra()) and adjacente not in tuplo_final:
                    tuplo_final+=(adjacente,)
    return tuple(ordena_intersecoes(tuplo_final))

def jogada(g, i, p):
    """
    jogada: goban x intersecao x pedra → goban
    Esta função modifica destrutivamente o goban g colocando a pedra de jogador p na interseção i e remove
    todas as pedras do jogador contrário pertencentes a cadeias adjacentes à i sem liberdades, devolvendo o próprio goban.
    """
    #A pedra nova é colocada.
    coloca_pedra(g, i, p)
    for adjacente in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
        #As adjacentes com pedras diferentes são obtidas.
        if not pedras_iguais(obtem_pedra(g, adjacente),cria_pedra_neutra()) and not pedras_iguais(p,obtem_pedra(g,adjacente)):
            #As cadeias das pedras diferentes e adjacentes são obtidas.
            cadeias_de_pedras_adjacentes= obtem_cadeia(g, adjacente)
            #Se cada cadeia não tiver liberdades significa que a cadeia está rodeada.
            numero_de_liberdades=obtem_adjacentes_diferentes(g, cadeias_de_pedras_adjacentes)
            #Se o tuplo devolvido for vazio significa que existem zero liberdades, ou seja, é possível remover a cadeia.
            if len(numero_de_liberdades)==0:
                g=remove_cadeia(g, cadeias_de_pedras_adjacentes)
    return g

def obtem_pedras_jogadores(g):
    """
    obtem pedras jogadores: goban → tuplo
    Esta função devolve um tuplo de dois inteiros que correspondem ao 
    número de interseções ocupadas por pedras do jogador branco e preto, respetivamente.
    """
    numero_pedras_brancas=0
    numero_pedras_pretas=0
    #Percorre-se o goban e por cada peça preta ou branca encontrada adiciona-se uma unidade a um contador.
    for sublista in g:
        if pedras_iguais(sublista[1],cria_pedra_preta()):
            numero_pedras_pretas+=1
        elif pedras_iguais(sublista[1],cria_pedra_branca()):
            numero_pedras_brancas+=1
    return (numero_pedras_brancas, numero_pedras_pretas)

def calcula_pontos(g):
    """
    calcula pontos: goban → tuple
    Esta função é auxiliar. A mesma recebe um goban e devolve o tuplo de dois
    inteiros com as pontuações dos jogadores branco e preto, respetivamente.
    """
    #Pontos iniciais(numeros de peças em jogo).
    numero_de_pontos_brancos=obtem_pedras_jogadores(g)[0]
    numero_de_pontos_pretos=obtem_pedras_jogadores(g)[1]
    #Os territórios são percorridos.
    for territorio in obtem_territorios(g):
        intersecoes_brancas=()
        #A fronteira do território é percorrida.
        for intersecao_da_fronteira in obtem_adjacentes_diferentes(g, territorio):
            intersecoes_brancas+=(eh_pedra_branca(obtem_pedra(g, intersecao_da_fronteira)),)
        #Se a fronteira do território for constituída apenas por peças brancas, o mesmo pertencerá ao jogador das peças brancas.
        #Caso contrário o território pertencerá ao jogador das peças pretas.
        if all(intersecoes_brancas) and len(intersecoes_brancas)>0:
            numero_de_pontos_brancos+=len(territorio)
        elif not any(intersecoes_brancas) and len(intersecoes_brancas)>0:
            numero_de_pontos_pretos+=len(territorio)
    return (numero_de_pontos_brancos, numero_de_pontos_pretos)

def eh_jogada_legal(g, i, p, l):
    """
    eh jogada legal: goban x intersecao x pedra x goban → booleano
    Esta função é auxiliar. A mesma recebe um goban (g), uma interseção(i), uma pedra de jogador(p) 
    e um outro goban (l) e devolve True se a jogada for legal ou False caso contrário, sem modificar g ou l.
    As jogadas ilegais são suicídio(se uma ou mais pedras da cor daquele jogador ficarem sem liberdades após a resolução da jogada)
    e repetição(ko)(se uma jogada tiver o efeito de criar um estado do tabuleiro que ocorreu anteriormente no jogo)
    """
    copia_do_goban=cria_copia_goban(g)
    #Se a interseção i não for válida ou já tiver uma pedra, não será possível colocar uma nova pedra.
    if not eh_intersecao_valida(g, i) or eh_pedra_jogador(obtem_pedra(g,i)):
        return False
    #Se a cadeia da nova pedra que foi colocada não tiver liberdades será suicídio.
    jogada(copia_do_goban, i, p)
    cadeia=obtem_cadeia(copia_do_goban, i)
    adjacentes = obtem_adjacentes_diferentes(copia_do_goban, cadeia)
    #Verificar se todas as pedras vizinhas são do adversário
    if len(adjacentes)==0:
        return False
    #Se o primeiro goban for igual a l, a função retorna False (caso de repetição).
    if gobans_iguais(copia_do_goban, l):
        return False
    return True

def turno_jogador(g, p, l):
    try:
        variavel=True
        while True:
            input_do_jogador= input("Escreva uma intersecao ou 'P' para passar [{}]:".format(pedra_para_str(p)))
            #Se o jogador digitar 'P' está a passar então a função devolve False.
            if input_do_jogador == 'P':
                return False
            #Caso o jogador digite uma interseção válida, a jogada será realizada, sendo que a mesma deve ser convertida de string para uma interseção em forma de tuplo.
            elif (len(input_do_jogador)==2 or len(input_do_jogador)==3) and eh_intersecao_valida(g, str_para_intersecao(input_do_jogador)) and 0<=ord(input_do_jogador[0])-65<=18 and 1<=int(input_do_jogador[1:])<=19 and eh_jogada_legal(g, str_para_intersecao(input_do_jogador), p, l):
                intersecao= str_para_intersecao(input_do_jogador)
                jogada(g, intersecao, p)
                return True
    except(ValueError):
        variavel=True

def go(n, tb, tp):
    """
    go: int x tuple x tuple → booleano 
    Esta é a função principal que permite jogar um jogo completo do Go de doisjogadores. 
    A mesma recebe um inteiro (n) correspondente à dimensão do tabuleiro, e dois tuplos
    (potencialmente vazios) com a representação externa das interseções ocupadas
    por pedras brancas (tb) e pretas (tp) inicialmente. 
    O jogo termina quando os dois jogadores passam a vez de jogar consecutivamente. 
    A função devolve True se o jogador com pedras brancas conseguir ganhar o jogo, ou False caso contrário. 
    """
    if type(n)!=int or (n != 9 and n != 13 and n != 19) or type(tb)!=tuple or type(tp)!= tuple:
        raise ValueError('go: argumentos invalidos') 
    tuplo_pretas=()
    tuplo_brancas=()
    goban_teste=cria_goban_vazio(n)
    for intersecao in tp:
        try:
            intersecao1=str_para_intersecao(intersecao)
        except ValueError:
            raise ValueError('go: argumentos invalidos')
        else:
            if eh_intersecao_valida(goban_teste,intersecao1):
                tuplo_pretas+= (intersecao1,)
    for intersecao2 in tb:
        try:
            intersecao3=str_para_intersecao(intersecao2)
        except ValueError:
            raise ValueError('go: argumentos invalidos')
        else:
            if eh_intersecao_valida(goban_teste,intersecao3):
                tuplo_brancas+= (intersecao3,)

    pedra=cria_pedra_preta()
    passar=0        #Este contador serve para calcular o numero de vezes que os dois jogadores passam(se passarem os dois significa que o jogo acaba).

    goban=cria_goban(n, tuplo_brancas, tuplo_pretas)
    while passar<2:     #O valor do contador ser igual a 2 significa que os dois jogadores passaram consecutivamente, ou seja, o jogo acaba.
        goban_anterior=cria_copia_goban(goban)
        pontuacao= calcula_pontos(goban)
        print(f'Branco (O) tem {pontuacao[0]} pontos')
        print(f'Preto (X) tem {pontuacao[1]} pontos')
        print(goban_para_str(goban))
        input_do_jogador= turno_jogador(goban,pedra, goban_anterior)
        if input_do_jogador==False:
            passar+=1
        else:
            passar=0

        if pedras_iguais(pedra, cria_pedra_preta()):
            pedra= cria_pedra_branca()
        else:
            pedra=cria_pedra_preta()

    pontuacao_final= calcula_pontos(goban)
    branco= pontuacao_final[0]
    preto= pontuacao_final[1]
    print(f'Branco (O) tem {branco} pontos')
    print(f'Preto (X) tem {preto} pontos')
    print(goban_para_str(goban))
    return branco >= preto