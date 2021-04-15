tabs = 0
with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
    for line in input:
        if '}' in line:
            tabs = tabs - 1
        output.write(' ' * tabs * 4 + line)
        if '{' in line:
            tabs = tabs + 1