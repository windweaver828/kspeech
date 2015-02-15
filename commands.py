#!/usr/bin/env python

# Examples to help under the if name == main clause down below

from CommandsDict import CommandsDict

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

# ------------------------------------------------------- #
# Add functions to call here                              #

def helloworld():
	print("Hello, World!")


def helloname(name):
	print("Hello, {name}!".format(name=name))


commands = CommandsDict()
# ------------------------------------------------------- #
# Add command definitions here                            #

commdef = [['hello'], ['world']]
func = helloworld
args = False
commfunc = [func, args]
commands[commdef] = commfunc


commdef = [['hello'], ['james', 'two']]
func = helloname
args = ['James']
commfunc = [func, args]
commands[commdef] = commfunc


if __name__ == '__main__':
	# This is an example set of functions and commands
	commands = CommandsDict()

	def helloworld():
		print("Hello, World!")

	def helloname(name):
		print("Hello, {name}!".format(name=name))

	def hellonames(name1, name2):
		print("Hello, {name1} and {name2}".format(name1=name1, name2=name2))


	# Example of setting command definition for
	# a function with no arguments
	commdef = [['hello'], ['one']]
	func = helloworld
	args = False
	commfunc = [func, args] # These two lines
	commands[commdef] = commfunc # Always the same

	# Example of setting command definition for
	# a function with one argument
	commdef = [['hello'], ['two']]
	func = helloname
	args = ['Keith'] # Put args in a comma seperated list
	commfunc = [func, args] # Again, These two lines
	commands[commdef] = commfunc # Always the same

	# Example of setting command definition for
	# a function with multiple arguments
	commdef = [['hello'], ['three']]
	func = hellonames
	args = ['Keith', 'James'] # Args always go in a one
							  # dimensional comma seperated list
	commfunc = [func, args]
	commands[commdef] = commfunc

	# And to pull it all back out and call it
	command = "hello one"
	func, args = matchCommand(command, commands)
	callCommand(func, args)
	# Or a nice one liner that we so love
	command = "hello two"
	callCommand(*matchCommand(command, commands))

	# If all we want is to call it if it exists (like usual)
	# and ignore if its not a match we use
	command = "This doesn't exist hahahah"
	matchAndCallCommand(command, commands)

	command = "hello three"
	matchAndCallCommand(command, commands)