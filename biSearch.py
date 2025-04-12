def bi(A,x,low,high):
    mid =(low+high)//2

    if x==A[mid]:
        return mid

    elif x > A[mid]:
        return bi(A,x,mid+1 , high)

    else:
        return bi(A,x,low,mid-1)

list = [0,1,2,3,4,5,6,7,8,9]

x = bi(list,3,0 , len(list)-1)
print(x)