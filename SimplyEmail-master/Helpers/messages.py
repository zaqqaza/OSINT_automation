from __future__ import print_function
from __future__ import absolute_import
from builtins import str
from . import helpers


def email_count(text, Module):
    Length = " [*] " + Module + \
        ": Gathered " + str(text) + " Email(s)!"
    print(helpers.color(Length, status=True))