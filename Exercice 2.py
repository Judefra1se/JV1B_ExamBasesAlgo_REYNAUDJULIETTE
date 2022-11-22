myTable=[1,4,2,6,5]
comparateur=0

for iteration in range(0,len(myTable)):
    if myTable[iteration]>comparateur:
        comparateur=myTable[iteration]

myTable.insert(5,comparateur)
myTable.pop(3)

print(myTable)