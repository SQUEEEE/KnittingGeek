totalsts = 81 #total number of stitches
decreasingsts = 10 #number of stitches to decrease
edgests = 4 #stitches left on both sides

totalbetween = totalsts - 2*decreasingsts - edgests

between = totalbetween / (decreasingsts - 1)
rest = totalbetween % (decreasingsts - 1)

if rest == 0:
  print between, 'sts between decreases'
else:
  between2 = between + 1
  print between, 'sts between decreases', decreasingsts-rest, 'times,', between2, 'sts between decreases', rest, 'times' 
