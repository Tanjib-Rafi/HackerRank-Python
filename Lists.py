if __name__ == '__main__' :

    N = int(input())

    store = []

    for i in range (N) :

        s = input().split() #for space separated input

        for j in range (1,len(s)) :
            s[j] = int(s[j])  #converting postiton 1 to rest in int

        if s[0] == "insert":
            store.insert(s[1],s[2])  

        elif s[0] == "append" :
            store.append(s[1])  

        elif s[0] == "remove" :
            store.remove(s[1])  

        elif s[0] == "reverse" :
            store.reverse()  

        elif s[0] == "sort" :
            store.sort() 

        elif s[0] == "pop" :
            store.pop() 

        elif s[0] == "print" :
            print(store)