def optimal_order(list,new,n):
    for i in range(0,n):
        x = select_min(list,i,n)
        new[i] = x

def select_min(l,i,n):
    x = l[i]
    L = i

    for k in range(i+1,n):
        if x > l[k]:
            x = l[k]
            L = k
    l[L],l[i] = l[i] , l[L]

    return x

list = [1.5,8.7,9.0,4.4,1.0,2.9,3.6,1.3]
new = [0 for _ in range(len(list)-1)]
optimal_order(list,new,len(list)-1)
print(new)