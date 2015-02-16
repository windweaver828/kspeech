#!/usr/bin/env python

from ast import literal_eval as le

class CommandsDict(dict):
	def __init__(self):
		dict.__init__(self)

	def __getitem__(self, key):
		if isinstance(key, list): key = repr(key)
		return dict.__getitem__(self, key)


	def __setitem__(self, key, val):
		if isinstance(key, list):
			key = repr(key)
		dict.__setitem__(self, key, val)


	def __iter__(self):
		for key in dict.__iter__(self):
			yield le(key)


	def __contains__(self, key):
		return key in self.keys()

	def has_key(self, key):
		return self.__contains__(key)


	def keys(self):
		return [le(key) for key in dict(self)]


	def items(self):
		items = list()
		for key in self.keys():
			items.append((key, self.__getitem__(key)))
		return items
