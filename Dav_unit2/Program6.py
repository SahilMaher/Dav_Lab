 ''' 6.Write a program in python to swap two variables without using
      temporary variable '''   
a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

    # Swap variables without using a temporary variable

a = a + b

b = a - b

a = a - b

print("\nAfter swapping:")
print("a =", a)
print("b =", b)