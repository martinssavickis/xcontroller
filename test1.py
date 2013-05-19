import xcontroller
import time

pad1 = xcontroller.get_controller(0)


while  True:
  time.sleep(0.1)
  # print("X: " + str(pad1.l_x()) + " Y: " + str(pad1.l_y()))
  # print("X: " + str(pad1.r_x()) + " Y: " + str(pad1.r_y()))
  # print ("LT: " + str(pad1.l_t()) + " RT: " + str(pad1.r_t()))
  # print ("up: " + str(pad1.h_u()) + " down: " + str(pad1.h_d()) + " left: " + str(pad1.h_l()) + " right: " + str(pad1.h_r()) )
  # print ("A: " + str(pad1.b_a()) + " B: " + str(pad1.b_b()) + " X: " + str(pad1.b_x()) + " Y: " + str(pad1.b_y()) )
  # print ("START: " + str(pad1.b_start()) + " BACK: " + str(pad1.b_back()) + " XBOX: " + str(pad1.b_xbox()))
  # print ("LEFT: " + str(pad1.b_l()) + " RIGHT: " + str(pad1.b_r()))

