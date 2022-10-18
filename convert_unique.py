ids = []
with open("id.txt") as file1, open("id_unique.txt","w") as file2:
    lines = file1.readlines()
    for line in lines:
        if line not in ids:
            ids.append(line)
            file2.write(line)

#  id.txt | id_unique.txt
#    1    |      1
#    2    |      2
#    3    |      3
#    2    |
#    3    |
#    1    |

# Note: Add blank line end of id.txt

# Alperen Cubuk
