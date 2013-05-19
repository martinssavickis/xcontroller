xcontroller 
================================

library for easy access to xbox 360 controller, and probably others too

Requiremets
-------------------------

[pygame library](http://www.pygame.org/)
[xboxdrv](http://pingus.seul.org/~grumbel/xboxdrv/)

Instruction
-------------------------

Import xcontroller.py

call xcontrollet.get_count() to get number of controllers

call pad = xcontroller.get_controller( i ) to get i'th controller 

call pad.l_x() for value of x axis of left stick

Commands
-------------------------

<table>
  <tr>
   <th>l_x</th><th>left stick x axis</th>
  </tr>
  <tr>
   <th>l_y</th><th>left stick y axis</th>
  </tr>
  <tr>
   <th>r_x</th><th>right stick x axis</th>
  </tr>
  <tr>
   <th>r_y</th><th>right stick y axis</th>
  </tr>
  
  <tr>
   <th>l_t</th><th>left trigger</th>
  </tr>
  <tr>
   <th>r_t</th><th>right trigger</th>
  </tr>
  
  <tr>
   <th>l_b</th><th>left button</th>
  </tr>
  <tr>
   <th>r_b</th><th>right button</th>
  </tr>
  
  <tr>
   <th>b_a</th><th>left stick y axis</th>
  </tr>
  <tr>
   <th>b_a</th><th>left stick y axis</th>
  </tr>
  
</table>


