### Question 2: Nested Loops with Conditions
'''
**Description:** Print a triangle pattern using numbers where each row contains numbers up to its index.
**Test Case:** For input 5, the output should include:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```
'''
def print_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
    return

print_triangle(5)

    