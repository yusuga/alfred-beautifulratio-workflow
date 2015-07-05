#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
from workflow import Workflow
import math

# https://en.wikipedia.org/wiki/Golden_ratio
goldenRatio = (1 + math.sqrt(5)) / 2
# https://en.wikipedia.org/wiki/Silver_ratio
silverRatio = math.sqrt(2)

def roundedStr(num):
    return str(int(round(num)))

def main(wf):
    try:
        num = float(wf.args[0])
    except:
        wf.add_item(title = 'Invalid string', subtitle = 'Beautiful Ratio', icon = 'failure.png')
        wf.send_feedback()
        return

    wf.logger.debug(num)

    grLong = roundedStr(num * goldenRatio)
    grShort = roundedStr(num / goldenRatio)
    slLong = roundedStr(num * silverRatio)
    slShort = roundedStr(num / silverRatio)

    wf.add_item(title = grLong, subtitle = 'Golden Ratio (longer side)', arg = grLong, valid = True, icon = 'golden-ratio-longer.png')
    wf.add_item(title = grShort, subtitle = 'Golden Ratio (shorter side)', arg = grShort, valid = True, icon = 'golden-ratio-shorter.png')
    wf.add_item(title = slLong, subtitle = 'Silver Ratio (longer side)', arg = slLong, valid = True, icon = 'silver-ratio-longer.png')
    wf.add_item(title = slShort, subtitle = 'Silver Ratio (shorter side)', arg = slLong, valid = True, icon = 'silver-ratio-shorter.png')

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
