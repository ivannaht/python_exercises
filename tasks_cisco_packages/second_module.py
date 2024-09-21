from sys import path
from first_module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

if __name__ == "__main__":
    print("main module")
else:
    print("other module")

for p in path:
    print(p)
