# FlatWorld
# Create a flat world of 101 x 101 cubes (the typical Minecraft Pi
# world is 255 x 255 cubes, but it is not necessarily centered on
# the origin.

# Import libraries needed by the program.
import mcpi.minecraft as minecraft
import mcpi.block as block

# Make a connection to the running minecraft server.
mc = minecraft.Minecraft.create()

# Create a 101 x 101 cube granite surface.
mc.setBlocks(-50, 0, -50, 50, 0, 50, block.GLOWING_OBSIDIAN.id)






