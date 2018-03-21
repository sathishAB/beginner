def smallest(arr,n):
     min = arr[0]
     for i in range(0, n):
        if(arr[i] > min):
            min = arr[i]
            return min
arr = [ 231, 34, 45, 56, 78 ];
n = len(arr)
Ans = smallest(arr,n)
print ("smallest num is",Ans)
 
