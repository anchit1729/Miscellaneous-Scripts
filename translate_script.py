import googletrans
import openpyxl
import sys

filename = sys.argv[0] 
translator = googletrans.Translator()
wb = openpyxl.load_workbook(filename)
sheet = wb.active
i = 1
for row in sheet.iter_rows():
    for cell in row:
        cell.value = str(translator.translate(str(cell.value), src='de', dest='en').text)
        print("completed " + str(i) + " cells...")
print("saving translated copy of file...")
wb.save("copy of " + filename)