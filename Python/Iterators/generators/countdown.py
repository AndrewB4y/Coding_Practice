

def countdown(n: int):
    """
    countdown - function that returns a generator object that yields
                the numbers from @n to 0 in steps of -1.
    
    @n: Integer number from which the countdown starts.

    Return: Generator object that holds the countdown.
    """
    
    print(f"Countdown starts from {n}")
    if n >= 0:
        while (n >= 0):
            yield n
            n -= 1
            yield "test"
        
    print("Done")


print(countdown(5))

for i in countdown(5):
    print(i)

gen = countdown(5)
it = countdown(5).__iter__()
print(it)
print(type(it))
print(it.__next__())
print(gen.__next__())
print("/////////////////////")
print(it.__next__())
print(gen.__next__())
print("/////////////////////")
print(it.__next__())
print(gen.__next__())
print("/////////////////////")