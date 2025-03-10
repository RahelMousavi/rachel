import os
class Node:
    def __init__(self, char, data):
        self.char = char
        self.data = data
        self.Lchild = None
        self.Rchild = None

class Huffman:
    def __init__(self):
        self.CFtable = []
        self.tree = []
        self.code = {}

    def CharCounter(self, t, l):
        for i in range(0, l):
            char = t[i]
            found = False
            for j in range(len(self.CFtable)):
                if self.CFtable[j][0] == char:
                    self.CFtable[j][1] += 1
                    found = True
                    break
            if not found:
                self.CFtable.append([char, 1])

        self.CFtable = sorted(self.CFtable, key=lambda item: item[1])
        return self.CFtable

    def Tree(self):
        for char, data in self.CFtable:
            self.tree.append(Node(char, data))

        while len(self.tree) > 1:
            self.tree.sort(key=lambda node: (node.data, node.char is not None, node.char if node.char else chr(127)))
            min1 = self.tree.pop(0)
            min2 = self.tree.pop(0)
            sum_data = min1.data + min2.data
            sum_node = Node(None, sum_data)
            sum_node.Lchild = min1
            sum_node.Rchild = min2
            self.tree.append(sum_node)

        return self.tree[0]

    def PrintTree(self, root):
        def preorder(node):
            if node:
                print(f'Data: {node.data}, Char: {node.char}, Left: {node.Lchild.data if node.Lchild else None}, Right: {node.Rchild.data if node.Rchild else None}')
                preorder(node.Lchild)
                preorder(node.Rchild)
        preorder(root)

    def Codes(self, root):
        def Create(node, current_code):
            if node is None:
                return -1
            if node.char is not None:
                self.code[node.char] = current_code
                return
            Create(node.Lchild, current_code + '0')
            Create(node.Rchild, current_code + '1')

        Create(root, "")
        return self.code


def main():
    text = open('new.txt', 'w')
    text.write("To be, or not to be, that is the question:\n")
    text.write("Whether 'tis nobler in the mind to suffer\n")
    text.write("The slings and arrows of outrageous fortune,\n")
    text.write("Or to take arms against a sea of troubles,\n")
    text.write("And by opposing end them: to die, to sleep\n")
    text.write("No more; and by a sleep, to say we end\n")
    text.write("The heart-ache, and the thousand natural \n")
    text.write("shocks\n")
    text.close()
    text = open('new.txt', 'r')
    t = text.read()
    l = len(t)
    obj = Huffman()
    ob = obj.CharCounter(t,l)
    text.close()
    print(ob)
    root = obj.Tree()
    binaryCodes = obj.Codes(root)
    codes = open('biCodes.txt','w')
    codes.write("\n--BINARY CODES FOR EACH CHARACTER:--")
    for char, code in binaryCodes.items():
        codes.write(f"CHARACTER '{char}'---- BINARY CODE '{code}'\n")
    codes.close()
    path = 'biCodes.txt'

    hamlet=open('BinaryHamlet.txt','w')
    for char in t:
        bi = binaryCodes[char]
        hamlet.write(bi)
    hamlet.close()
    Path = 'BinaryHamlet.txt'

    def menu():
        x = input(
            "--IF YOU WANNA SEE THE BINARY TREE ENTER T--\n--IF YOU WANNA EACH CHARACTER CODE FOR CRACK ENTER C--\n--IF YOU WANNA SEE THE CODED TEXT ENTER CT--\n")
        if x == "T":
            print("\n--HERE IS THE TREE:--\n")
            obj.PrintTree(root)
            y = input("--ANYTHING ELSE?--\n --Y OR N?--\n")
            if y == "Y":
                menu()
            else:
                print("--BAY BAY--")
        elif x == "C":
            os.startfile(path)
            y = input("--ANYTHING ELSE?--\n --Y OR N?--\n")
            if y == "Y":
                menu()
            else:
                print("--BAY BAY--")
        elif x == "CT":
            os.startfile(Path)
            y = input("--ANYTHING ELSE?--\n --Y OR N?--\n")
            if y == "Y":
                menu()
            else:
                print("--BAY BAY--")
        else:
            print("--CHOSE FROM THE MENU FOR GOD SACK--")
            menu()
    menu()

main()