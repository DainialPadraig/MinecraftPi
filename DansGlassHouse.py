# Building a house of glass using the setBlocks command.

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# Where am I?
playerTilePos = mc.player.getTilePos()

# Build a square floor around my location (51 x 51 cubes)
mc.setBlocks(playerTilePos.x - 25, playerTilePos.y, playerTilePos.z - 25,
             playerTilePos.x + 25, playerTilePos.y, playerTilePos.z + 25,
             block.DIAMOND_BLOCK.id)

# Build a wall 5 blocks in front of me.
#mc.setBlocks(playerTilePos.x - 25, playerTilePos.y, playerTilePos.z + 5,
#             playerTilePos.x + 25, playerTilePos.y + 10, playerTilePos.z + 5,
#             block.DIAMOND_BLOCK.id)

# Add a 3 x 3 door in the center of the wall
#mc.setBlocks(playerTilePos.x - 1, playerTilePos.y, playerTilePos.z + 5,
#             playerTilePos.x + 1, playerTilePos.y + 3, playerTilePos.z + 5,
#             block.AIR.id)

# Build a side wall to the left (as you are looking at the house)
#mc.setBlocks(playerTilePos.x - 25, playerTilePos.y, playerTilePos.z + 6,
#             playerTilePos.x - 25, playerTilePos.y + 10, playerTilePos.z + 21,
#             block.DIAMOND_BLOCK.id)

# Build the side wall on the right
#mc.setBlocks(playerTilePos.x + 25, playerTilePos.y, playerTilePos.z + 6,
#             playerTilePos.x + 25, playerTilePos.y + 10, playerTilePos.z + 21,
#             block.DIAMOND_BLOCK.id)

# Build the back wall
#mc.setBlocks(playerTilePos.x - 25, playerTilePos.y, playerTilePos.z + 22,
#             playerTilePos.x + 25, playerTilePos.y + 10, playerTilePos.z + 22,
#             block.DIAMOND_BLOCK.id)

# Build a flat roof
#mc.setBlocks(playerTilePos.x - 25, playerTilePos.y + 11, playerTilePos.z + 5,
#             playerTilePos.x + 25, playerTilePos.y + 11, playerTilePos.z + 22,
#             block.DIAMOND_BLOCK.id)
