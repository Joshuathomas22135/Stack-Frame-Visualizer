""" Write a python program to build a Stack Frame Visualizer using Python. They will run five recursion patterns and observe how function calls move down,
return back, or branch into multiple calls. The program helps students compare linear recursion, tail recursion, head recursion, increasing-decreasing
recursion, and tree recursion through simple printed outputs."""

print("Linear Recursion")

def linearRecursion(n):
    if n == 0:
        print("Base case reached")
        return

    print(f"Linear call {n}")
    linearRecursion(n - 1)

linearRecursion(8)
print()

print("Tail Recursion")

def tailRecursion(n, acc=1):
    if n == 0:
        print("Base case reached")
        print(f"Final accumulator: {acc}")
        return

    print(f"Tail call {n}")
    tailRecursion(n - 1, acc * n)

tailRecursion(4)
print()    

print("Head Recursion")

def headRecursion(n):
    if n == 0:
        print("Base case reached")
        return

    headRecursion(n - 1)
    print(f"Head call {n}")

headRecursion(5)
print()

print("Increasing / Decreasing Recursion")

def increasingDecreasingRecursion(n):
    if n == 0:
        print("Base case reached")
        return

    print(f"Increasing {n}")
    increasingDecreasingRecursion(n-1)
    print(f"Decreasing {n}")

increasingDecreasingRecursion(6)
print()

print("Tree Recursion")

def treeRecursion(n):
    if n == 0:
        print("Reached base case")
        return

    print(f"Tree node: {n}")
    treeRecursion(n-1)
    treeRecursion(n-1)

treeRecursion(3)