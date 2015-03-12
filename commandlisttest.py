import itertools
import random
from Commands import commands
from commandtools import isCommand


wordslist = [
    "if", "to", "the", "would", "you", "or", "this", "they", "them",
]

def gentests(command):
    return itertools.product(*command)


def addwords(addto, wordslist, count):
    addto = list(addto)
    for _ in xrange(count):
        addto.append(random.choice(wordslist))
    random.shuffle(addto)
    return addto 


if __name__ == "__main__":
    # List all commands and functions linked to

    # Test isCommand on all variations of defined commands in commands.py
    passed = list()
    fails = list()
    for command in commands:
        for test in gentests(command):
        # test = addwords(test, wordslist, random.randrange(3, 10))
            test = " ".join(test)
            if isCommand(test, command):
                passed.append(test)
            else:
                fails.append(test)

    for pas in passed:
        print("{pas}".format(pas=pas))
    for fail in fails:
        print("{fail}".format(fail=fail))
