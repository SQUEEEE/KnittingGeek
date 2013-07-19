

rnd = int(input('How many sts do you start with? '))
end = int(input('How many sts do you end with? '))

sts = rnd*3 #there are worked 3 rounds before decreases start



while (rnd > end):
  rnd-=4 #4 sts decrease every other round
  sts+=rnd*2 #...so there are 2 rounds worked with this stitch count
#  print "Stitch count is ", rnd
#  print "No sts worked total: ", sts

stripel = int(input('How many rounds is the stripe sequence? '))
stripew = int(input('Over how many sts? '))

stripe = stripel*stripew #number of sts in a stripe sequence

stripes = sts/stripe #number of stripes needed for the heel


print(stripes, " stripe sequence(s) needed for heel.")
