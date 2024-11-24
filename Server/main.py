import numpy as np

## Variáveis Globais
MAZE_PATH = 'Server/Matrizes'

## Variáveis especificadas no problema
erro = 1e-4


def readCSV(path):
    with open(path, 'r') as file:
        fileLines = file.readlines()
        data = []
        for line in fileLines:
            data.append([float(x) for x in line.strip().split(',')])
        return np.array(data)

Maze_60x60 = readCSV(f"{MAZE_PATH}/H-1-60x60.csv")
#Maze_30x30 = readCSV(f"{MAZE_PATH}/H_30x30.csv")

##_____________________________________________________

import random

def generate_random_id():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for i in range(12))

print(generate_random_id())
