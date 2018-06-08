from PyPDF2 import PdfFileReader, utils, PdfFileWriter
from StringIO import StringIO
import subprocess
from subprocess import call
import callCommandTest as cct


input_path = 'in.pdf'

def decompress_pdf(temp_buffer):
    temp_buffer.seek(0)  # Make sure we're at the start of the file.

    process = subprocess.Popen(['pdftk.exe',
                                '-',  # Read from stdin.
                                'output',
                                '-',  # Write to stdout.
                                'uncompress'],
                                stdin=temp_buffer,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return StringIO(stdout)

with open(input_path, 'rb') as input_file:
    input_buffer = StringIO(input_file.read())

try:
    input_pdf = PdfFileReader(input_buffer)
except utils.PdfReadError:
    input_pdf = PdfFileReader(decompress_pdf(input_file))

output = PdfFileWriter()

numPages = input_pdf.getNumPages()
print "document has %s pages." % numPages

# for i in range(numPages):
page = input_pdf.getPage(0)
print page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
page.trimBox.lowerLeft = (225, 200)
page.trimBox.upperRight = (25, 1000)
page.cropBox.lowerLeft = (350, 100) #x, y
page.cropBox.upperRight = (800, 140) #go low 140
output.addPage(page)

with open("out.pdf", "wb") as out_f:
    output.write(out_f)
cct.getDigit()
