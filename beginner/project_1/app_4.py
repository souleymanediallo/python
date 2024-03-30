def est_palindrome(mot):
    return mot == mot[::-1]

print(est_palindrome("radar"))
print(est_palindrome("python"))
print(est_palindrome("kayak"))
print(est_palindrome("ressasser"))
print(est_palindrome("bonjour"))
