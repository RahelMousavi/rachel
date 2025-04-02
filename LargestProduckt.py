"این کد بزرگترین حاصل ضرب را بین n رقم مجاور در یک سریال عدد نمایش میدهد."

def LargestProduckt(file,n):
    path = str(file)
    file = open(path,'r')
    line = file.read().strip()
    new = open('new.txt','w')

    for i in range(0, len(line) - (n-1)):
        chunk = line[i:i+n]
        new.write(chunk + '\n')

    new.close()
    file.close()
    n = open(r'C:\Users\User\PycharmProjects\pythonProject8\new.txt','r')

    temp = []
    while True:
        mul = n.readline()
        if not mul:
            break
        m = 1
        M = mul.rstrip()
        for i in range(len(M)):
            num = int(M[i])
            m = m * num
        temp.append(m)
    n.close()
    m =max(temp)
    print(m)

def main():
    file = input("Enter the path to the file containing the serial number: ")
    n = int(input("How many adjacent digits do you want the largest coefficient in? "))
    LargestProduckt(file,n)
main()