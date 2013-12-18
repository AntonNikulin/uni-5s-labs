
matrix =[	[1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
			[1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 2],]

length = len(matrix)
sum = 0
column = length - 1
minColumn = length/2
for row in range(length-1,-1,-1):
	sum += matrix[row][column]
	print matrix[row][column]
	print "Sum is: {0}".format(sum)