def largest(arr,n):
     max = arr[0]
     for i in range(1, n):
        if(arr[i] > max):
            max = arr[i]
            return max
arr = [12, 23, 34, 45, 56, 78 ];
n = len(arr)
Ans = largest(arr,n)
print ("Largest num is",Ans)
 
