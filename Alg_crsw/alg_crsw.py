
matrix =[	[1, 1, 1, 1, 1, 1, 1, 1, 100, 2],
			[1, 1, 1, 1, 1, 1, 1, 100, 2, 2],
			[1, 1, 1, 1, 1, 1, 100, 2, 2, 2],
			[1, 1, 1, 1, 1, 100, 2, 2, 2, 2],
			[1, 1, 1, 1, 100, 2, 2, 2, 2, 2],
			[1, 1, 1, 1, 100, 2, 2, 2, 50, 2],
			[1, 1, 1, 1, 1, 100, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 100, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 100, 2, 2],
			[1, 1, 1, 1, 1, 1, 1, 1, 100, 2], ]


columnLength = len(matrix)
rowLength = len(matrix[0])
maxElem = 0
maxElemRow = 0
maxElemColumn = 0
centerColumn = columnLength/2
rowStart = columnLength-1
rowEnd = -1
delta = 0   #value to converge

for column in range(rowLength-1, centerColumn-1, -1):
    for row in range(rowStart - delta , rowEnd + delta, -1):
    	if matrix[row][column] > maxElem:
            maxElem = matrix[row][column]
            maxElemRow = row
            maxElemColumn = column

    delta += 1

print "Max element is: {0} in position {1} : {2}".format(maxElem, maxElemRow, maxElemColumn)
