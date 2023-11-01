def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns: 
        bool: answer
    """
    if s.isdigit():
        return True
    else:
        return False
    
    
s="2345"
print(main(s))