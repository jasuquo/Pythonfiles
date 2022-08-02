# 🚨 create map list below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
#there are 3columns and 3rows input should in this format e.g 23 column 2 row 3
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

row_selected =map[vertical -1] 
row_selected[horizontal -1]="X"

print(f"{row1}\n{row2}\n{row3}")
