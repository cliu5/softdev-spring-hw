'''
scenario: randomiing greetings in an HTML doc
goal: separate generation oftext from HTML-ification

time-saving solution via closures
'''

import random

'''
this fxn will wrap text in an H1 tag pair:
'''

def make_HTML_heading(f):
    txt = f()
    def inner():
        return '<h1>' + txt + '</h1>'
    return inner

# equivalent to greet = makeHTMLheading(greet)

@make_HTML_heading
def greet():
    greetings = ['Hello', 'Welcome', 'Ayo!', 'Hola', 'Bonjour', 'Word up']
    return random.choice(greetings)

print(greet())

'''
the "pythonic" way
apply a DECORATOR

memoization: process of storing previously calculated results (i.e. writing 'memos')
so as to avoid re-calculation

'''

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

fib = memoize(fib)
print(fib(6))


# def make_fib():
#     x = 0
#     y = 1
#     def count():
#         nonlocal x
#         nonlocal y
#         b = y
#         y = x
#         x = x + b
#         return x
#     return count
#
#
# crt1 = make_fib()
# print(crt1())
# print(crt1())
# print(crt1())
# print(crt1())
# print(crt1())
# print(crt1())
