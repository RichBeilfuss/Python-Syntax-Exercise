def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase.    
    """
    for word in words:
        print(f"{word.upper()}")


def print_upper_words_E(words):
    """For a list of words, print out each word that starts with e or E on a separate line, but in all uppercase.
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(f"{word.upper()}")

def print_upper_words_specify(words, starts_with):
    """For a list of words, print out each word that starts with letters defined in words_start_with on a separate line, 
    but in all uppercase.
    """
    for word in words:
        for l in starts_with:
            if word.startswith(l):
                print(f"{word.upper()}")
                break



print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words_E(["elephant", "orange", "Eragon", "dragon", "Blue", "Encourage"])
print_upper_words_specify(["James", "and", "the", "Giant", "Peach"], starts_with={"J","G","P"})