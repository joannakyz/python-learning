def palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False
        
word = "radar"
if palindrome(word):
    print("okay")
else:
    print("not")
