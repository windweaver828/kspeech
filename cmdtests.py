import itertools
import random
from commands import isCommand

wordslist = [
    "please", "if", "to", "the", "would", "you", "or", "blah",
    "test", "when", "hello", "world", "this", "they", "them",
]

command = [
    ['power', 'shut', 'turn'],
    ["off", "down"],
    ["computer"]
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
for test in gentests(command):
    test = addwords(test, wordslist, random.randrange(3, 10))
    test = " ".join(test)
    if isCommand(test, command):
        passed.append(test)
    else:
        fails.append(res)

print("Ran {testnum} tests.".format(testnum=(len(passed)+len(fails))))
print("Passed {passed} tests.".format(passed=len(passed)))
for pas in passed:
    print("\t{pas}".format(pas=pas))
print("Failed {fails} tests.".format(fails=len(fails)))
for fail in fails:
    print("\t{fail}".format(fail=fail))

