def string_to_val(s = "hello"):
    return int("".join(["{:07b}".format(ord(x)) for x in s]),2)
    
def val_to_string_natural(val = 28130883183):
    s = []
    v = val
    while v > 0:
        s.append(v & 0b1111111)
        v = v >> 7
    s.reverse()
    g = [chr(x) for x in s]
    return "".join(g)
    
def main():
    print(string_to_val())
    print(val_to_string_natural())
    
    
if __name__ == "__main__":
    main()
