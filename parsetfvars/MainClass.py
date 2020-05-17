#!/usr/bin/env python3
import re
import json


class ParseTfvars:
    """ docstring for ParseTfvars.
    trys to parse tfvars variables
    to use it on python local-exex """

    def __init__(self, file):
        self.file = file

    def simpleline(self, var):
        """ opens varfile """
        return [line for line in open(self.file).readlines() if var
                in line]

    def st(self, var):
        st = self.simpleline(var)
        return str(st[0].split('=')[1].split('"')[1])

    def nb(self, var):
        nb = self.simpleline(var)
        return int(nb[0].split('=')[1])

    def bl(self, var):
        bl = self.simpleline(var)
        return bl(bool[0].split('=')[1].title())

    def lt(self, var):
        lt = self.simpleline(var)
        return list(re.sub('"', '', re.sub(r'(^\[|\]$)', '', re.sub(r'\s', '',
                    lt[0]).replace("%s=" % var, ""))).split(","))

    def mp(self, var):
        mp = self.simpleline(var)
        var = json.loads(re.sub(r'(,)(?!.*\1)', '', re.sub(r'\]', '],',
                         re.sub(' ', '', re.sub(r'\=', ':', re.sub(r'\=',
                                ':', mp[0], count=1
                                ).split(':')[1]), count=1))))
        return var
