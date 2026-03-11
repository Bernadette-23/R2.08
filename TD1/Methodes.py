import sys

print("\nMéthode N°1 : ")
for arg in sys.argv[1:]:
    print(arg)

print("\nMéthode N°2 : ")
for index in range (1, len(sys.argv)):
    print((sys.argv[index]))

print("\nMéthode N°3 : ")
for index, element in enumerate(sys.argv[1:]):
    print(element)
    print((sys.argv[index+1]))

