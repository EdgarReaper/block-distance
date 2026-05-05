from block_distance import solucao

testes = [
    # (descricao, lista, resultado_esperado)
    ("Exemplo do enunciado 1",          [2, 6, 8, 5],                                                        2),
    ("Exemplo do enunciado 2",          [1, 5, 5, 2, 6],                                                     3),
    ("Lista com valores muito grandes", [100, 2, 25, 75, 34, 54, 175, 4, 480, 348, 5],                       3),
    ("Zero no meio",                    [3, 0, 123, 75, 34, 96],                                             3),
    ("Grande variação de alturas",      [24, 63, 3, 643, 263, 346, 12],                                      2),
    ("Zeros + subida longa",            [0, 1, 0, 50, 51, 52, 1, 2, 3, 0, 100, 200, 150, 0, 1],              4),
    ("Lista longa e complexa",          [2, 1, 0, 5, 3, 2, 0, 8, 9, 10, 6, 4, 1, 0, 15, 20, 25, 10, 3, 1],   7),
]

print("RESULTADOS DOS TESTES")

passaram = 0
falharam = 0

for descricao, blocos, esperado in testes:
    print(f"\nA correr teste: {descricao}...")
    print(f"Lista: {blocos}")
    resultado = solucao(blocos, auto_fechar = True)
    
    # extrai só o numero da string "Distancia Maxima: X, Tempo..."
    distancia = int(resultado.split(":")[1].split(",")[0].strip())
    ok = distancia == esperado
    
    if ok:
        passaram = passaram + 1
        print(f"PASSOU - Esperado: {esperado} | Obtido: {distancia}")
    else:
        falharam = falharam + 1
        print(f"FALHOU - Esperado: {esperado} | Obtido: {distancia}")

print(f"\nResultado final: {passaram} passaram, {falharam} falharam")

