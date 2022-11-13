def unique_with_set(input: str, output: str) -> None:
    ids = set()
    with open("id.txt") as file1, open("id_unique.txt", "w") as file2:
        lines = file1.readlines()
        for line in lines:
            ids.add(line)
        for id in ids:
            file2.write(id)


def unique_without_set(input: str, output: str) -> None:
    ids = []
    with open("id.txt") as file1, open("id_unique.txt", "w") as file2:
        lines = file1.readlines()
        for line in lines:
            if line not in ids:
                ids.append(line)
                file2.write(line)


unique_with_set("id.txt", "id_unique.txt")
# unique_without_set("id.txt","id_unique.txt")

#  id.txt | id_unique.txt
#    1    |      1
#    2    |      2
#    3    |      3
#    2    |
#    3    |
#    1    |

# Note: Add blank line end of id.txt

# Note: Set is unordered

# Alperen Cubuk
