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

example of this can be seen in test1.py

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
   <th>b_a</th><th>a button</th>
  </tr>
  <tr>
   <th>b_b</th><th>b button</th>
  </tr>
  <tr>
   <th>b_x</th><th>x button</th>
  </tr>
  <tr>
   <th>b_y</th><th>y button</th>
  </tr>
  
  <tr>
   <th>h_u</th><th>hat up</th>
  </tr>
  <tr>
   <th>h_d</th><th>hat down</th>
  </tr>
  <tr>
   <th>h_l</th><th>hat left</th>
  </tr>
  <tr>
   <th>h_l</th><th>hat right</th>
  </tr>
  
  <tr>
   <th>b_l</th><th>left stick press</th>
  </tr>
  <tr>
   <th>b_r</th><th>right stick press</th>
  </tr>
  
  <tr>
   <th>b_back</th><th>back button</th>
  </tr>
  <tr>
   <th>b_start</th><th>start button</th>
  </tr>
  <tr>
   <th>b_xbox</th><th>guide button</th>
  </tr>
  
</table>


