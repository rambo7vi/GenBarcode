from barcode import EAN13
from barcode.writer import ImageWriter
num=int(input("How many Barcodes do you need to generate?"))

for i in range(num):
    id = input("Give 12 Digit numbers for your barcode id:")
    my_code=EAN13(id,writer=ImageWriter()) #default saves as png
    name= input("Give name to save barcode:")
    my_code.save(name)