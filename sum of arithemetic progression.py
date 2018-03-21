def rec_sum(a_1, d, n):
  if (n == 0):
        return 0

  return (n*(a_1+rec_sum(a_1,d,n-1)))/2

print(rec_sum(2,2,4))
