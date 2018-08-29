#!/usr/bin/python
# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create() # create Minecraft Object

x, y, z = mc.player.getPos()
mc.setBlocks(x + 2, y - 1, z + 2, x + 7, y + 3, z + 8, 5) # make shell
mc.setBlocks(x + 3, y, z + 3, x + 6, y + 2, z + 7, 0) # remove inside
mc.setBlocks(x + 2, y, z + 5, x + 2, y + 1, z + 5, 0) # make doorway
mc.setBlocks(x + 4, y + 1, z + 8, x + 5, y + 1, z + 8, 102) # make window 1
mc.setBlocks(x + 4, y + 1, z + 2, x + 5, y + 1, z + 2, 102) # make window 2
mc.setBlocks(x + 7, y + 1, z + 4, x + 7, y + 1, z + 6, 102) # make window 3
