def quick_sort(A , low , high):

    if low < high :

        j = partition(A,low,high)
        quick_sort(A,low,j-1)
        quick_sort(A, j+1,high)

def partition(a,l,h):
    pivot = a[l]
    i = l + 1
    j = h
    while True:
        while i <= j and pivot >= a[i]:
            i += 1

        while i <= j and  a[j] >= pivot:
            j -= 1

        if i > j:
            break
        a[i] , a[j] = a[j] , a[i]
    a[l] , a[j] = a[j] , a[l]

    return j

list = [1,8,7,4,5,9,6,3]
quick_sort(list,0,len(list)-1)
print(list)