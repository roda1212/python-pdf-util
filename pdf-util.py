import argparse
from enum import Enum
import os
import sys

import src.Log as Log
import src.Processor as Processor

class Mode(Enum):
    """
    モード
    """
    SetPassword = 'SetPassword'
    CheckPassword = 'CheckPassword'
    @classmethod
    def toMode(cls, val:str):
        try:
            return Mode(val)
        except Exception:
            return None

def InitArgParser(mode:Mode) -> argparse.ArgumentParser:
    """
    引数の初期化
    """
    parser = argparse.ArgumentParser(description='PDF操作用のユーティリティ')
    parser.add_argument('mode', type=Mode, help='実行モード')
    parser.add_argument('pdf_file', type=str, help='対象PDFファイル')
    if mode == Mode.SetPassword:
        parser.add_argument('password', type=str, help='パスワード')
    elif mode == Mode.CheckPassword:
        parser.add_argument('password', type=str, help='パスワード')
    return parser

def Process(mode, args):
    if mode == Mode.SetPassword:
        Processor.SetPassword(args.pdf_file, args.password)
    elif mode == Mode.CheckPassword:
        Processor.CheckPassword(args.pdf_file, args.password)


def Main():
    mode = Mode.toMode(sys.argv[1])
    args = InitArgParser(mode).parse_args()

    if not os.path.exists(args.pdf_file):
        Log.Error(f"ファイルが見つかりません（{args.pdf_file}）")
        return

    Process(mode, args)
    

if __name__ == '__main__':
    Main()