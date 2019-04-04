import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())
# phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print (phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# beginWithHello = re.compile(r'Hello')
# beginWithHello.search('Hello word')
# beginWithHello.search('He said hello.') == None
# endWithNumber = re.compile(r'\d$')
# endWithNumber.search('Your number is 42')
# endWithNumber.search('Your number is forty two') == None
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
