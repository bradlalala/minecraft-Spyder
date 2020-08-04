# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    mc.postToChat('duck')