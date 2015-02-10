from termcolor import colored

#Prints Output Normal Color


def s(text):
    print("\n+------| {} |-----+").format(text)

# Prints Output in Red


def r(text):
    print colored("\n+-----| {} |-----+", 'red').format(text)

# Prints Output in Blue


def b(text):
    print colored("\n+-----| {} |-----+", 'blue').format(text)

# Prints Output in Green


def g(text):
    print colored("\n+-----| {} |-----+", 'green').format(text)

# Prints Output in Yellow


def y(text):
    print colored("\n+-----| {} |-----+", 'yellow').format(text)

