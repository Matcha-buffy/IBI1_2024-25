import numpy as np
import matplotlib.pyplot as plt
N = 10000  
I = 1     
S = N - I  
R = 0      
beta = 0.3
gamma = 0.05 
S_=[S]
I_=[I]
R_=[R]
for t in range(1000):
    new_I=np.random.binomial(S,beta*I/N)
    new_R=np.random.binomial(I,gamma)
    S-=new_I
    R+=new_R
    I+=new_I-new_R
    S_.append(S)
    R_.append(R)
    I_.append(I)
plt.figure(figsize=(6,4),dpi=150)
plt.plot(S_, label='S', color='red')
plt.plot(I_, label='I', color='blue')
plt.plot(R_, label='R', color='green')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR Model')
plt.legend()

plt.show()
