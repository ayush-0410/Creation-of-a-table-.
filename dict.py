record1 = ['stdid', 'stdname', 'standard', 'age', 'Hindi', 'English', 'Maths', 'Science', 'Computer', 'Total']
record2 = ['stdid101', 'Ashish Kumar', '10th', 15, 67, 89, 87, 89, 90, 422]
record3 = ['stdid102', 'Abhishek Kumar', '10th', 14, 85, 45, 48, 90, 45, 313]
record4 = ['stdid103', 'Aman', '10th', 15, 23, 56, 78, 78, 67, 302]
record5 = ['stdid104', 'Rahul', '10th', 14, 45, 67, 45, 45, 56, 258]
record6 = ['stdid105', 'Ruby', '10th', 13, 89, 67, 89, 93, 65, 403]
record7 = ['stdid106', 'Sumam', '10th', 13, 90, 46, 67, 67, 67, 337]
record8 = ['stdid107', 'Saurabh', '10th', 15, 23, 23, 34, 45, 34, 159]
record9 = ['stdid108', 'Sumit', '10th', 14, 56, 45, 67, 78, 90, 336]
record10 = ['stdid109', 'Kamlesh', '10th', 15, 45, 56, 78, 99, 67, 345]
record11 = ['stdid110', 'Rohan', '10th', 15, 34, 12, 24, 45, 56, 171] 


# Combine the records into a list of lists
records = [record1, record2, record3, record4, record5, record6, record7, record8, record9, record10, record11]


# Column widths
column_widths = [10, 15, 10, 5, 8, 8, 8, 10, 10, 6]

# The table header
header = records[0]
header_row = "  ".join(f"{header[i]:<{column_widths[i]}}" for i in range(len(header)))
print(header_row)
print("  " * len(header_row))

# The table rows
for row in records[1:]:
    row_str = " | ".join(f"{row[i]:<{column_widths[i]}}" for i in range(len(row)))
    print(row_str)

# The index of the English column
english_index = record1.index('English')

# Names of students who scored more than 50 in English
print("\nStudents who scored more than 50 in English:")
for record in records[1:]:
    if record[english_index] > 50:
        print(record[record1.index('stdname')])
