import numpy as np
import matplotlib.pyplot as plt
N = 10000  
I = 1         
beta = 0.3
gamma = 0.05 
vaccine=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
curve=[]
for v_rate in vaccine:
    S = (1 - v_rate) * (N - I) 
    V = v_rate * N 
    I = 1
    R = 0
    S_ = [S]
    I_ = [I]
    R_ = [R]
    for t in range(1000):
        new_I=np.random.binomial(S,beta*I/N)
        new_R=np.random.binomial(I,gamma)
        S-=new_I
        R+=new_R
        I+=new_I-new_R
        S_.append(S)
        R_.append(R)
        I_.append(I)

    curve.append(I_)
plt.figure(figsize=(6,4),dpi=150)
plt.xlabel('Time')
plt.ylabel('Infected individuals')
plt.title('Effect of Vaccination')
for i, v_rate in enumerate(vaccine):
    plt.plot(curve[i], label=f'Vaccination rate: {v_rate*100:.0f}%')
plt.legend()
plt.show()
