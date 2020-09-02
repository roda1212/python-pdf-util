import sys
from enum import Enum

import PyPDF2

from .. import Log

def SetPassword(pdf_file:str, password:str) -> int:
    reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
    writer = PyPDF2.PdfFileWriter()
    writer.cloneReaderDocumentRoot(reader)
    writer.encrypt(password, use_128bit=True)
    with open('out.pdf', 'wb') as f:
        writer.write(f)
    return 0

def CheckPassword(pdf_file:str, password:str) -> int:
    reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
    if reader.isEncrypted:
        ret = reader.decrypt(password)
        if ret == 2:
            Log.Info('correct password (owner)')
            return 0
        elif ret == 1:
            Log.Info('correct password (user)')
            return 0
        else:
            Log.Error('invalid password')
    else:
        Log.Error('not encrypted')
    return 1

def SetPageLayout(pdf_file:str, page_layout:str) -> int:
    reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
    writer = PyPDF2.PdfFileWriter()
    writer.cloneReaderDocumentRoot(reader)
    writer.setPageLayout(page_layout)
    with open('out.pdf', 'wb') as f:
        writer.write(f)
    return 0

def SetPageMode(pdf_file:str, page_mode:str) -> int:
    reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
    writer = PyPDF2.PdfFileWriter()
    writer.cloneReaderDocumentRoot(reader)
    writer.setPageMode(page_mode)
    with open('out.pdf', 'wb') as f:
        writer.write(f)
    return 0
