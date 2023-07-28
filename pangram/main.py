def is_pangram(text):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    letter=set((text.lower()))
    return set(alphabet)<=letter

def  anagram_check():
    metin="The quick brown fox jumps over the lazy dog"
    if(is_pangram(metin)):
        print("is anagram")
        return True
    else:
        print("not anagram")
        return False



anagram_check()