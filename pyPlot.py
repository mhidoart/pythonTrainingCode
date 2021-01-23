import matplotlib.pyplot as plt
import sys

import numpy as np
l1 = []
for line in sys.stdin:
    row = line.split(",")
    del row[-1]
    l1.append(row)
print(l1)

for row in l1:
    plt.plot(row)
plt.show()
# #plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()
