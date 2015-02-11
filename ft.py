#!/usr/bin/env python

from commands import isCommand




command = "hello world good morning"
assert(isCommand(command, [['hello']]))
assert(isCommand(command, [['hello'], ['world']]))
assert(isCommand(command, [['hello', 'world']]))
assert(isCommand(command, [['hello'], ['noexists', ['world', "good"]]]))



assert(not isCommand(command, [['noexists']]))
assert(not isCommand(command, [['hello', "world"], ['noexists']))
