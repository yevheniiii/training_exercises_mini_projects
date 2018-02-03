# Exercise 1

"""
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
where every other element of the input tuple is copied, starting with the first one.
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
"""
# Solution 1


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

    t = []
    for tup in aTup:
        if len(tup) % 2 != 0:
            t.append(tup)
    return tuple(t)


aTup = ('I', 'am', 'a', 'test', 'tuple')

print(oddTuples(aTup))

# Solution 2


def oddTuples(aTup):
    return aTup[::2]


aTup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(aTup))

########################################################################
