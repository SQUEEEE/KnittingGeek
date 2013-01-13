rnd = 64 #at the beginning of the heel there are 64 sts total
sts = rnd*3 #these are worked 3 rounds before decreases start

while (rnd > 24):
  rnd-=4 #4 sts decrease every other round
  sts+=rnd*2 #...so there are 2 rounds worked with this stitch count
  print "Stitch count is ", rnd
  print "No sts worked total: ", sts

stripe = 6*60 #the self striping yarn is 6 rows over 60 sts => 360 sts/stripe
stripes = sts/stripe #number of stripes needed for the heel

print stripes, " whole stripes needed for heel, plus ", sts%stripe, " sts."     
