#!/usr/bin/env python

from ast import literal_eval as le

class CommandsDict(dict):
	def __init__(self):
		dict.__init__(self)

	def __getitem__(self, key):
		if isinstance(key, list): key = repr(key)
		val = dict.__getitem__(self, key)
		try: val = le(val)
		except ValueError: pass
		return val

	def __setitem__(self, key, val):
		if isinstance(key, list):
			key = repr(key)
		dict.__setitem__(self, key, val)

	def keys(self):
		keys = dict.keys(self)
		newkeys = list()
		for key in keys:
			try: key = le(key)
			except ValueError: pass
			newkeys.append(key)

		return newkeys

	def items(self):
		items = list()
		for key in self.keys():
			items.append((key, self.__getitem__(key)))
		return items