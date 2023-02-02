
def create_file(filepath, data):
    with open(filepath, "s") as file:
        file.write(data)


book_data = """
123, A, AA, 1000
124, 8, 88, 1001
125, C, CC, 1002
"""

create_file("book.txt", book_data)
