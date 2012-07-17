totalsts = 81
increasests = 10
edgests = 2
betweens = increasests - 1

totbetween = totalsts - edgests
between = totbetween / (increasests - 1)
rest = totbetween % (increasests - 1)

if rest == 0:
  print between, 'sts between increases'
else:
  print between, 'sts between increases', betweens-rest, 'times', between+1, 'sts between increases', rest, 'times' 
