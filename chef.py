class chef():
	def addto(item1,var,after=True):
	    if after == True:
		    return var + item1
	    else:
		    return item1 + var
	
	def serve(var): print(var)
	
	def cut(item1, item2, var):
		global output
		output = var[int(item1-1):int(item2)]
		return output
	
	def add(num1, num2):
		return int(num1) + int(num2)
