#!/usr/bin/env python

from commands import isCommand




command = "hello world good morning"
assert(isCommand(command, [['hello']])==True)
assert(isCommand(command, [['hello'], ['world']])==True)
assert(isCommand(command, [['hello', 'world']])==True)


assert(isCommand(command, [['noexists']])==False)
