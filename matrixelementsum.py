def matrixElementsSum(matrix):
    total = 0
    print("input matrix")
    notHaunted = []
    print("creating matrix to store values")
    print(matrix)
    matrixHeight = len(matrix)
    print("The matrix height is: " + str(matrixHeight))
    matrixWidth = len(matrix[0])
    print("The matrix width is: " + str(matrixWidth))
    validColumns = []
    column = 0
    for i in range(matrixWidth):
        validColumns.append(column)
        column += 1
    print("The valid columns in this matrix are currently : " + str(validColumns))
    validRows = []
    row = 0
    for i in range(matrixHeight):
        validRows.append(row)
        row += 1
    print("List of valid rows generated.")
    zeros[]
    for row in validRows:
        print("checking row :" + str(validRows[row]))
        for column in validColumns:
            print("checking columns")
            if matrix[row][column] == 0:
                print("This room is haunted.")
                print("Removing column from valid columns.")
                validColumns.remove(column)
                print("The columns remaining are :" + str(validColumns))
                zeros.append([row,column])
            else:
                total = total + matrix[row][column]
                print("total value has been updated to " + str(total))
                print("The columns remaining are :" + str(validColumns))
    return total

matrix = [[0,1,1,2],
            [0,5,0,0],
            [2,0,3,3]]
matrixElementsSum(matrix)
