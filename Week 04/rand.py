#
import numpy.random as rand
import matplotlib.pyplot as plt
import numpy as np

def powerResidue(N, seed=None, a=273673163155, c=13, M=2**48):
    """ Calculate a series of random numbers
    """
    import datetime
    if seed == None:
        #print("Seed value set to NONE, defaulting to system time.")
        seed=int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    else:
        pass
    #print(seed)

    r = seed
    rand = []
    for i in range(N):
        rand.append(((a*r + c) % M)/M)
        r = (a*r + c) % M
    return rand[0:N]



print(powerResidue(5))
"""
This seems random with this setting of seed, a, c, and M
"""

print(powerResidue(5,None,6,6,6))
print(powerResidue(5,12021,4,3,5))

"""
The above are easy patterns to create using the "random" number generator. One 
produces all zeros and the other repeats 0.4 and 0.2. This is because, for the first one, 
the values for a, c, and M are all the same so the modulus is not going to have a remainder, and
for the second one the numbers for a and c are so small that the remainder is easily repeatable.
"""

plt.plot(powerResidue(100,12412412), "r")
plt.plot(powerResidue(100,None), "b")
plt.plot(powerResidue(100,1241345345), "g")

plt.xlabel("N")
plt.ylabel("random")
plt.show()
    

