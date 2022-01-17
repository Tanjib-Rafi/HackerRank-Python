if __name__ == '__main__':
    students = [] #store students name with score
    scores = [] #store students score for remove the min and store the second min

    for N in range(int(input())):
        name = input()
        score = float(input())

        scores.append(score) #add score in scores list
        students.append([name, score])   #add name and score in students list

    count = scores.count(min(scores)) #count how many min duplicate number are there

    for i in range(count):
        scores.remove(min(scores)) #remover the min duplicate numbers
   
    secondHigh = min(scores) #store the second lowest number

    students.sort() #sort students name alphabetically

    output = [x for x in students if x[1] == secondHigh] #x[1] means the number index

    for i in output:

        print(i[0]) #print name alphabetically