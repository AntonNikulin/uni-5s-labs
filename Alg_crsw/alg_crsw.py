
matrix =[	[1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
			[1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 2], ]


columnLength = len(matrix)
rowLength = len(matrix[0])
sumMtr = 0
centerColumn = columnLength/2
rowStart = columnLength-1
rowEnd = -1
delta = 0

for column in range(rowLength-1, centerColumn-1, -1):
    for row in range(rowStart - delta , rowEnd + delta, -1):
    	sumMtr += matrix[row][column]
    	print matrix[row][column]
    	print "Sum is: {0}".format(sumMtr)

    delta += 1
