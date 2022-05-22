import math
from numpy import pi

def f(V2,          # Valor a se calcular 
      V0 = 45.0158, # Tensão média aparente na fonte
      R = 40,       # Resistência
      L = 0.3,      # Indutância
      omega = 377): # Omega = 2*pi*f = 2*pi*60 = 377

    return V0*(1/1-1/3)-V2 

def bisseccao(x1,  # x1 início do intervalo
              x2,  # x2 fim do intervalo
              TOL = 0.0001,  # erro tolerado
              iter=50):  # número máximo de iterações
    
    hp = (x1 + x2)/2  # Ponto médio entre os valores x1 e x2
    if f(x1) * f(x2) > 0:
        print("Nenhuma raíz encontrada.")  # nenhuma raíz.
        return 0
    else:
        c = 0  # variável contador
        ERRO = abs(f(x2) - f(x1))  # diferença entre os valores de y
        while ERRO > TOL or c > iter:  # loop iterativo com critérios de parada
            hp = (x1 + x2) / 2.0
            if f(hp) == 0:
                return [hp, c]
            elif f(x1) * f(hp) < 0:
                x2 = hp
                c += 1  # contagem
            else:
                x1 = hp
            ERRO = abs(f(x2) - f(x1))
        return {"hp": hp, "iteração": c}  # raíz da função; número de iterações

resp = bisseccao(25, 35)
try:
    print(f'raíz aprox {resp["hp"]:.4f}')
    print(f'O número de iterações foi {resp["iteração"]}')
except:
    print('Raiz não encontrada')