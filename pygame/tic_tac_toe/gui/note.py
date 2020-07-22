def click_to_cell(x, y):
    cell_width = 50
    cell_height = 50
    return x // cell_width, y // cell_height

column, row = click_to_cell(120, 70)
print(row)
print(column)

"""
_|_|_
_|_|_ <- row 1
_|_|_
    ^ column 2
"""
