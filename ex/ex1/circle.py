#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math


if len(sys.argv) == 1:
    print("入力値がありません")
else:
    radius = sys.argv[1]

    try:
        print(float(radius) * float(radius) * math.pi)
    except:
        print("数値を入力してください")
