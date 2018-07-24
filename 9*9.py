import sys
count = 0
for x in xrange(1,10):
	for y in xrange(1,x+1):
		result = x * y  
		sys.stdout.write(str(y)+" * "+str(x)+" = "+str(result))
		sys.stdout.write(' ')
		count+=1
	print ''

print count


