from enum import Enum

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
