import subprocess
def pip_byt_slicer():
	cmd1='pip list --format json'
	r1 = subprocess.check_output(cmd1, shell=True)
	n=r1.index(b'}]')+2
	f1 = open('pip_list.json', "wb")
	f1.write(r1[0:n])
	f1.close()
	f2=open('pip_list_2.txt','wb')
	f2.write(r1[n+1:len(r1)])
  	print(r1[0:n])
  	print('--------------------')
  	print(r1[n+1:len(r1)])
pip_byt_slicer()
