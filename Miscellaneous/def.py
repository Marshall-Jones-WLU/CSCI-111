def pyra(h, s):
    """
    
    """
    for i in range(h):
        print((h-i) *" " + (2*i+1) * s)

def main():
    pyra(10, "#")
    pyra(10, "8")


#if __name__ == '__main__':
