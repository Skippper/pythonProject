import os
import sys

v1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(v1)
res = os.path.join(v1,"base1")
print(res)
sys.path.append(res)

import loopTest
import csv






