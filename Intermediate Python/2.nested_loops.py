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
i = 0

while i <=5:
    for j in range(1, i+1):
        print(j, end='')
    