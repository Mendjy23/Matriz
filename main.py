import numpy as np

B = np.array( [ [3, 1, 3], [6, 5, 5] ])
print('B = ',B)

C = np.array( [ [100, 50], [50, 100], [50, 50] ])
print('\nC =',C)

print('\n\n B x C', B.dot(C))
