# Norm of a matrix
## Aim
To write a program to find the 1-norm, 2-norm and infinity norm of the matrix and display the result in two decimal places.
## Equipment’s required:
1.	Hardware – PCs
2.	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
# Common Steps for All Norm Calculations
### Step 1:  
Import the required library (`numpy`) for matrix operations.

### Step 2:  
Input the matrix using the `np.array()` function with `eval(input())`.

### Step 3:  
Use the `np.linalg.norm()` function to calculate the norm of the matrix:  
- For **1-norm**, pass `ord=1` as the argument (or directly use `np.linalg.norm(matrix, 1)`).  
- For **2-norm**, pass `ord=2` (or directly use `np.linalg.norm(matrix, 2)`).  
- For **infinity norm**, calculate the maximum row sum using `np.max(np.sum(np.abs(matrix), axis=1))`.

### Step 4:  
Format the result to two decimal places using `"{:.2f}".format()` or `f-string`.

### Step 5:  
Print the result.

## Program:
```Python
# Register No: 24900085
# Developed By: Mohamed Riyaz Ahamed

# 1-Norm of a Matrix

import numpy as np
mat = np.array(eval(input()))
ans = np.linalg.norm(mat, 1)
NORM = "{:.2f}".format(ans)
print(NORM)

# 2-Norm of a Matrix

import numpy as np
# Type your code here
mat = np.array(eval(input()))
ans = np.linalg.norm(mat, 2)
NORM = "{:.2f}".format(ans)
print(NORM)

# Infinity Norm of a Matrix

import numpy as np
matrix = np.array(eval(input()))
red = np.max(np.sum(np.abs(matrix), axis=1))
print(f"{red:.2f}")
```
## Output:
### 1-Norm of a Matrix
![image](https://github.com/user-attachments/assets/7852a673-1ed0-43a1-b00a-134b523e3bc9)


### 2-Norm of a Matrix
![image](https://github.com/user-attachments/assets/56f38142-e1f2-4051-b321-fe6e4bb216dc)


### Infinity Norm of a Matrix
![image](https://github.com/user-attachments/assets/fed6aff8-8b19-4dee-94cc-e598e1a2c27b)


## Result
Thus the program for 1-norm, 2-norm and Infinity norm of a matrix are written and verified.
