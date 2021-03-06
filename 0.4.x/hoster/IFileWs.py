# -*- coding: utf-8 -*-

from ..internal.DeadHoster import DeadHoster


class IFileWs(DeadHoster):
    __name__ = "IFileWs"
    __type__ = "hoster"
    __version__ = "0.06"
    __status__ = "stable"

    __pattern__ = r'http://(?:www\.)?ifile\.ws/\w{12}'
    __config__ = []  # @TODO: Remove in 0.4.10

    __description__ = """Ifile.ws hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("z00nx", "z00nx0@gmail.com")]
