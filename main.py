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
