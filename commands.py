#!/usr/bin/env python

def callfunc(func, args=list()):
    if len(args):
        return func(args*)
    else: return func()


def helloworld():
    print("Hello, World!")


commands = {
    [["hello"], ["world"]]:(helloworld, None),
}