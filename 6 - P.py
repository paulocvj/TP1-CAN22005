import math
from numpy import pi

def f(P,            # Valor a se calcular 
      Irms = 1.1292,# Irms calculado por bissecção          
      Vm = 50,      # Vm apresentado no problema
      R = 40,       # Resistência
      L = 0.3,      # Indutância
      omega = 377): # Omega = 2*pi*f = 2*pi*60 = 377

    return ((Irms**2) * R) - P

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

resp = bisseccao(45, 55)
try:
    print(f'raíz aprox {resp["hp"]:.4f}')
    print(f'O número de iterações foi {resp["iteração"]}')
except:
    print('Raiz não encontrada')