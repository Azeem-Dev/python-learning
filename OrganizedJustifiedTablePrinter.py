from typing import Literal,List


def PrintTable(table: list[list[str]], justification: Literal['r', 'l'] = 'r') -> None:
    noOfColumns = len(table[0])

    for row in table:
        if len(row) != noOfColumns:
            print("Error: All rows must have the same number of columns.")
            return

    # Transpose the table (ROWS INTO COLUMNS)
    # new_table = []
    # for column in range(noOfColumns):
    #     new_row = []
    #     for row in range(len(table)):
    #         new_row.append(table[row][column])
    #     new_table.append(new_row)

    colWidths = [max(len(column) for column in row) for row in table]

    for columnIndex in range(noOfColumns):
        new_row = []
        for rowIndex, row in enumerate(table): 
            if (justification == 'r'):
                new_row.append(row[columnIndex].rjust(colWidths[rowIndex]))
            else:
                new_row.append(row[columnIndex].ljust(colWidths[rowIndex]))
        print(" ".join(new_row))


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

PrintTable(tableData, 'r')
