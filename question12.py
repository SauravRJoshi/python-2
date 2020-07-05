def is_palindrome(input_word):
    if input_word.upper() == input_word.upper()[::-1]:
        return 'is palindrome'
    else:
        return 'is not palindrome'

input_word = input("Enter a string :")
print(input_word,is_palindrome(input_word))