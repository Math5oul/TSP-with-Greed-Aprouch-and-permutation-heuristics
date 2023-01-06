import time
from typing import DefaultDict

# Maior valor int possível
INT_MAX = 2147483647
 
# Algoritmo Guloso para solução inicial
def greedyTSP(tsp):
    start_time =  time.time()
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = INT_MAX
    visitedRouteList = DefaultDict(int)
 
    # A partir do 0º indexado
    visitedRouteList[0] = 1
    route = [0] * len(tsp)
 
    # Loop que percorre a matriz
    while i < len(tsp) and j < len(tsp[i]):
 
        # Fronteira da matriz
        if counter >= len(tsp[i]) - 1:
            break
 
        # Ignora o valor de visitar a si mesmo e se o valor for o  menor então atualiza a rota
        if j != i and (visitedRouteList[j] == 0):
            if tsp[i][j] < min:
                min = tsp[i][j]
                route[counter] = j + 1
            
        j += 1
 
        # Checa todos os caminhos a partir do n° ponto
        if j == len(tsp[i]):
            sum += min
            min = INT_MAX
            visitedRouteList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1
 
    # Insere o ultimo ponto a rota
    i = route[counter - 1] - 1
 
    for j in range(len(tsp)):
 
        if (i != j) and tsp[i][j] < min:
            min = tsp[i][j]
            route[counter] = j + 1
    
    sum += min
    
    exec_time =  time.time() - start_time
    print("Algoritmo Guloso")
    print("Custo do caminho:", sum)
    print(route)
    print("Tempo de Execução da Busca Gulosa:", exec_time,"s")
    return(route)
 
 
# Função para calcular o custo do caminho dado
def sumPath(route, data):
    i = 0
    j = 0
    sum = 0
    while i < len(route):
        sum += data[route[i]-1][j]
        j = route[i]-1
        i += 1
    return(sum)

# Simples swap
def swap(arr,i,j):
    aux      = arr[i]
    arr[i] = arr[j]  
    arr[j] = aux

# Checa se um nó estaria visitando a si mesmo
def isThereNoSelfVisit(arr):
    i = 0
    while i < len(arr):
        if i == arr[i]-1:
            return(False)
        i += 1
    return(True)

def localSearch(arr, data):
    start_time =  time.time()
    
    best = arr.copy()
    test = arr.copy()
    bestValue = sumPath(best, data)
    testValue = INT_MAX
    i = 0
    # Loop para todas as permutações possíveis 
    while i < len(route):
        j = i + 1
        while j < len(arr):
            # Checa se um nó estaria visitando a si mesmo caso swap
            if i != test[j]-1 and j != test[i]-1:
                swap(test,i,j)

            testValue = sumPath(test, data)
            # Atualiza os Valores
            if testValue < bestValue:
                best = test.copy()
                bestValue = testValue
            j +=1
        i += 1
    exec_time =  time.time() - start_time
    print("Tempo de Execução da Busca Local",exec_time)
    return(best)

 # instância do problema

tsp =  [[0, 11, 86, 83, 78, 52, 67, 11, 21, 10],
        [11, 0, 54, 63, 19, 24, 75, 58, 69, 33],
        [86, 54, 0, 28, 22, 46, 49, 11, 75, 38],
        [83, 63, 28, 0, 65, 55, 14, 33, 52, 19],
        [78, 19, 22, 65, 0, 19, 82, 34, 13, 34],
        [52, 24, 46, 55, 19, 0, 21, 50, 44, 17],
        [67, 75, 49, 14, 82, 21, 0, 42, 51, 72],
        [11, 58, 11, 33, 34, 50, 42, 0, 55, 48],
        [21, 69, 75, 52, 13, 44, 51, 55, 0, 37],
        [10, 33, 38, 19, 34, 17, 72, 48, 37, 0]]

route=greedyTSP(tsp)
route=localSearch(route, tsp)
print("Rota após busca local", route)
print("Custo após a busca por permutação",sumPath(route, tsp))