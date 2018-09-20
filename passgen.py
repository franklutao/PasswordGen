#!/usr/bin/env python

import secrets
import random
import string
import re


class PasswordGenerator:
    """
    Password generator - v1.0
    created by franklutao 2018/09/20
    type: l for lowercase, u for uppercase, d for digits, s for special characters,
          followed by a number indicating the minimum occurrence of each type
    for example,type={'l': 2, 'u': 1, 'd': 1, 's': 1}  length=8 will generate a password of 8 characters
    containing at least 2 lowercase, 1 uppercase,  1 digit and 1 special character.
    """

    __CORRECT_INPUT = True

    def __init__(self, chtype,  length, spc="@#$%!~"):
        """
        chtype: dict with keys of "d","l","u","s"
        length: int , length of password
        """
        self.num = {'l': 0, 'u': 0, 'd': 0, 's': 0}
        self.min_length = 0
        self.spc = spc
        self.passstr = ""

        try:
            for k, v in chtype.items():
                self.num[k] = int(v) if v != '' else 1
                self.min_length += self.num[k]

            if self.min_length > length:
                raise ValueError
        except ValueError:
            self.__CORRECT_INPUT = False

    def set_special_char(self, _spc):
        self.spc = _spc

    def set_char_types(self, _chtype):
        self.min_length = 0
        try:
            for k, v in _chtype.items():
                self.num[k] = int(v) if v != '' else 1
                self.min_length += self.num[k]

            if self.min_length > length:
                raise ValueError
        except ValueError:
            self.__CORRECT_INPUT = False

    def generate(self):

        if not self.__CORRECT_INPUT:
            return "INVALID INPUT"

        # generate each required type of string, put in a list and shuffle it
        ds = ''.join(secrets.choice(string.digits) for i in range(self.num['d']))
        ls = ''.join(secrets.choice(string.ascii_lowercase) for i in range(self.num['l']))
        us = ''.join(secrets.choice(string.ascii_uppercase) for i in range(self.num['u']))
        ss = ''.join(secrets.choice(self.spc) for i in range(self.num['s']))
        rs = ''.join(secrets.choice(string.digits+string.ascii_lowercase+string.ascii_uppercase+self.spc) for i in range(length-self.min_length))
        self.passstr = list(ds+ls+us+ss+rs)
        random.shuffle(self.passstr)

        return "".join(self.passstr)


if __name__ == '__main__':

    pattern = r'([luds])(\d*)'
    types = dict(re.findall(pattern, "l2u1d2s1"))
    length = 8
    pg = PasswordGenerator(types, length)
    print(pg.generate())
    types = dict(re.findall(pattern, "l2u1d2s4"))
    pg.set_char_types(types)
    print(pg.generate())
