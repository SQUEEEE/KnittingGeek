totalsts = 81 #total number of stitches
decreasingsts = 10 #number of stitches to decrease
edgests = 4 #stitches left on both sides
betweens = decreasingsts - 1

totalbetween = totalsts - 2*decreasingsts - edgests #number of stitches that aren't used for decreasing or as edgests

between = totalbetween / betweens  #there are one less 'between' than number of decreases
rest = totalbetween % betweens  #the remaining stitches need to be added to a 'between' each

if rest == 0:
  print between, 'sts between decreases'
else:
  print between, 'sts between decreases', betweens-rest, 'times,', between+1, 'sts between decreases', rest, 'times' 
