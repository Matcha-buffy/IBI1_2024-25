# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
# Initialize parameters
N = 100
I = 1
beta = 0.3
gamma = 0.1
# Initialize the population array (0: susceptible, 1: infected, 2: recovered
population = np. zeros((100, 100))
population [4 ,12]
# Randomly select one infected individual
outbreak = np.random.choice(range(100) ,2)
population [outbreak [0],outbreak [1]] = 1
# Define a function to infect neighbors
def neighbor(population, beta):
    a = np.where(population == 1)
    for x, y in zip(a[0], a[1]):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny< N and np.random.rand() < beta :
                        population[nx,ny] = 1
# Define a function to recover individuals
def recover(population , gamma):
     b = np.where(population == 1)
     for x, y in zip(b[0], b[1]):
          if np.random.rand() < gamma:
            population[x,y] = 2
# Time course simulation for 100 time points
for t in range(100):
    neighbor(population, beta)
    recover(population, gamma)
    if t in [0, 10, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time: {t}')
        plt.colorbar()
        plt.show()