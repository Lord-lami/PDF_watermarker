import sys
import PyPDF2

pdfpath, waterpath = sys.argv[1:]

if __name__ == '__main__':
	content = PyPDF2.PdfReader(pdfpath).pages
	writer = PyPDF2.PdfWriter()
	x = 1
	for page in content:
		watermark_image = PyPDF2.PdfReader(waterpath).pages[0]
		mediabox = page.mediabox

		watermark_image.merge_page(page)
		watermark_image.mediabox = mediabox
		writer.add_page(watermark_image)
		
		print(x)
		x += 1

	name = input('What do you want to name the new file? ')
	writer.write(name)
