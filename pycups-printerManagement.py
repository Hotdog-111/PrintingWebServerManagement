import pycups

conn = pycups.Connection()
printers = conn.getPrinters()

for printer in printers:
    print(printer, printers[printer]["device-uri"])
