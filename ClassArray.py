from array import *
class Array:

    def __init__(self,size):
        self.MaxSize = size
        self.array = array("i", [])

    def Add(self,x):
        self.array.append(x)
        self.MaxSize = self.MaxSize+1
        print( self.MaxSize , x)

    #Order = O(1)

    def Search(self,x):
        for i in self.array:
            if self.array[i]==x:
                return True
            elif self.array[i]!= x:
                continue
            else:
                return False

    #Best Order = O(1)
    #Worst Order = O(n)
    #Midel Order = O(n)

    def Insert(self,pos,x):
        for i in range(self.MaxSize,pos,-1):
            self.array[i+1] = self.array[i]
        self.array[pos] = x
        self.MaxSize = self.MaxSize+1
        return self.array , self.MaxSize

    # Best Order = O(1)
    # Worst Order = O(n)
    # Midel Order = O(n)

    def Delet(self,pos):
        x = self.array[pos]
        for i in range(pos,self.MaxSize-1):
            self.array[i]=self.array[i-1]
        self.MaxSize = self.MaxSize-1
        return self.array,self.MaxSize,x
    # Best Order = O(1)
    # Worst Order = O(n)
    # Midel Order = O(n)
