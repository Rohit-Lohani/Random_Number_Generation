import matplotlib.pyplot as plt      # For Visualization/Demonstrating the number generation
import numpy as np                   # For storing the number in array
def pseudo_uniform_good(mult = 12345,
                   mod = (2**31)-1,
                   seed = 123456789,
                   size=1) :
    U = np.zeros(size)
    x=(seed*mult+1)%mod
    U[0] = x/mod
    for i in range(1,size) :
        x = (x*mult+1)%mod
        U[i] = x/mod
    return U

def pseudo_uniform(low=0,
                   high=1,
                   seed=123456789,
                   size=1) :
    return low+(high-low)*pseudo_uniform_good(seed=seed,size=size)

l = pseudo_uniform(low=0,high=1,size= 10000)

# For Generating second Random Number. To be used in calculating Pi
def pseudo_uniform_n(low=0,
                   high=1,
                   seed=123456700,
                   size=1) :
    return low+(high-low)*pseudo_uniform_good(seed=seed,size=size)

n = pseudo_uniform_n(low=0,high=1,size= 10000)

# Demonstrating that the number generated using visualization method

plt.hist(l,bins=50,edgecolor = 'r')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(-0.5,1.5)
plt.show()

# Predicting the value of Pi

Points_in_circle = 0
for i in range(0,10000) :
    x = l[i]
    y = n[i]

    distance = (x*x + y*y)**0.5

    if distance <= 1 :
        Points_in_circle +=1

pi = 4*Points_in_circle/10000

print(pi)

