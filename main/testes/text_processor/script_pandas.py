import pandas as pd

listas_de_bolas = []


def processando_textos():
    global listas_de_bolas

    # Ler o arquivo CSV com a codificação correta
    df = pd.read_csv('/home/uroot/ws-mega-sena/testes/jogos_site_loterias/Mega-Sena.csv', encoding='latin1')

    # Selecionar as colunas Bola1 até Bola6
    bolas = df[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6']]

    # Gerar uma variável em forma de lista para cada linha do CSV
    listas_de_bolas = bolas.values.tolist()

    # Salvar as colunas selecionadas em um novo arquivo CSV
    bolas.to_csv('/home/uroot/ws-mega-sena/testes/jogos_site_loterias/bolas_selecionadas.csv', index=False)

    print("Os valores das colunas Bola1 até Bola6 foram salvos no arquivo 'bolas_selecionadas.csv'.")


def return_jogos_in_list():
    global listas_de_bolas
    processando_textos()
    return listas_de_bolas

processando_textos()
print(listas_de_bolas)