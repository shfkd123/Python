import numpy as np

arr = [0,0,1,0,0 , 0,0,0,0,0]
arr_n = np.array(arr)

idx = np.argmax(arr_n)
print("idx", idx)
    