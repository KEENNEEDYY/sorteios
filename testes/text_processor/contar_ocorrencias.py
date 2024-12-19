from collections import Counter
import script_pandas

def contar_repeticoes(listas):
    # Achatar a lista de listas em uma única lista
    todos_numeros = [num for sublist in listas for num in sublist]
    
    # Contar as ocorrências de cada número
    contagem = Counter(todos_numeros)
    
    # Imprimir a contagem de cada número em ordem crescente
    for numero in range(1, 61):
        print(f"Número {numero} se repete {contagem[numero]} vezes")

def imprimir_e_salvar_repeticoes(listas):
    # Achatar a lista de listas em uma única lista
    todos_numeros = [num for sublist in listas for num in sublist]
    
    # Contar as ocorrências de cada número
    contagem = Counter(todos_numeros)
    
    # Imprimir o número a quantidade de vezes que ele se repete, separado por vírgula
    resultado = []
    for numero in range(1, 61):
        resultado.extend([str(numero)] * contagem[numero])
    
    resultado_str = ",".join(resultado)
    
    # Salvar o resultado em um arquivo
    with open("/home/uroot/ws-mega-sena/testes/text_processor/resultado.txt", "w") as f:
        f.write(resultado_str)

# Exemplo de uso
listas_de_numeros = script_pandas.return_jogos_in_list()

imprimir_e_salvar_repeticoes(listas_de_numeros)

# Confirmar que o resultado foi salvo
with open("/home/uroot/ws-mega-sena/testes/text_processor/resultado.txt", "r") as f:
    print(f.read())