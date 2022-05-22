import math
from numpy import pi

def f(Irms,         # Valor a se calcular 
      V2 = 30.0106, # V2 calculado por bissecção          
      V4 = 6.0021,  # V4 calculado por bissecção
      V0 = 45.0158, # Tensão média aparente na fonte
      R = 40,       # Resistência
      L = 0.3,      # Indutância
      omega = 377): # Omega = 2*pi*f = 2*pi*60 = 377

    return math.sqrt((V0/R)**2+(V2/abs(R+(1j*2*omega*L))/math.sqrt(2))**2
        + (V4/abs(R+(1j*4*omega*L))/math.sqrt(2))**2) - Irms

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

resp = bisseccao(0.5, 1.5)
try:
    print(f'raíz aprox {resp["hp"]:.4f}')
    print(f'O número de iterações foi {resp["iteração"]}')
except:
    print('Raiz não encontrada')