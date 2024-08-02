
#PASTE THE NEXT COMAND INTO A PYTHON TAB INSIDE SCRIPT EDITOR 
#THEN WITH THE MIDDLE MOUSE DRAG IT TO YOUR CUSTOM SHELF 
#EDIT THE IMAGE WITH EDIT POP UP


from Camera_Rig import cam_ui
reload(cam_ui)

cam_ui.show_ui()


#IF YOUR ARE USING PYTHON 3.4 OR LATER VERSIONS PASTE THIS INSTEAD

import importlib
from Camera_Rig import cam_ui
importlib.reload(cam_ui)

cam_ui.show_ui()


#IF IT DOESN'T WORK RUN THIS CODE FIRST REMPLACING 'YOUREQUIPMENTNAME' THEN RUN THE PREVIOUS CODE.

import sys
import maya.cmds as cmds

path_to_scripts_folder = r'C:\Users\YOUREQUIPMENTNAME\Documents\maya\scripts\Camera_Rig'
if path_to_scripts_folder not in sys.path:
    sys.path.append(path_to_scripts_folder)


#OPTIONAL: EDIT THE POP UP USING CAMARA_RIG.png AS THE IMAGE