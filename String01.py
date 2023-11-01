def main(s):
    """
    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.
    Args:
        s: str 
    Retu rns:
        str: answer
    """ 
    #a=s.capitalize()
    b=s.title()
    # c=s.lower()
    # d=s.upper()
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    return b
s="beshikjdvfhb bsj nk lsdjf hvgjwdfhh"
print(main(s))