def getMedian(Values):
  Values = sorted(Values)
  if (len(Values) % 2 == 1):
    return Values[(len(Values)+1)/2-1]
  else:
    lower = Values[len(Values)/2-1]
    upper = Values[len(Values)/2]
    return (float(lower + upper)) / 2 
print(getMedian) 
