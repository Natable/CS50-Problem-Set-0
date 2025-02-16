# Main function
def main():
    # Asks the user for x then converts the input into an int
    x = int (input ("Whats x? "))
    # Prints the output and uses the square function
    print ("x squared is", square (x))

# Square function
def square(n):

    # Squares the input of the user to the power of 2 and then returns the value
    return pow (n, 2)

# Calls the main function
main ()
