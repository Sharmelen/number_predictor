# import xlsxwriter

# # Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('Expenses01.xlsx')
# worksheet = workbook.add_worksheet()

# # Some data we want to write to the worksheet.
# expenses = (
    # ['Rent', 1000],
    # ['Gas',   100],
    # ['Food',  300],
    # ['Gym',    50],
# )

# # Start from the first cell. Rows and columns are zero indexed.
# row = 0
# col = 0

# # Iterate over the data and write it out row by row.
# for item, cost in (expenses):
    # worksheet.write(row, col,     item)
    # worksheet.write(row, col + 1, cost)
    # row += 1

# workbook.close()

# import itertools

# stuff = [1, 2, 3]
# for L in range(0, len(stuff)+1):
    # for subset in itertools.combinations(stuff, L):
        # print(subset)
		
		
import itertools
print(list(itertools.combinations([1, 2, 3],3)))

print(list(itertools.permutations([1, 2, 3])))