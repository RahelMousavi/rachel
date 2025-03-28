import random
class Sorting:
    def __init__(self):
        self.array= []
        self.len=len(self.array)

    def array(self):
        for i in range(0,10):
            x = random.randint(0,10)
            self.array.append(x)
        return self.array

    def BubbleSort(self):
        for i in range(self.len-1):
            for j in range(self.len-1):
                if self.array[j]>self.array[j+1]:
                    self.array[j],self.array[j+1] = self.array[j+1],self.array[j]

    def SelectionSort(self):
        for i in range(self.len-1):
            MinPos=i
            for j in range(i+1,self.len):
                if self.array[j]<self.array[MinPos]:
                    MinPos = j

            self.array[MinPos],self.array[i] = self.array[i],self.array[MinPos]

    def InsertionSort(self):
        for i in range(1, self.len):
            j = i-1
            element = self.array[i]
            while (self.array[j]>element) and (j>=0):
                self.array[j+1] = self.array[j]
                j = j-1
            self.array[j+1] = element

    def ShelSort(self):
        k = self.len//2
        while k>0:
            for i in range(k,self.len):
                temp = self.array[i]
                j = i
                while j>=k and self.array[j-k]>temp:
                    self.array[j] = self.array[j-k]
                    j = j-k
                self.array[j] = temp
            k = k//2

    def ExchangeSort(self):
        for i in range(0,self.len-1):
            for j in range(i+1,self.len):
                if self.array[i]>self.array[j]:
                    self.array[i],self.array[j] = self.array[j],self.array[i]

    def quickSort(self):
        self.quickSortHelper(self.array,0,self.len-1)

    def quickSortHelper(self,list,first,last):
        if first<last:
            p = self.partition(list,first,last)
            self.quickSortHelper(list,first,p-1)
            self.quickSortHelper(list,p+1,last)

    def partition(self,list,first,last):
        pivotValue = list[first]
        leftMark = first+1
        rightMark = last
        done = False
        while not done:
            while leftMark<=rightMark and list[leftMark]<=pivotValue:
                leftMark = leftMark+1
            while list[rightMark]>=pivotValue and rightMark>=leftMark:
                rightMark=rightMark-1
            if rightMark<leftMark:
                done = True
            else:
                temp = list[leftMark]
                list[leftMark]=list[rightMark]
                list[rightMark]=temp
        temp=list[first]
        list[first]=list[rightMark]
        list[rightMark]=temp
        return rightMark
    def mergeSort(self,list):
        if self.len<=1:
            return self.array
        middle = self.len//2
        Llist = self.array[:middle]
        Rlist = self.array[middle:]
        Llist = self.mergeSort(Llist)
        Rlist = self.mergeSort(Rlist)
        return list(self.merge(Llist,Rlist))
    def merge(self,lHalf,rHalf):
        res = []
        while len(lHalf)!=0 and len(rHalf)!=0:
            if lHalf[0] < rHalf[0]:
                res.append(lHalf[0])
                lHalf.remove(lHalf[0])
            else:
                res.append(rHalf[0])
                rHalf.remove(rHalf[0])
        if len(lHalf)==0:
            res = res+rHalf
        else:
            res = res+lHalf
        return res
    def print(self):
        for i in range(self.len):
            print(i,end = ' ')
