import argparse
from enum import Enum
import os
import sys

import src.Log as Log
import src.Processor as Processor
import src.Prop as Prop

class Mode(Enum):
    """
    モード
    """
    SetPassword = 'SetPassword'
    CheckPassword = 'CheckPassword'
    SetPageLayout = 'SetPageLayout'
    SetPageMode = 'SetPageMode'
    GetMetaData = 'GetMetaData'
    SetMetaData = 'SetMetaData'
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
    elif mode == Mode.SetPageLayout:
        parser.add_argument('page_layout', type=Prop.PageLayout, help=f"ページレイアウト（{Prop.PageLayout.members()}）")
    elif mode == Mode.SetPageMode:
        parser.add_argument('page_mode', type=Prop.PageMode, help=f"ページモード（{Prop.PageMode.members()}）")
    elif mode == Mode.GetMetaData:
        parser.add_argument('name', type=str, help=f"取得する情報（{Prop.MetaData.members()}, 他）")
    elif mode == Mode.SetMetaData:
        parser.add_argument('name', type=str, help=f"設定する情報（{Prop.MetaData.members()}, 他）")
        parser.add_argument('-v', '--value', type=str, help=f"設定する値", default='')
        parser.add_argument('-d', '--delete', action='store_true', help=f"削除フラグ")
    return parser

def Process(mode, args):
    """
    モードに応じた処理の実行
    """
    if mode == Mode.SetPassword:
        Processor.SetPassword(args.pdf_file, args.password)
    elif mode == Mode.CheckPassword:
        Processor.CheckPassword(args.pdf_file, args.password)
    elif mode == Mode.SetPageLayout:
        Processor.SetPageLayout(args.pdf_file, args.page_layout.value)
    elif mode == Mode.SetPageMode:
        Processor.SetPageMode(args.pdf_file, args.page_mode.value)
    elif mode == Mode.GetMetaData:
        Processor.GetMetaData(args.pdf_file, args.name)
    elif mode == Mode.SetMetaData:
        Processor.SetMetaData(args.pdf_file, args.name, args.value, args.delete)

def Main():
    mode = Mode.toMode(sys.argv[1])
    args = InitArgParser(mode).parse_args()

    if not os.path.exists(args.pdf_file):
        Log.Error(f"ファイルが見つかりません（{args.pdf_file}）")
        return

    Process(mode, args)
    

if __name__ == '__main__':
    Main()