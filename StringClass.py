class StringClass:
    def __init__(self):
        self.Nchar=0
        self.str=[]

    def CountChar(self,x,c):
        for i in self.str:
            if i==x:
                c+=1
        return c

    def Concat(self,other):
        self.str=self.str+other.str

    def LenStr(self,N):
        for i in self.str:
            N+=1
        return N

    def ReplaceChar(self,x,y):
        for i in range(self.Nchar):
            if self.str[i]==x:
                self.str[i]=y

    def Replace(self,i,x):
        N = len(self.str)
        if i < N:
            self.str[i]=x

    def AppendChar(self,x):
        self.str[self.Nchar]=x

    def Insert(self,str,i):
        if i < self.Nchar:
            one = self.str[0:(i-1)]
            two = self.str[i:]
            return one + str + two