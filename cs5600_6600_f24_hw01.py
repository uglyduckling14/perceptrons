
####################################################
# CS 5600/6600: F24: Assignment 1
# ESPERANZA HAUPTMAN
# A02391616
# Starter code for Assignment 1
#####################################################

import numpy as np

class and_percep:

    def __init__(self):
        ## your code here
        pass
        
    def output(self, x):
        ## your code here
        if(x[0]==1 and x[1]== 1):
            return 1
        return 0
        

class or_percep:
    
    def __init__(self):
        ## your code here
        pass

    def output(self, x):
        ## your code here
        if(x[0]==1 or x[1]==1):
            return 1
        return 0

class not_percep:
    
    def __init__(self):
        ## your code here
        pass

    def output(self, x):
        ## your code here
        if(x[0]==1):
            return 0
        return 1

class xor_percep:
    
    def __init__(self):
        ## your code here
        pass

    def output(self, x):
        if((x[0]!=1 and x[1]== 1) or (x[0]==1 and x[1]!=1)):
            return 1
        return 0

class xor_percep2:
    def __init__(self):
        ## your code here
        pass

    def output(self, x):
        if((x[0]!=1 and x[1]== 1) or (x[0]==1 and x[1]!=1)):
            return np.array([1])
        return np.array([0])

class percep_net:
    
    def __init__(self):
        ## your code here
        pass

    def output(self, x):
        ## your code here
        if(((x[0]==1 or x[1]==1) and not(x[2]==1)) or x[3] ==1):
            return 1
        return 0
        





