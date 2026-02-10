#for i in range (4)
# print(iteration)
# print("Iteration number is " + str(i))
# print ()
# print("Fin says \"I\'m fine\"") #Escape char
#Fin says "I'm fine"

#Mutible vs Immutable

x = 10

def f():
    message = 'hello'
    x = 5
    return x

y = f()
print (y)
print (x)
print (message)

#Draw a square
"""
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
"""
def draw_square(size):
    for i in range(size):
        print('🧱' * size)

draw_square(4)

#To row i, how many bricks are there? i+1

def draw_triangle(size):
    for i in range(size):
        print('🧱' * (i + 1)
              )
draw_triangle(4)



###
    #   0   4 spaces + 1 # = 5 5 - 0 - 1 = 4
   ##   1   3 spaces + 2 # = 5 5 - 1 - 1 = 3
  ###   2   2 spaces + 3 # = 5 5 - 2 - 1 = 2
 ####   3   1 space  + 4 # = 5 5 - 3 - 1 = 1
#####   4   0 spaces + 5 # = 5 5 - 4 - 1 = 0
###

def reverse_triangle(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '#' * (i + 1))

reverse_triangle(4)