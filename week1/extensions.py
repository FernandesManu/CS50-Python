def mimetype(extension):
    match extension.lower():
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "gif":
            return "image/gif"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case _:
            return "application/octet-stream"