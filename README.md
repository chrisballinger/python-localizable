python-localizable
==================

Localizable.strings parser for Python

# Usage

Install using pip.

    $ pip install localizable
    
You can either parse a full string directly or pass a file path:

	import localizable
	
	strings = localizable.parse_strings(filename='Localizable.strings')
	strings = localizable.parse_strings(content="content of .strings file") # this works too
	
The output format is an array of dictionaries, in order, with the following key/value pairs:

    /* Comment */
    "Key" = "Value";

 * `key`: "Key"
 * `value`: "Value"
 * `comment`: "Comment"
 
# License

GPLv2. Adapted from Transifex.