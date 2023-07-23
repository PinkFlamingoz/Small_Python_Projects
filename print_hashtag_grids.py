# Import
from basic_functions import get_valid_input


# Get size
def get_size_bounded():
    while True:
        n = get_valid_input(int ,"Size must be positive(up to 11), Size: ")
        if 1 <= n <= 11:
            return n


# Print horizontal
def print_horizontal(n):
    print("Horizontal print :\n" + "#" * n)


# Print vertical 
def print_vertical(n):
    print("Vertical print :")
    for i in range(n):
        print("#")


# Print grid
def print_grid(n):
    print("Grid nxn print :")
    print(f"\n{'#'*n}"*n)


# Print pyramid left
def print_pyramid_left(n):
    print("Pyramid left print :")
    for i in range(n):
        print("#" * (i + 1))


#  Print pyramid right
def print_pyramid_right(n):
    print("Pyramid right print :")
    for i in range(n):
        print(" " * (n - i - 1) + "#" * (i + 1))


# Print pyramid top left
def print_top_pyramid_left(n):
    print("Pyramid top left print :")
    for i in range(n, 0, -1):
        print("#" * i)


# Print pyramid top right
def print_top_pyramid_right(n):
    print("Pyramid top right print :")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "#" * i)


# Print pyramid full
def print_pyramid_full(n):
    print("Full pyramid print :")
    for i in range(n):
        print(" " * (n - i - 1) + "#" * (2*i + 1))


# Print pyramid full down
def print_pyramid_full_down(n):
    print("Full pyramid down print :")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "#" * (2*i - 1))


# Print full pyramid with gap
def print_pyramid_full_gap(n):
    print("Full pyramid with gap print :")
    for i in range(1, n+1):
        print(" " * (n - i) + "#" * i + "  " + "#" * i)


# Print full pyramid with gap down
def print_pyramid_full_gap_down(n):
    print("Full pyramid with gap down print :")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "#" * i + "  " + "#" * i)


# Print single pyramid 
def print_pyramid_single(n):
    print("Single pyramid print :")
    for i in range(n):
        print(" " * (n - i - 1) + "# " * (i + 1))


# Print single pyramid down
def print_pyramid_single_down(n):
    print("Single pyramid down print :")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "# " * i)


# Print Pascal triangle with comb function from math module (comb(i, j))
def print_pyramid_pascal(n):
    print("Pascal triangle print :")
    from math import comb
    for i in range(n):
        print(" " * (n - i - 1) + " ".join(str(comb(i, j)) for j in range(i + 1)))


# Print diamond
def print_diamond(n):
    print("Diamond print :")
    for i in range(n):
        print(" " * (n - i - 1) + "#" * (2*i + 1))
    for i in range(n, 0, -1):
        print(" " * (n - i) + "#" * (2*i - 1))


# Main
def main():
    n = get_size_bounded()

    print_horizontal(n)
    print_vertical(n)
    print_grid(n)
    print_pyramid_left(n)
    print_pyramid_right(n)
    print_top_pyramid_left(n)
    print_top_pyramid_right(n)
    print_pyramid_full(n)
    print_pyramid_full_down(n)
    print_pyramid_full_gap(n)
    print_pyramid_full_gap_down(n)
    print_pyramid_single(n)
    print_pyramid_single_down(n)
    print_pyramid_pascal(n)
    print_diamond(n)


# Start
if __name__ == "__main__":
    main()
