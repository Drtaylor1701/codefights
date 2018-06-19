def seatsInTheater(nCols, nRows, col, row):
    columnInQuestion = col - 1
    nCols = nCols - columnInQuestion
    nRows = nRows - row
    print(nCols, nRows)
    return nCols * nRows
