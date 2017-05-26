import array

Arry=array.array('B', [0]*1048576)
with open (".\zero.txt", "wb") as zero:
	for i in range(1,102400):
		zero.write(Arry)