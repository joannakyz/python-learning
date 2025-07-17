print(f"Result of 1 + 5 = {1+5}")
x = 4
print(f"Value of x = {x}") #prints x = 4
print(f"Value of {x = }") #also prints x = 4 

mult_line = (
    f"Value of {x = }\n"
    f"5 + 6 = {5 + 6}\n"
    f"5 * 6 = {5 * 6}"
)
print(mult_line)

#real numbers 
real = 15.617
print(f"Float with 2 decimals: {real:.2f}")
print(f"float with: {real:11f}")
print(f"float with 2 decimals and 5 digits total {real:5.2f}")
print(f"float with 2 decimals and 10 digits total {real:10.2f}") #leaves space for 10 digits, even if it is just space

print(f"An integer in hexadecimal: {155:x}") 
print(f"An integer in octal: {155:o}")
print(f"An integer inn scientific: {155:e}")
