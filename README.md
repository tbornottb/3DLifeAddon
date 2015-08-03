#3D Game of Life Addon
This script generates a customized, randomized simulation of a 3-dimensional version of Conway's Game of Life.

## Installation
Download the .py file. In Blender, go to **File->User Preferences->Install From File...** and choose the .py file. It will then appear as a button at the top of the Objects dropdown, and will be searachable in the spacebar menu (listed under "3D Life").

## Options
- The Simulations Dimensions slider allows you to set the number of cells in all three dimensions.
- The Simulation Frames allows you to change how long the simulation runs for.
- The Keyframe Step slider allows you to change how many blank frames occur between each calculated keyframe.

## Notes
The algorithm eliminates redundant keyframes - keyframes are only put at the beginning and end of each stretch of life or death. The simulation uses the "4555" ruleset for 3D Life - you can experiment by changing the ruleset, which would involve tweaking the newstatus function. 'Dead' and 'alive' are represented in this simulation by scale 0 and 1, respectively - if the Keyframe Step is greater than 1, you'll see the cells expand and contract as they change between alive and dead. 
