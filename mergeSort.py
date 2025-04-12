def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2
        A1 = A[:mid]
        A2 = A[mid:]
        merge_sort(A1)
        merge_sort(A2)

        merge(A1,A2,A)

def merge(a1,a2,a):
    i = j = k =0
    while i < len(a1) and j < len(a2):
         if a1[i] > a2[j]:
             a[k] = a2[j]
             j+=1

         else:
             a[k] = a1[i]
             i+=1
         k += 1

    while i < len(a1):
        a[k] = a1[i]
        i +=1
        k += 1

    while j < len(a2):
        a[k] = a2[j]
        j += 1
        k += 1

list = [1,8,7,4,5,9,6,3]
merge_sort(list)
print(list)