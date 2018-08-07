# Examples of local and global variables. Locals are only visibly inside function


# define global
a = [1,2,3]

#define function f1
def f1():
    a[0] = 5

    print(a)

def f2():
    print(a)

f1()
f2()
print(a)


