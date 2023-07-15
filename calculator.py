# Integer overflow is gone, python just uses more memory if the number gets bigger,
# truncation is also gone,
# however floating-point imprecision is still there

x = int(input("x: "))
y = int(input("y: "))

z = x + y
zz = x / y

print(x + y)
print(zz,z)
print (f"{zz:.50f}")
