# How to use
1. download this repo.
2. put your PDF file, named in.pdf, in the same folder.
3. Specify the "crop box" you would like the information to be extracted in 
4. run python2 cropAccountNoFromPDF
5. Information will be in the output.txt! Yay!

# Dependencies
## Homebrew manage package:
1. brew install tesseract
2. brew install ImageMagick
## Python Package: PyPDF2
1. pip install PyPDF2

# Operation: what the program will do
1. crop PDF (in.pdf) to a small PDF with the size you 
2. convert PDF to tiff
3. OCR to get the information you need from the tiff
4. write the OCR output into output.txt

# Future Upgrades (TODO):
0. before upload, pop up window letting user enter page, media box and crop box number.
1. pop up a PDF Viewer to let user choose which part (page, media box and crop box) to crop.
2. upgrade to python3
