#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import sys
from interface import Interface
#from player import Player

def main (args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    
	# parser = SafeConfigParser()
	# parser.read('etc/soundboard.ini')

	# bytes = {}
	# tmp_byte = {}
	# for section_name in parser.sections():
	# 	tmp_byte[section_name] = {}
	# 	for option in parser.options(section_name):
	# 		tmp_byte[section_name][option] = parser.get(section_name, option)

	# 	bytes[section_name] = Soundbyte(section_name, tmp_byte[section_name])

    gui = Interface()
 #   player = Player()

if __name__ == "__main__":
	main()

