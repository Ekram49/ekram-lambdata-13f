def enlarge(n):
    return int(n) * 100


if __name__ == "__main__":
    # only run when run from cmd line

    x = 5
    print(enlarge(x))

    z = input("Please choose a number to enlarge: ")
    print(enlarge(int(z)))
