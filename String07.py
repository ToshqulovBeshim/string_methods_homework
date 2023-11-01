def main(s):
    """
    A variable of type str is given. Check that it consists of letters only.
    Args:
        s: str 
    Returns:
        bool: answer
    """
    if s.isalpha():
        return True
    else:
        return False
s="sjhgf"
print(main(s))