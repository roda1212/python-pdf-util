import sys
from enum import Enum

class PageLayout(Enum):
    NoLayout = '/NoLayout'
    SinglePage = '/SinglePage'
    OneColumn = '/OneColumn'
    TwoColumnLeft = '/TwoColumnLeft'
    TwoColumnRight = '/TwoColumnRight'
    TwoPageLeft = '/TwoPageLeft'
    TwoPageRight = '/TwoPageRight'
    @classmethod
    def members(cls):
        return ', '.join([str(l.value) for l in cls])

class PageMode(Enum):
    UseNone = '/UseNone'
    UseOutlines = '/UseOutlines'
    UseThumbs = '/UseThumbs'
    FullScreen = '/FullScreen'
    UseOC = '/UseOC'
    UseAttachments = '/UseAttachments'
    @classmethod
    def members(cls):
        return ', '.join([str(l.value) for l in cls])
