#!/bin/bash

pvpython py_anim_closeup.py
while [ $? != 1 ]; do
    /Applications/ParaView-5.11.0.app/Contents/bin/pvpython py_anim_closeup.py
done
