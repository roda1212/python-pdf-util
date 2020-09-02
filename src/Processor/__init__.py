import sys
from enum import Enum

import PyPDF2

from .. import Log

__all__ = [ 
            'SetPassword',
            'CheckPassword',
            'SetPageLayout',
            'SetPageMode',
            'GetMetaData',
            'SetMetaData',
            ]

class Processor:
    """
    PDFファイルを加工するための汎用処理をまとめたクラス
    """
    def __init__(self, in_file:str, out_file:str):
        self.__reader = PyPDF2.PdfFileReader(in_file, strict=False)
        self.__writer = PyPDF2.PdfFileWriter()
        self.__writer.cloneReaderDocumentRoot(self.__reader)
        self.out_file = out_file
    def Process(self, processing_function, auto_copy_metadata:bool = True):
        processing_function(self.__reader, self.__writer)
        if auto_copy_metadata:
            d = {key: self.__reader.documentInfo[key] for key in self.__reader.documentInfo.keys()}
            self.__writer.addMetadata(d)
        with open(self.out_file, 'wb') as f:
            self.__writer.write(f)

def SetPassword(pdf_file:str, password:str) -> int:
    Log.Info(f"パスワードを設定します")
    p = Processor(pdf_file, 'out.pdf')
    p.Process(lambda r, w: w.encrypt(password, use_128bit=True))
    Log.Info(f"設定が完了しました")
    return 0

def CheckPassword(pdf_file:str, password:str) -> int:
    reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
    if reader.isEncrypted:
        ret = reader.decrypt(password)
        if ret == 2:
            Log.Info('パスワードが一致しました (owner)')
            return 0
        elif ret == 1:
            Log.Info('パスワードが一致しました (user)')
            return 0
        else:
            Log.Error('パスワードが一致しません')
    else:
        Log.Error('暗号化されていません')
    return 1

def SetPageLayout(pdf_file:str, page_layout:str) -> int:
    Log.Info(f"ページレイアウトを設定します : {page_layout}")
    p = Processor(pdf_file, 'out.pdf')
    p.Process(lambda r, w: w.setPageLayout(page_layout))
    Log.Info(f"設定が完了しました")
    return 0

def SetPageMode(pdf_file:str, page_mode:str) -> int:
    Log.Info(f"ページモードを設定します : {page_mode}")
    p = Processor(pdf_file, 'out.pdf')
    p.Process(lambda r, w: w.setPageMode(page_mode))
    Log.Info(f"設定が完了しました")
    return 0

def GetMetaData(pdf_file:str, name:str) -> int:
    reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
    try:
        value = reader.documentInfo[f"/{name}"]
        Log.Info(f"/{name} = {value}")
    except KeyError:
        Log.Info(f"/{name} = {None}")
    return 0

def CopyMetaDataWithChanging(reader, writer, key:str, value:str = None, delete:bool = False):
    d = {k: reader.documentInfo[k] for k in reader.documentInfo.keys()}
    if delete:
        Log.Info(f"メタデータを削除します : /{key}")
        d.pop(key)
    else:
        Log.Info(f"メタデータを設定します : /{key} = {value}")
        d[key] = value
    writer.addMetadata(d)

def SetMetaData(pdf_file:str, name:str, value:str, delete:bool) -> int:
    if len(value) == 0 and not delete: 
        return

    p = Processor(pdf_file, 'out.pdf')
    try:
        p.Process(lambda r, w: CopyMetaDataWithChanging(r, w, f"/{name}", value, delete), False)
    except KeyError:
        pass
    Log.Info(f"設定が完了しました")
