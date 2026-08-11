from extensions import mimetype 

filename = input(str("File name: "))
extension = filename.split(".")[-1]

print("MIME type:", mimetype(extension))
