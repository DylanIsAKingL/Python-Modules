class counter():
	def count(start=3,secs=1,wait=1):
		debounce = False
		count = start
		
		if start < secs:
		    while debounce == False:
			    print(count)
			    count += 1
			    if count - 1 == secs:
				    debounce = True
			    else:
				    time.sleep(int(wait))
		else:
			print("end is lower than start amount or no arguments given!")
	def countdown(secs=3,start=1,wait=1):
		finished = False
		count = secs
		
		if start < secs:
			while finished == False:
				print(count)
				count -= 1
				if count + 1 == start:
					finished = True
				else:
					time.sleep(int(wait))
		else:
			print("error")
