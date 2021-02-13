from pylab import *
import matplotlib.pyplot as plt
N = array([190]) # Number of particles
nstep = 5000#50000 # Number of steps
for NN in N:
    n = zeros(nstep)
    n[0] = NN # Initial number on left side
    for i in range(1,nstep):
        r = rand(1)
        if (r<n[i-1]/NN):
            n[i] = n[i-1] - 1 # Move atom from left to right
        else:
            n[i] = n[i-1] + 1 # Move atom from right to left
    plot(range(0,nstep), n/NN, label='N= '+str(NN))
    plt.legend()
plt.axhline(y=0.5, color='black', linestyle='--')
xlabel('t'),ylabel('n/N')
show()
