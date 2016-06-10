# STEP 1 - Import
# First, we need to import some code that other people have written to let us connect to Minecraft

#import the minecraft modules
import mcpi.minecraft as minecraft
import mcpi.block as block

#import random so you can create lights in random locations


#import time so we can put delays into our program

  
  
  
  
  
  
  
# STEP 2 - Connect
# Next, we will connect to Minecraft, by setting up a connection with minecraft.Minecraft.create() and naming it "mc":



  
  
  
  
  
# STEP 3 - Test Post
# To test the connection, try posting something to chat, using mc.postToChat("message")







# STEP 4 - Position
# Use mc.player.getTilePos() to find the player's positiona and save it as a variable called "pos"


  
  
  
  
  
  

# STEP 5 - Build The Board
# We want the game to appear just in front of the player's location.
# You can make the game board out of whatever block material you want, google for a full list of names.
# Choose two materials, one for "good" blocks, and one for "bad". I've chosen COBBLESTONE and MOSS_STONE. 

mc.setBlocks(pos.x - 1, pos.y, pos.z + 3,
             pos.x + 1, pos.y + 2, pos.z + 3,
             block.COBBLESTONE.id)








# STEP 6 - Countdown
# The player needs a warning that the game is about to start
# Use the mc.PostToChat("message") from earlier, along with time.sleep(seconds) 









# STEP 7 - Set Up Variables
# We need to keep track of a few bits of information, so we will create variables for each of them.
# We need to know how many blocks are currently bad (blocksBad) and what score the player has got (points)






# STEP 8 - Loop
# Set up a While Loop that will keep running until all the lights are bad (Hint: use blocksBad < 9)
# Remember to indent all code inside the loop



  
  
# STEP 9 - Hit Blocks
# You now need need to turn off any blocks that have turned bad.
# Most of the code for this section has been given, but make sure you understand most of it and make any needed alterations before moving on.

    # poll a list of block hits, then use for to loop through each hitBlock:
    for hitBlock in mc.events.pollBlockHits():
      
        # check if the the block in that location was bad 
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.MOSS_STONE.id:
          
            # if it was, set that location back to a good block
            mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.COBBLESTONE.id)
            
            
            # Add some code to increase score and lower the blocksBad count:
            
            
            
            

    # STEP 10 - Turn a Block Bad
    # Select a random block as our next bad block by choosing random coordinates:
    xPos = pos.x + random.randint(-1,1)
    yPos = pos.y + random.randint(0,2)
    zPos = pos.z + 3
    
    # Use mc.setBlock(x,y,z,material) to make the block at those coordinates into the bad material:
    
    
    # Increase the blocksBad count:
    
    
    
            
    # STEP 11 - Wait
    # At the end of the loop, make the game pause for a second before changing the next block.
    # Use time.sleep(seconds) like before. 0.2 is roughly the right amount, but experiment.

  
            
    
    
    
    
# STEP 12 - Gameover
# Because the loop has ended (we aren't indenting any more), we know that all of the blocks went bad.
# Display a message to the player, including points scored.














# WHAT NEXT?
# Think about what cool extra features you might want to add to your game. 
# Here are a few ideas:

# Add a message to the loop so that the player can see their score 

# The difficulty of the game is set by the waiting before changing another block, currently time.sleep(0.2)
# Inceasing this time will make it easier, decreasing will make it harder.
# Experiment and see what works best for you.

# What if the player gets things wrong and hits the wrong block?
# Can you change the program so that it changes the block to something else?
# This forces the player to think more about what block they are hitting and increases the skill required.

# It is common for video games to start easy and get harder.
# Can you make the game start easier and the more points you score, the harder it gets?

# If you've used Python Functions before, try to rearrange and separate your code so that it all lies in neat functions.
