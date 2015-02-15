import itertools
import random
from commands import isCommand, commands

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


passed = list()
fails = list()
for command in commands.keys():
	for test in gentests(command):
	    # test = addwords(test, wordslist, random.randrange(3, 10))
	    test = " ".join(test)
	    if isCommand(test, command):
	        passed.append(test)
	    else:
	        fails.append(test)

print("Ran {testnum} tests.".format(testnum=(len(passed)+len(fails))))
print("Passed {passed} tests.".format(passed=len(passed)))
for pas in passed:
    print("\t{pas}".format(pas=pas))
print("Failed {fails} tests.".format(fails=len(fails)))
for fail in fails:
    print("\t{fail}".format(fail=fail))

