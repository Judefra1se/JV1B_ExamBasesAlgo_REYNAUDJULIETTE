myTable=[1,4,2,6,5]
comparateur=5
tours=0

while (tours<len(myTable)-1):
    comparateur=myTable[tours]
    indice=tours
    for iteration in range(0,len(myTable)):
        if myTable[iteration]>comparateur:
            comparateur=myTable[iteration]
            myTable.pop
            myTable.insert((len(myTable)),comparateur)
    

    tours=tours+1

print(myTable)
    