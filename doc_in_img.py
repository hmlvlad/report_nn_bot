from PIL import ImageGrab
from config import get_path
import win32com.client


def reform_doc(doc_name):
    xlsx_path = get_path('documents', doc_name)

    client = win32com.client.Dispatch("Excel.Application")
    wb = client.Workbooks.Open(xlsx_path)
    ws = wb.ActiveSheet

    ws.Range("A1:D6").CopyPicture(Format=2)

    img = ImageGrab.grabclipboard()
    img.save(get_path('documents', f'{doc_name[:-5]}.jpg'))

    wb.Close()  # иначе табл будет открыта
    client.Quit()

