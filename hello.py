import outside_functions

def double_it(n):
    return(2 * n)

def main():
    print("Main function called")
    print(double_it(25))
    outside_functions.outside2()

main()
