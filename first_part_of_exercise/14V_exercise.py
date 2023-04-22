
A = int(input("Enter the distance between rows : "))
B = int(input("Enter the distance between holes in a row : "))
N = int(input("Enter the number of holes in each row : "))
l = int(input("Enter the length of the free end of the lace : "))

L = ((N-1)*A) + ((N-1)*B)

total_length = L + 2 * N * l

print(f"Your total lenght of lace is {total_length} cm.")
