try :
	print "Enter 1 for Addition "
	print "Enter 2 for Subtraction"
	print "Enter 3 for Multiplication"
	print "Enter 4 for Divition"

	class calculator :
		def Add ( self, A, B ):
			print A + B
		def Sub (self, A, B ):
			print A - B
		def Mul (self, A, B ):
			print A * B
		def Div (self, A, B ):
			print A / B

	C = calculator()

	Input = int (raw_input ("Enter the choice:"))
	A = int (raw_input ("Enter A:"))
	B = int (raw_input ("Enter B:"))
	if Input == 1:
		C.Add (A,B)
	elif Input == 2:
		C.Sub (A,B)
	elif Input == 3:
		C.Mul (A,B)
	elif Input == 4:
		C.Div (A,B)
	elif Input <= 5:
		print "Its not avaliable try again"
		exit ()

except ValueError:
      "The value is wrong"
		