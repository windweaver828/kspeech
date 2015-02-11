#!/usr/bin/env python

def isCommand(command, args):
        index = 0
        for arg in args:
            if isinstance(arg, list):
                for ar in arg:
                    if isinstance(ar, list):
                        for a in ar:
                            if not a in command:
                                break
                        else:
                            index+=1
                    elif ar in command:
                        index+=1
                        break
        if index >= len(args):
            return True


def callfunc(func, args=list()):
    return func(args*)


def helloworld():
    print("Hello, World!")


commands = {
	[["hello"], ["world"]]:callfunc(helloworld),
	}