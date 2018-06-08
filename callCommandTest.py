import subprocess
from subprocess import call

def getDigit():
	

	convertToImg = 'convert -density 300 out.pdf -depth 8 -strip -background white -alpha off file.tiff'
	extractDigit = 'tesseract file.tiff output.txt'
	p = subprocess.Popen(convertToImg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	retval = p.wait()
	# extractDigit
	e = subprocess.Popen(extractDigit, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


# (output, err) = e.communicate()
# for line in p.stdout.readlines():
#     print line,

"""
Another Way
"""
"""
import os
cmd = 'ls -al'
os.system(cmd)
"""