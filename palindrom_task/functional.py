
def chek_is_word_palindrom(word: str):
    """Check is word palindrom"""
    inverse_word = word[::-1]
    if inverse_word.lower() == word.lower():
        print("Это слово палиндрормом")
    else:
        print("Это слово не палиндром")