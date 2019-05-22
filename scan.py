# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# simple inquiry example
import bluetooth

nearby = bluetooth.discover_devices()

for b in nearby:
    print(bluetooth.lookup_name(b))



