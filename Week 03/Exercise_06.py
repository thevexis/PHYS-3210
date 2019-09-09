#Importing all necessary extensions 
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def walk(N):    #Creates a function called walk that takes an input of steps N
    """ Function to compute an N-step random walk
    
        Input:
            N  ::  Total number of steps

        Output:
            x  ::  Array of all x positions
            y  ::  Array of all y positions

    """
    # seed random number generator
    # this uses the function r_i+1 = remainder(a*r_i + c /(M)) to generate a 
    #random number sequence 
    rand.seed()

    # initialize x, y
    x = [0.0] 
    y = [0.0]

    # step in x-y space N times
    for n in range(N):    #Simple for loop to generate values for x and y
        #append puts new object into exists list. x consisted of the list [0.0]
        #but now we take the last element x[-1] and add a random number, which is between 0 and 1 then subtract 0.5 and then times 2.0
        #do this for y as well. if you don't take the last index you will always take the first index
        #which is 0.0 so when you keep adding some number to that you just fill up your graph instead of moving around
        #because you are not adding to your previous location
        
        x.append(x[-1] + (rand.random() - 0.5)*2.0)
        y.append(y[-1] + (rand.random() - 0.5)*2.0)
    
    return np.array(x), np.array(y) # end of function that returns what ever value 
#the function should have done. In this case it returns an two arrays with random numbers


# Example simulation
walker_1 = walk(1000)   # compute path for 1000 steps
#sets the function walk to a variable called walker_1 so that we can index the x and y arrays to plot

# Example plot of (x, y) pairs from example simulation 
plt.plot(walker_1[0], walker_1[1], '-') #finally we plot the x and y arrays with lines
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

for n in range(0,50):
    walker_2 = walk(1000)
    plt.plot(walker_2[0], walker_2[1], '-') 
    
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
#plt.savefig("4-Walkers")
 
"""
 We can see 4 different colored random walkers in our graph and from what I would 
 expect to be random it is very close. Randomness does not mean that valuse are not repeated, 
 there is a wonderful numberfile video on this when flipping a coin. The walker goes around
 and repeats but never in a pattern that can be discerned. On top of one walker doing this
 when four walkers are all graphed together on the same graph we can see that they are all
 rather random.
 
"""    
N = 1000
d = []

for n in range(0,100):
    walker = walk(N)
    x_walker = walker[0]
    y_walker = walker[1]
    x_displacement = x_walker[1000] - x_walker[0]
    y_displacement = y_walker[1000] - y_walker[0]
    distance = (x_displacement**2 + y_displacement**2)**0.5
    d.append(distance)
    

"""
    We can see that each walker does that end up the same distance from the origin and
we would expect this because each walker should be random so there final point should be random
and therefore the distance from the starting point to the final point.

"""

histogram = plt.hist(d)
plt.show


"""
I might be completely off about this idea but it seems you could use this random walker idea for finding
inmportant information regarding a stars age, temperature, or mass. Since there are so many stars
in the unverise then there is mostly likely some normalized variable with all of them that can fit a 
distribution curve that can be solved with random walkers. Now that I think about it, is this not what we did 
at the first of class with the walkers and the different variables of stars?


Random Walker expanded to 3D with histogram below:

"""

def walk3(N):
    rand.seed()
    x = [0.0]
    y = [0.0]
    z = [0.0]
    for n in range(N):
        x.append(x[-1] + (rand.random() - 0.5)*2.0)
        y.append(y[-1] + (rand.random() - 0.5)*2.0)
        z.append(y[-1] + (rand.random() - 0.5)*2.0)
        
    return np.array(x), np.array(y), np.array(z)
    

N = 1000
walker_3 = walk3(N)

x = walker_3[0]
y = walker_3[1]
z = walker_3[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(x, y, zs=z)

plt.show


for n in range(0,100):
    walker = walk(N)
    x_walker = walker[0]
    y_walker = walker[1]
    z_walker = walker[2]
    x_displacement = x_walker[1000] - x_walker[0]
    y_displacement = y_walker[1000] - y_walker[0]
    z_displacement = z_walker[1000] - z_walker[0]
    distance = (x_displacement**2 + y_displacement**2 + z_displacement**2)**0.5
    d.append(distance)
    
histogram = plt.hist(d)
plt.show
