#!/usr/bin/env python3

from getpass import getpass
from crypt import crypt

pw = getpass()
print(crypt(pw))

