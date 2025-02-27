import os, random
os.system('cls')

row = 0
int_rows = 5
sta_values = [1, 30, 320, 3220, 32220]

while row < int_rows:
    col = 0
    int = sta_values[row]
    row_values = []
    
    while col < 5:  
        row_values.append(int)
        int += 1
        col += 1
    print(" ".join(map(str, row_values)))
    row += 1
