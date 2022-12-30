import textwrap 

dataString = str(input("Enter string to be converted...\n"))

print('')
charWidth = 50
wapper = textwrap.TextWrapper(width=charWidth)
tmpString = wapper.fill(text=dataString)

print(tmpString)