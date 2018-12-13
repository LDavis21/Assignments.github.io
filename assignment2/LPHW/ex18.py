#exercise 18
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args i actually pointless, we can just do this 
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just take one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this take no arguments
def print_none():
    print("i got nothin'.")


print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("first!")
print_none()
 