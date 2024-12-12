import random

def find_primes(start:int, stop:int) -> list:
    primes=[]
    for i in range(start, stop):
        is_prime = True
        for j in range(2,int(i/2)):
            if i%j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    return primes

def say_hi_to(first:str, last="", do_print=False) ->str:
    text = "Hi" + " " + first + " " + last + "!"
    if do_print:
        print(text)
    return text
    
def shuffle_trials(trials, max_iter=1000):
    ok = False
    count = 0
    while not ok:
        count+=1
        if count > max_iter:
            raise StopIteration
        found_duplicate = False
        for i in range(1, len(trials)):
            if trials[i] == trials[i-1]:
                found_duplicate = True
        if not found_duplicate:
            ok = True
        else:
            random.shuffle(trials)
    return trials