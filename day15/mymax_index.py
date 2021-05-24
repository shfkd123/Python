arr = [0,0,0,0,0 ,0,0,1,0,0]

max = -1;
for i in arr:
    if max < i :
        max = i

for idx,i in enumerate(arr):
    if max == i :
        print(idx)
        break;
    
    