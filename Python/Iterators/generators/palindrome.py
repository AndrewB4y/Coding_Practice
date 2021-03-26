"""
This module intents to work with generators to detect palindromes
saving memory.

Example taken from: https://realpython.com/introduction-to-python-generators/

Here, besides the yield statement/expression, it used the methods:
  - .send()
  - .throw()
  - .close()
"""


def is_palindrome(num):
    """
    is_palindrome - function that evaluates if a number is palindrome.

    @num: number to evaluate

    Return: The same number @num if is a palindrome. False otherwise.
    """
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    """
    infinite_palindromes - infinite sequence generator that yields a digit
                           if this one is a palindrome and starts a search
                           for the next one from there.

    Return: yields any number that is found a palindrome.
    """
    num = 0
    while True:
        if is_palindrome(num):
            # yield is an expression, rather than a statement
            # i takes the value that is yielded.
            # This allows you to manipulate the yielded value.
            i = (yield num)
            if i is not None:
                num = i  # This is the new starting point from which
                # the next palindrome number is searched.
        num += 1


# Main execution
pal_gen = infinite_palindromes()  # Obtains the palindrome generator
for i in pal_gen:
    digits = len(str(i))  # Gets the number of digits of the palindrome
    # found from a starting point.
    pal_gen.send(10 ** (digits))  # returns a processed value to the generator
    # which is captured by the variable "i" in
    # the function infinite_palindromes()

"""
Here you can see that, by creating a generator function into which you
can pass data, you are creating a "coroutine". These are useful for
constructing data pipelines, but as you’ll see soon, they aren’t necessary
for building them.

There is still the .throw() method that can be used to capture some errors
within the generators.
"""


# Now using .throw()
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))

# Here it seems like .throw() doesn't make much difference from "raise"
# yet the perks of using generators can be seen next re-writting the
# generator


def infinite_palindromes():
    """
    infinite_palindromes - infinite sequence generator that yields a digit
                           if this one is a palindrome and starts a search
                           for the next one from there.

    Return: yields any number that is found a palindrome.
    """
    num = 0
    try:
        while True:
            if is_palindrome(num):
                try:
                    i = (yield num)
                    if i is not None:
                        num = i
                except ValueError:
                    print("A process to run when error rised")
                    print("--------------")
                    break
            num += 1
    finally:
        print("Closing generator secuence")


# Running againg shows how you can catch the throw inside the generator
# and proceed with any neccesary closing sequence
pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))


"""
Now, the .close() method as its name implies, .close() allows you to stop
a generator. This can be especially handy when controlling an infinite
sequence generator.
"""

# Updating the main execution

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))

"""
The advantage of using .close() is that it raises StopIteration, an exception used to signal the end of a finite iterator
"""

