#!/usr/bin/env python


def isCommand(command, args):
    index = 0
    for arg in args:
        if isinstance(arg, list):
            for ar in arg:
                if isinstance(ar, list):
                    for a in ar:
                        if isinstance(a, list):
                            index-=1
                            isCommand(command, a)
                        elif not a in command:
                            break
                        else:
                            index+=1
                elif ar in command:
                    index+=1
                    break
    if index >= len(args):
        return True


def callCommand(func, args):
    if args: return func(*args)
    else: return func()


def matchCommand(command, commands):
    for commdef in commands.keys():
        if isCommand(command, commdef):
            return commands[commdef]
    else: return False


def matchAndCallCommand(command, commands):
    ret = matchCommand(command, commands)
    if ret: callCommand(*ret)

