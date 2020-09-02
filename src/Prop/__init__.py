import sys
from enum import Enum

class PropBase(Enum):
    @classmethod
    def members(cls):
        return ', '.join([str(l.value) for l in cls])

class PageLayout(PropBase):
    NoLayout = '/NoLayout'
    SinglePage = '/SinglePage'
    OneColumn = '/OneColumn'
    TwoColumnLeft = '/TwoColumnLeft'
    TwoColumnRight = '/TwoColumnRight'
    TwoPageLeft = '/TwoPageLeft'
    TwoPageRight = '/TwoPageRight'

class PageMode(PropBase):
    UseNone = '/UseNone'
    UseOutlines = '/UseOutlines'
    UseThumbs = '/UseThumbs'
    FullScreen = '/FullScreen'
    UseOC = '/UseOC'
    UseAttachments = '/UseAttachments'

class MetaData(PropBase):
    Creator = 'Creator'
    Producer = 'Producer'
    Title = 'Title'
