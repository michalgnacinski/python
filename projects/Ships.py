def create_board(rows, cols):
    width = 4
    vert_line = ("+" + "-" * width) * cols + "+"
    hori_line = ("|" + " " * width) * cols + "|"
    
    for _ in range(rows):
        print(vert_line)
        print(hori_line)
    print(vert_line)
create_board(5,5)