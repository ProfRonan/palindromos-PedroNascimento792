"""Main functions"""
import re

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    string = re.sub(r"\W+", "", string.lower())
    return string == string[::-1]
    
