"""
Given a string, reverse the order of the vowels in the string.

Method: Two pointer technique -- forward/backward two-pointer

Time Complexity: O(n) (where n is the size of the array )
Space Complexity: O(1)

Time: 10 minutes
"""

def solution(s):
    s = list(s) # turn string to mutable type
    l = 0         # set up two pointers
    r = len(s) - 1

    vowels = set(["a","e","i","o","u", "A", "E", "I", "O", "U"])

    while r > l:
        # flip if both vowels
        if (s[r] in vowels) and (s[l] in vowels):
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            l += 1
            r -= 1
        elif s[r] in vowels:
            l += 1
        elif s[l] in vowels:
            r -= 1
        else:
            l+=1
            r-=1

    
    return "".join(s)

if __name__ == "__main__":
    # Provided test cases
    s = "Uber Career Prep"
    assert solution(s) == "eber Ceraer PrUp"

    s = "xyz"
    assert solution(s) == "xyz"

    s = "flamingo"
    assert solution(s) == "flominga"

    # Student test cases
    assert solution("") == ""
    assert solution("abba") == "abba"
    assert solution("Abba") == "abbA"
    assert solution("Potatoooo") == "Pototooao"




