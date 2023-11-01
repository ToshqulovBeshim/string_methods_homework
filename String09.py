def main(s):
    """
    A str containing the letter "a" is given. Find the number of letters "a" in this variable.
    Args:
         s: str
    Returns:
        int: answer
    """
    d=0
    for i in range(len(s)):
       if "a"==s[i]:
           d+=1   
    return d
a="isuydgvhsjajhsgddhj"
print(main(a))