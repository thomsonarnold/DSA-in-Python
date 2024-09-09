def Vowels(A):
    return [i for i in A if i in "aeiou" ]
print(Vowels("geeksforgeeks"))

def Strings(B):
    return [i for i in B if i.startswith("g")]
print(Strings(["geeks","gfg","Arnold","gold"]))

def square():
    return [i**2 for i in range(0,6)]
print(square())