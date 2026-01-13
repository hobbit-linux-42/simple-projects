import numpy as np
import matplotlib.pyplot as plt
import math

def cauchy(lam:float):
    return 1.323 + (3.32e-3)/(lam**2) - (3.26e-5)/(lam**4)

def cherenkov(lam: float, beta: float, n: float, charge = 1):
    ALPHA = 1.0 / 137.036
    if beta*n <= 1:
        return 0
    else:
            efficiency = 1 - 1/(beta*n)**2
            yield_val = (2*np.pi*ALPHA* charge**2)/(lam**2) * efficiency 
            return yield_val/1e7

def angle(n:float, beta:float):
    cos=1/(n*beta)
    return math.acos(cos)
    
def main(beta: float):
    print(angle(1.33, beta))
    x = list(range(50, 600))
    cherenkov_y=[]
    for i in x: 
        n = cauchy(i* 1e-3)
        cherenkov_y.append(cherenkov(i* 1e-7, beta, n))
    plt.plot(x, cherenkov_y)
    plt.xticks(list(range(50, 650, 50)))
    plt.xlabel("wave lenght [nm]")
    plt.ylabel("photons/cm")
    plt.axvspan(0, 200, alpha=0.2, color='orange', label='water absorption band')
    plt.axvline(x[cherenkov_y.index(max(cherenkov_y))], color='red', 
        linestyle='--', linewidth=1, alpha=0.8, label="peak")
    plt.legend()
    plt.show()
    
    
if __name__ == "__main__":
    beta = float(input("particle speed [v/c]: "))
    main(beta)
