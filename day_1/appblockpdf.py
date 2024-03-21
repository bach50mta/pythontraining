import sys
import uuid
from pypdf import PdfReader, PdfWriter

try:
    path = sys.argv[-1]
    reader= PdfReader(path)
    writer = PdfWriter()

    writer.append_pages_from_reader(reader)
    password=uuid.uuid4().hex
    print(password)

    writer.encrypt(password)

    with open(path, "wb") as out_file:
        writer.write(out_file)
except Exception:
    print("file đã được tạo mật khẩu rồi")