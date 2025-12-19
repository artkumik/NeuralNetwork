import numpy as np

input = [[0,0.4,0.9],[0.1,0.4,0.2]]
expected = [2,1]

print(np.mean(np.argmax(input)==expected))