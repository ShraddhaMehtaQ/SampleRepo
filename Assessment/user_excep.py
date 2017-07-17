class NumberTooSmallError(Exception):
	message = '\nException: NumberTooSmallError:\nYour number is too small. \nTry a bigger one!'
class NumberTooBigError(Exception):
	message = '\nException: NumberTooBigError:\nYour number is too big. \nTry a smaller one!'


def checkNumber(num):
    
    if(num < 99):
        raise NumberTooSmallError
    elif(num > 99):
        raise NumberTooBigError
    return num

usrInput = int(raw_input( "\nPlease enter the number: " ))
try:
	print checkNumber(usrInput)
except NumberTooSmallError:
       	print "Number too small"
except NumberTooBigError, e:
       	print "Number too big" + e.message
   
 