stringFromSingleQuote='Hello World'
stringFromDoubleQuotes="Hello Worlds"
emptyString=""
print(stringFromSingleQuote)

stringUsingStr=str("Hello World from str")
print(stringUsingStr)

fetchSpecificCharacterFromString=stringFromSingleQuote[2]
print(fetchSpecificCharacterFromString)

fetchSpecificCharactersFromString=stringFromSingleQuote[2:8]
print(fetchSpecificCharactersFromString)

from math import pi
print(f'The pi number is {pi}')

myText=str("The number is {}").format(pi)
print(myText)

myText="{:.2f}".format(pi)
print(myText)

myText="Full num: {} and shortened num: {:.2f}".format(pi,pi)
print(myText)

list=['what','a','day']

#.join(['what','a','day'])
#.split()
#.lower()
#.upper()
#.strip()
#.replace()
#.trim()

print('gg' in 'eggs')
print('eggs make' + ' omelette')
print(len('ola kala'))
print('ola kala'.count('l'))
print('repeat'*3)

list=[]
list=[1,2,3,6,7,2,4,3,8,4,6,4]
#print(list[2])
#list.sort()
#list.sort(reverse=true)
#list.append(10)
#list.insert(2,10)
#list.reverse()
#list.clear()
print(list)

print(3 in list)
print(list.count(4))

del list[4]
print(list)

print("After finishing my changes I like to check for errors")

