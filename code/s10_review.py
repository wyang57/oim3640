n = 6
while n != 0:
    print(n)
    n -= 2

print('after while loop, n is', n)

def uses_any(word, letters):
    for letter in word:
        if letter in letters:
            return True
    return False


def version_a(word):           
    for letter in word:          
        if letter in 'aeiou':        
            print(letter)                
    print('Done')                 


def version_b(word):
    for letter in word:
        if letter in 'aeiou':
            return letter
    return 'None found'

version_a('hello')