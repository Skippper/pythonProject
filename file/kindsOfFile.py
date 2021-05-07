import json, logging, yaml, operator, sys
from datetime import datetime
from os import path
import os

tgt = 'Echo(189****5121),吴坤(13624498255),Kiki(159****1280),王泽(138****9614)'

tgt_arr = tgt.split(',')
for i in range(len(tgt_arr)):
    if i != len(tgt_arr) -1 :
        res_str = process_str.split('(')[0] + '(' + \
                   process_str.split('(')[1][0:3] + \
                   '****' + process_str.split('(')[1][7:] + ','
