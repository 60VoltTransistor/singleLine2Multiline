dataString = str(input("Enter string to be converted...\n"))
print('\n')
dataList = dataString.split()
tmpString = ""
tmp = 1
splitCount = 10

for i in range(len(dataList)):
    tmpString += dataList[i]
    if (tmp % splitCount) == 0:
        tmpString += '\n'
        """ print(tmpString) """
    else:
        tmpString += ' '
    tmp += 1

print(tmpString)