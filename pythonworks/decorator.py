def dec_fun(fn):
    def inner_fun(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_fun

def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2

print(sub(10,5))
print(sub(5,10))