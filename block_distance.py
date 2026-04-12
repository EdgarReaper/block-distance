import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import random


# Função Principal
def solucao(blocos, auto_fechar = False):
    # Verifica se todos os números são positivos
    if any(b < 0 for b in blocos):
        return "Erro: a lista deve conter apenas números positivos"
    
    tempo_inicio = time.time()

    n = len(blocos)
    max_distancia = 0
    melhor_esquerda = 0
    melhor_direita = 0
    melhor_inicio = 0
    
    for inicio in range(n):
        esquerda = inicio
        while esquerda > 0 and blocos[esquerda - 1] >= blocos[esquerda]:
            esquerda = esquerda - 1

        direita = inicio
        while direita < n - 1 and blocos[direita + 1] >= blocos[direita]:
            direita = direita + 1

        distancia = direita - esquerda
        if distancia > max_distancia:
            max_distancia = distancia
            melhor_esquerda = esquerda
            melhor_direita = direita
            melhor_inicio = inicio
            
    tempo_fim = time.time()
    tempo = f"{tempo_fim - tempo_inicio:.8f}"

    # Gráfico
    cores = ['steelblue'] * n
    cores[melhor_esquerda] = 'green'
    cores[melhor_direita] = 'green'
    cores[melhor_inicio] = 'yellow'
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(range(n), blocos, color=cores, edgecolor='black')

    # Sapos em cima das barras
    ax.plot(melhor_esquerda, blocos[melhor_esquerda] + 0.3, 'go', markersize=15, label='Sapo 1')
    ax.plot(melhor_direita, blocos[melhor_direita] + 0.3, 'rs', markersize=15, label='Sapo 2')
    
    # Seta com a distância
    margem = (max(blocos) - min(blocos)) * 0.2 + 1
    altura_seta = max(blocos) + margem

    if melhor_esquerda != melhor_direita:
        ax.annotate('', xy=(melhor_direita, altura_seta),
                        xytext=(melhor_esquerda, altura_seta),
                        arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        ax.text((melhor_esquerda + melhor_direita) / 2, altura_seta + margem * 0.5,
                f'Distância: {max_distancia}', ha='center', fontsize=12, color='red')
    
    if melhor_inicio == melhor_esquerda or melhor_inicio == melhor_direita:
        label_amarelo = 'Bloco inicial (coincide com posição final)'
    else:
        label_amarelo = 'Bloco inicial'

    ax.set_ylim(0, max(blocos) * 1.6 + 1)
    ax.set_xticks(range(n))
    ax.set_xlabel('Índice do bloco')
    ax.set_ylabel('Altura')
    ax.set_title(f'Distância Máxima: {max_distancia} | Tempo de Execução: {tempo}s')
    patch_verde = mpatches.Patch(color='green', label='Posição final dos sapos')
    patch_amarelo = mpatches.Patch(color='yellow', label=label_amarelo)
    patch_azul = mpatches.Patch(color='steelblue', label='Blocos neutros')
    sapo1 = mlines.Line2D([], [], color='green', marker='o', linestyle='None', markersize=10, label='Sapo 1')
    sapo2 = mlines.Line2D([], [], color='red', marker='s', linestyle='None', markersize=10, label='Sapo 2')
    ax.legend(handles=[patch_verde, patch_amarelo, patch_azul, sapo1, sapo2])    
    plt.tight_layout()
    if auto_fechar:
        plt.show(block=False)
        plt.pause(5)
        plt.close()
    else:
        plt.show()

    return f"Distância Máxima: {max_distancia}, Tempo de Execução: {tempo} segundos"


''' Testes
solucao([2, 6, 8, 5])
solucao([1, 5, 5, 2, 6])
solucao([3, 5, 7, 2])
solucao([100, 2, 25, 75, 34, 54])
solucao([2, 6, 4, 9, 0])
solucao([24, 63, 36, 48])
solucao([2,6,-7,9,3]) # erro'''


# Funções Auxiliares
def testar_manualmente():
    lista = []
            
    print("Adicione números à lista um a um. Escreva 'fim' quando terminar.")
            
    while True:
        entrada = input("Número: ")
                
        if entrada.lower() == "fim":
            if len(lista) == 0:
                print("Erro: a lista está vazia!\n")
            elif len(lista) == 1:
                print("Erro: a lista deve ter pelo menos 2 blocos!\n")
            else:
                break
        else:  
            try:
                n = int(entrada)
                if n < 0:
                    print("Erro: a lista deve conter apenas números positivos")
                else:
                    lista.append(n)
                    print(f"Lista atual: {lista}")
            except ValueError:
                print("Erro: introduza um número inteiro ou 'fim' para terminar")
                
    solucao(lista)
  
    
def testar_aleatoria():
    try:
        n = int(input("Quantos blocos quer gerar? (mínimo 2): "))
        if n < 2:
            print("Erro: o número de blocos deve ser pelo menos 2!")
            return
        altura_max = int(input("Altura máxima dos blocos: "))
        if altura_max < 1:
            print("Erro: a altura máxima deve ser pelo menos 1!")
            return
    except ValueError:
        print("Erro: introduza um número inteiro válido")
        return

    lista = [random.randint(0, altura_max) for _ in range(n)]
    print(f"Lista gerada aleatoriamente: {lista}")
    solucao(lista)


def testar_predefinidas():
    while True:
        print("\n Listas predefinidas que pode testar:\n", "1) [2, 6, 8, 5]\n", 
              "2) [1, 5, 5, 2, 6]\n", "3) [100, 2, 25, 75, 34, 54, 175, 4, 480, 348, 5]\n",
              "4) [3, 0, 123, 75, 34, 96]\n", "5) [24, 63, 3, 643, 263, 346, 12]\n", 
              "6) [0, 1, 0, 50, 51, 52, 1, 2, 3, 0, 100, 200, 150, 0, 1]\n",
              "7) [2, 1, 0, 5, 3, 2, 0, 8, 9, 10, 6, 4, 1, 0, 15, 20, 25, 10, 3, 1]\n",
              "0) Voltar Atrás")
    
        entrar = input("Opção: ")
        
        try:
            op = int(entrar)
            if op == 1:
                solucao([2, 6, 8, 5])
            elif op == 2:
                solucao([1, 5, 5, 2, 6])
            elif op == 3:
                solucao([100, 2, 25, 75, 34, 54, 175, 4, 480, 348, 5])
            elif op == 4:
                solucao([3, 0, 123, 75, 34, 96])
            elif op == 5:
                solucao([24, 63, 3, 643, 263, 346, 12])
            elif op == 6:
                solucao([0, 1, 0, 50, 51, 52, 1, 2, 3, 0, 100, 200, 150, 0, 1])
            elif op == 7:
                solucao([2, 1, 0, 5, 3, 2, 0, 8, 9, 10, 6, 4, 1, 0, 15, 20, 25, 10, 3, 1])
            elif op == 0:
                print("A voltar atrás...")
                break
            else:
                print("Erro: introduza uma das opções disponíveis ou 0 para terminar")
                
        except ValueError:
            print("Erro: introduza uma das opções disponíveis ou 0 para terminar")


# Menu
def menu():
    print("Bem-vindo ao Jogo dos Sapos")
    while True:
        
        print("\n 1) Teste com números positivos\n", "2) Teste com números aleatórios\n", 
              "3) Listas predefinidas\n","0) Fechar Jogo")
        
        comeca = input("Opção: ")
            
        try:
            opcao = int(comeca)
            if opcao == 1:
                testar_manualmente()
                        
            elif opcao == 2:
                testar_aleatoria()
                    
            elif opcao == 3:
                testar_predefinidas()
                        
            elif opcao == 0:
                print("Saiu do Jogo!")
                return False
            
            else:
                print("Erro: introduza uma das opções disponíveis ou 0 para terminar")
                
        except ValueError:
            print("Erro: introduza uma das opções disponíveis ou 0 para terminar")
            

def run():
    menu()

if __name__ == "__main__":
    run()

