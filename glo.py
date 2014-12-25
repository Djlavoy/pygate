from termcolor import colored

# Prints OutPut
def output(text):
    print("\n+-----| {} |-----+").format(text)
# Prints Output in Red
def output_r(text):
    print colored("\n+-----| {} |-----+", 'red').format(text)
# Prints output in Blue
def output_b(text):
    print colored("\n+-----| {} |-----+", 'blue').format(text)
# Prints output in Green
def output_g(text):
    print colored("\n+-----| {} |-----+", 'green').format(text)
# Prints output in Yellow
def output_y(text):
    print colored("\n+-----| {} |-----+", 'yellow').format(text)
