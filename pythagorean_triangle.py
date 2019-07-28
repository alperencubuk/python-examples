# Find Pythagorean Triangle
# a^2 + b^2 = c^2 and a+b+c = sum

def find_pythagorean_triangle(sum):
    for a in range(1,int(sum/3)+1):
        for b in range(a+1,int(sum/2)+1):
            c = sum-a-b
            if a*a + b*b == c*c:
                return (a,b,c)
    return None


print(find_pythagorean_triangle(1000))
# Output: (200,375,425)

# Alperen Cubuk