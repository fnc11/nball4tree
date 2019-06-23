#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("/home/lab-mueller/Documents/AILab/cc.hi.300.vec",'r') as vec, open("data/wordEmbs.txt",'w') as word_embs:
    cont = vec.read()
    lines = cont.split('\n')
    for line in lines:
        word = line.split(" ")[0]
        word_embs.write(word+"$")