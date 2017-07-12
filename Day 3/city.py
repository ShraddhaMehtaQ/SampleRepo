city = {'chennai':'tamil nadu',
 'mumbai':'maharashtra',
 'bangalore':'karnataka',
 'delhi':'delhi', 'nagpur':'maharashtra',
 'kharagpur':'west bengal'}


inp= raw_input('enter city name from \nchennai ,mumbai ,delhi ,bangalore ,delhi ,nagpur ,kharagpur : ')

print ("\n {}".format(city[str.lower(inp)]))

