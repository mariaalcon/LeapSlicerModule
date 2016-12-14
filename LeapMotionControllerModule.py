import os, string, sys, inspect
import unittest
import vtk, qt, ctk, slicer
import logging
import importlib
import Leap
from slicer.ScriptedLoadableModule import *
import os
from __main__ import vtk, qt, ctk, slicer

#
# LeapMotionControllerModule
#

class LeapMotionControllerModule(ScriptedLoadableModule):

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = 'LeapMotionControllerModule'
        self.parent.categories = ['Gesture Control']
        self.parent.dependencies = []
        self.parent.contributors = ['Maria Alcon']
        self.parent.helpText = 'Slicer module that allows Slicer manipulation through the LeapMotion Controller'
        self.parent.acknowledgementText = ' '
        self.parent = parent

        # Create the logic to start processing Leap messages on Slicer startup
        logic = LeapMotionControllerModuleLogic()


#
# qSlicerLeapModuleWidget
#

class LeapMotionControllerModuleWidget(ScriptedLoadableModuleWidget):

    """Main widget that controls the UI"""

    def setup(self):
        ScriptedLoadableModuleWidget.setup(self)
    # def __init__(self, parent = None):
    #     if not parent:
    #       self.parent = slicer.qMRMLWidget()
    #       self.parent.setLayout(qt.QVBoxLayout())
    #       self.parent.setMRMLScene(slicer.mrmlScene)
    #     else:
    #       self.parent = parent
    #       self.layout = self.parent.layout()
    #     if not parent:
    #       self.setup()
    #       self.parent.show()
 
    # def setup(self):
    #     # Instantiate and connect widgets ...
     
    #     #
    #     # Reload and Test area
    #     #
    #     reloadCollapsibleButton = ctk.ctkCollapsibleButton()
    #     reloadCollapsibleButton.text = "Reload && Test"
    #     self.layout.addWidget(reloadCollapsibleButton)
    #     reloadFormLayout = qt.QFormLayout(reloadCollapsibleButton)
     
    #     # reload button
    #     # (use this during development, but remove it when delivering
    #     #  your module to users)
    #     self.reloadButton = qt.QPushButton("Reload")
    #     self.reloadButton.toolTip = "Reload this module."
    #     self.reloadButton.name = "LeapMotionControllerModule Reload"
    #     reloadFormLayout.addWidget(self.reloadButton)
    #     self.reloadButton.connect('clicked()', self.onReload)
     
    #     # reload and test button
    #     # (use this during development, but remove it when delivering
    #     #  your module to users)
    #     self.reloadAndTestButton = qt.QPushButton("Reload and Test")
    #     self.reloadAndTestButton.toolTip = "Reload this module and then run the self tests."
    #     reloadFormLayout.addWidget(self.reloadAndTestButton)
    #     self.reloadAndTestButton.connect('clicked()', self.onReloadAndTest)
    
    #     # Add vertical spacer
    #     self.layout.addStretch(1)

    # def cleanup(self):
    #     pass
    
    # def onReload(self,moduleName="LeapMotionControllerModule"):
    #     """Generic reload method for any scripted module.
    #     ModuleWizard will subsitute correct default moduleName.
    #     """
    #     import imp, sys, os, slicer
     
    #     widgetName = moduleName + "Widget"
     
    #     # reload the source code
    #     # - set source file path
    #     # - load the module to the global space
    #     filePath = eval('slicer.modules.%s.path' % moduleName.lower())
    #     p = os.path.dirname(filePath)
    #     if not sys.path.__contains__(p):
    #       sys.path.insert(0,p)
    #     fp = open(filePath, "r")
    #     globals()[moduleName] = imp.load_module(
    #         moduleName, fp, filePath, ('.py', 'r', imp.PY_SOURCE))
    #     fp.close()
     
    #     # rebuild the widget
    #     # - find and hide the existing widget
    #     # - create a new widget in the existing parent
    #     parent = slicer.util.findChildren(name='%s Reload' % moduleName)[0].parent().parent()
    #     for child in parent.children():
    #       try:
    #         child.hide()
    #       except AttributeError:
    #         pass
    #     # Remove spacer items
    #     item = parent.layout().itemAt(0)
    #     while item:
    #       parent.layout().removeItem(item)
    #       item = parent.layout().itemAt(0)
     
    #     # delete the old widget instance
    #     if hasattr(globals()['slicer'].modules, widgetName):
    #       getattr(globals()['slicer'].modules, widgetName).cleanup()
     
    #     # create new widget inside existing parent
    #     globals()[widgetName.lower()] = eval(
    #         'globals()["%s"].%s(parent)' % (moduleName, widgetName))
    #     globals()[widgetName.lower()].setup()
    #     setattr(globals()['slicer'].modules, widgetName, globals()[widgetName.lower()])
     
    # def onReloadAndTest(self,moduleName="LeapMotionControllerModule"):
    #     try:
    #       self.onReload()
    #       evalString = 'globals()["%s"].%sTest()' % (moduleName, moduleName)
    #       tester = eval(evalString)
    #       tester.runTest()
    #     except Exception, e:
    #       import traceback
    #       traceback.print_exc()
    #       qt.QMessageBox.warning(slicer.util.mainWindow(), 
    #           "Reload and Test", 'Exception!\n\n' + str(e) + "\n\nSee Python Console for Stack Trace")



#
# LeapMotionControllerModuleLogic
#

class LeapMotionControllerModuleLogic(ScriptedLoadableModuleLogic):
 #"""The actual brain in the application, this binds all the leapmotion gestures to the slicer commands and executes the script"""

    def __init__(self):
        import Leap
        print 'Initiation Leap Controller Reads'
        self.controller = Leap.Controller()   
        self.listener = LeapMotionListener(self.controller)
        #self.controller = Leap.Controller()
        # self.finger_names = ['Thumb', 'Index','Middle','Ring','Pinky']
        # self.enable_axis_change = False
        # self.thumb_gesture_started = False 
        # self.ending_gesture_started = False
        # self.initial_gesture_done = False
        # self.ending_gesture_done = False
        # self.axis_selected = ""
        # self.gesture_time_elapsed = 0
        # self.first_time_position = True
        # self.first_index_position = 0
        # self.last_distance = 0
        # self.distance_last_time = True
        # self.choose_brillo_contraste_navegacion = False
        # self.enable_brillo = False
        # self.enable_contraste = False
        # self.enable_navegacion = False
        # self.distance = 0
        # self.enable_zoom = False
        # self.enable_nav_brillo_contr = False
        # self.gestureDetected = ""
        # self.zoomFactor = 1
        # self.contrasteFactor = 0
        # self.brightnessFactor = 0
        # self.offset = 0
        self.listener.start(self.controller)

    # def __init__(self):
    #     print 'Initiation Leap Controller Reads'
    #     self.controller = Leap.Controller()
    #     self.listener = LeapMotionListener(self.controller)
    #     self.slicer = Slicer()

    # def stop(self):
    #     print 'Stopping Leap Controller Reads'
    #     self.listener.stop()

    # def onFrame(self):

    #     frame = self.LeapController.frame()
        
    #     print "Frame ID: "      + str(frame.id)\
    #         + "Timestamp: "     + str(frame.timestamp)\
    #         + "# of hands: "    + str(len(frame.hands))\
    #         + "# of Fingers: "  + str(len(frame.fingers))\
    #         + "# of Tools: "    + str(len(frame.tools))\
    #         + "# of Gestures: " + str(len(frame.gestures()))
        

    #     for hand in frame.hands:
    #         handType = "Left Hand" if hand.is_left else "Right Hand"
    #         lifetime_of_this_hand_object = hand.time_visible
    #         #print lifetime_of_this_hand_object
    #         # print handType + "Hand ID: " + str(hand.id) + " Palm position: " + str(hand.palm_position)
           
    #         for finger in hand.fingers:
    #             extended_finger_list = frame.fingers.extended()
    #             if len(extended_finger_list) == 0 and self.initial_gesture_done:
    #                 print "Gesto final"
    #                 if not self.ending_gesture_started:
    #                     self.ending_gesture_started = True
    #                     self.gesture_time_elapsed = time.time()

    #                 if self.ending_gesture_started and (time.time() - self.gesture_time_elapsed >= 2):
    #                     self.ending_gesture_done = True
    #                     self.initial_gesture_done = False
    #                     self.ending_gesture_started = False
    #                     gestureDetected = "Final"
    #                     print "Deteccion deshabilitada"
                    
    #             for finger in extended_finger_list:                    
    #                 #print str(len(extended_finger_list))

    #                 if not self.ending_gesture_done:
    #                     if len(extended_finger_list) == 5 and lifetime_of_this_hand_object >=5 and not self.initial_gesture_done:
    #                         gestureDetected ="inicial"
    #                         self.enable_axis_change = True
    #                         self.initial_gesture_done = True
    #                         self.gesture_time_elapsed = time.time()
    #                         gestureDetected = "Inicial"
    #                         print "Deteccion habilitada"
    #                         print "Modo seleccion de eje"

    #                     ################## Elegimos el eje en el que queremos realizar la transformacion#######################

    #                     if self.initial_gesture_done and self.enable_axis_change:

    #                         if hand.fingers.finger_type(finger.TYPE_INDEX)[0].is_extended and len(extended_finger_list) == 1 :
    #                             gestureDetected = "axial"
    #                             if self.axis_selected != "axial":
    #                                 self.gesture_time_elapsed = time.time()
    #                             self.axis_selected = "axial"
    #                             print "Gesto axial" + str(self.enable_axis_change)
    #                             if time.time() - self.gesture_time_elapsed >= 2:
    #                                 self.enable_axis_change = False
    #                                 self.thumb_gesture_started = False
    #                                 gestureDetected = "Axial"
    #                                 print "Eje axial activado"

    #                         if self.finger_names[finger.type] == "Middle" and len(extended_finger_list) == 2 :
    #                             gestureDetected = "sagital"
    #                             if self.axis_selected != "sagital":
    #                                 self.gesture_time_elapsed = time.time()
    #                             self.axis_selected = "sagital"
    #                             print "Gesto sagital" + str(self.enable_axis_change)
    #                             if time.time() - self.gesture_time_elapsed >= 2:
    #                                 self.enable_axis_change = False
    #                                 self.thumb_gesture_started = False
    #                                 gestureDetected = "Sagital"
    #                                 print "Eje sagital activado"

    #                         if self.finger_names[finger.type] == "Ring" and len(extended_finger_list) == 3 :
    #                             gestureDetected = "coronal"
    #                             if self.axis_selected != "coronal":
    #                                 self.gesture_time_elapsed = time.time()
    #                             self.axis_selected = "coronal"
    #                             print "Gesto coronal" + str(self.enable_axis_change)

    #                             if time.time() - self.gesture_time_elapsed >= 2:
    #                                 self.enable_axis_change = False
    #                                 self.thumb_gesture_started = False
    #                                 gestureDetected = "Coronal"
    #                                 print "Eje coronal activado"

                            

    #                     ######################## Elegimos la transformacion que queremos relizar ##############################

    #                     if self.initial_gesture_done and not self.enable_axis_change:

    #                         ##########################################ZOOM########################################

    #                         if not self.enable_nav_brillo_contr  and len(extended_finger_list) == 2 and hand.fingers.finger_type(finger.TYPE_INDEX)[0].is_extended and hand.fingers.finger_type(finger.TYPE_THUMB)[0].is_extended:
    #                             self.enable_zoom = True
    #                             self.thumb_gesture_started = False
    #                             index_finger = hand.fingers.finger_type(finger.TYPE_INDEX)[0]
    #                             thumb = hand.fingers.finger_type(finger.TYPE_THUMB)[0]
                                
    #                             if self.distance_last_time:
    #                                 self.last_distance = index_finger.tip_position.distance_to(thumb.tip_position)
    #                                 self.distance_last_time = False
    #                                 #print "Last distance: " + str(self.last_distance)
                                    

    #                             if not self.distance_last_time:
    #                                 distance = index_finger.tip_position.distance_to(thumb.tip_position)
    #                                 zoomFactor = self.last_distance / distance
                                    
    #                                 if distance > self.last_distance and math.fabs(distance - self.last_distance) > 5:
    #                                     gestureDetected = "In"
    #                                     Slicer.zoom(self.axis_selected, zoomFactor)
    #                                     print "Zoom In"
    #                                     print "Resta ->" + str(math.fabs(distance - self.last_distance))
    #                                     print "ZoomFactor ->" + str(zoomFactor)
    #                                     self.distance_last_time = True
    #                                 elif (distance < self.last_distance and math.fabs(distance - self.last_distance) > 5):
    #                                     gestureDetected = "Out"
    #                                     Slicer.zoom(self.axis_selected, zoomFactor)
    #                                     print "Zoom In"
    #                                     print "Zoom Out"
    #                                     print "Resta ->" + str(math.fabs(distance - self.last_distance))
    #                                     print "ZoomFactor ->" + str(zoomFactor)
    #                                     self.distance_last_time = True

                                
                                
    #                         ##################################### Navegacion, Brillo, Contraste #######################################

    #                         if not self.enable_zoom and len(extended_finger_list) == 2 and hand.fingers.finger_type(finger.TYPE_INDEX)[0].is_extended and hand.fingers.finger_type(finger.TYPE_MIDDLE)[0].is_extended :
    #                             self.enable_nav_brillo_contr = True
    #                             self.thumb_gesture_started = False
    #                             index_finger = hand.fingers.finger_type(finger.TYPE_INDEX)[0]
    #                             middle_finger = hand.fingers.finger_type(finger.TYPE_MIDDLE)[0]

    #                             if self.first_time_position:
    #                                 self.first_index_position = index_finger.tip_position
    #                                 self.first_time_position = False
    #                                 self.choose_brillo_contraste_navegacion = True
    #                                 print "First: " + str(self.first_index_position)


    #                             if self.choose_brillo_contraste_navegacion:
    #                                 print "Elige Brillo, Contraste o Navegacion"
    #                                 index_position_after_two_seconds = index_finger.tip_position 

    #                                 if (math.fabs(index_position_after_two_seconds.x - self.first_index_position.x) > math.fabs(index_position_after_two_seconds.y - self.first_index_position.y)) and (math.fabs(index_position_after_two_seconds.x - self.first_index_position.x) > math.fabs(index_position_after_two_seconds.z - self.first_index_position.z)):
    #                                     self.enable_navegacion = True
    #                                     self.choose_brillo_contraste_navegacion = False
    #                                     print "Navegacion"
    #                                 elif (math.fabs(index_position_after_two_seconds.y - self.first_index_position.y) > math.fabs(index_position_after_two_seconds.x - self.first_index_position.x)) and (math.fabs(index_position_after_two_seconds.y - self.first_index_position.y) > math.fabs(index_position_after_two_seconds.z - self.first_index_position.z)):
    #                                     self.enable_brillo = True
    #                                     self.choose_brillo_contraste_navegacion = False
    #                                     print "Brillo"
    #                                 elif (math.fabs(index_position_after_two_seconds.z - self.first_index_position.z) > math.fabs(index_position_after_two_seconds.x - self.first_index_position.x)) and (math.fabs(index_position_after_two_seconds.z - self.first_index_position.z) > math.fabs(index_position_after_two_seconds.y - self.first_index_position.y)):
    #                                     self.enable_contraste = True
    #                                     self.choose_brillo_contraste_navegacion = False
    #                                     print "Contraste"


    #                             if not self.first_time_position and not self.choose_brillo_contraste_navegacion:

    #                                 index_position = index_finger.tip_position

    #                                 if self.enable_navegacion:
    #                                     self.offset = index_position.x
    #                                     Slicer.navegacion(self.axis_selected, self.offset)

    #                                     if(index_position.x >= self.first_index_position.x and math.fabs(index_position.x) > math.fabs(index_position.y)):
    #                                         gestureDetected = "Navegacion_Derecha"
    #                                         print "Navegacion derecha -> " + str (index_position.x)
    #                                     elif (index_position.x < self.first_index_position.x and math.fabs(index_position.x) > math.fabs(index_position.y)):
    #                                         gestureDetected = "Navegacion_Izquierda"
    #                                         print "Navegacion izquierda->" + str (index_position.x)


    #                                 if self.enable_brillo:
    #                                     self.brightnessFactor = index_position.y
    #                                     slicer.brillo(self.brightnessFactor)

    #                                     if (index_position.y > self.first_index_position.y and math.fabs(index_position.x) < math.fabs(index_position.y)):
    #                                         gestureDetected = "Brillo_Aumenta"
    #                                         print "Aumenta Brillo ->" + str (self.brightnessFactor)
    #                                     elif (index_position.y < self.first_index_position.y and math.fabs(index_position.x) < math.fabs(index_position.y)):
    #                                         gestureDetected = "Brillo_Disminuye"
    #                                         print "Disminuye Brillo ->" + str (self.brightnessFactor)

    #                                 if self.enable_contraste:
    #                                     self.contrasteFactor = index_position.z
    #                                     slicer.contrasteFactor(self.contrasteFactor)

    #                                     if (index_position.z > 0):
    #                                         gestureDetected = "Contraste_Disminuye"
    #                                         print "Disminuye Contraste ->" + str (self.contrasteFactor)
    #                                     elif (index_position.z < 0):
    #                                         gestureDetected = "Contraste_Aumenta"
    #                                         print "Aumenta Contraste ->" + str (self.contrasteFactor)


    #                         ########################### Salimos a elegir otro eje o finalizar ##############################
    #                         if hand.fingers.finger_type(finger.TYPE_THUMB)[0].is_extended and len(extended_finger_list) == 1:
    #                             print "Gesto pulgar"
    #                             if not self.thumb_gesture_started:
    #                                 self.thumb_gesture_started = True
    #                                 self.gesture_time_elapsed = time.time()
    #                             if self.thumb_gesture_started and (time.time() - self.gesture_time_elapsed >= 2):
    #                                 self.gesture_time_elapsed = time.time()
    #                                 self.enable_zoom = False
    #                                 self.enable_nav_brillo_contr = False
    #                                 self.enable_axis_change = True
    #                                 self.thumb_gesture_started = False
    #                                 self.axis_selected = ""
    #                                 print "Gesto pulgar Activado" 
    #                                 print "Modo seleccion de eje"

class Slicer:
 """Manipulates the camera for looking at the object"""
 def __init__(self):
  self.camera = slicer.util.getNode('Default Scene Camera')
  self.camera.SetAndObserveTransformNodeID(self.transform.GetID())
  self.vtkcam = self.camera.GetCamera()
  self.matrix = vtk.vtkTransform()

 def zoom(self, axis_selected, zoomFactor):
  lm = slicer.app.layoutManager()

  if axis_selected == "axial":
   red = lm.sliceWidget('Red')
   redLogic = red.sliceLogic()
   redSliceNode = redLogic.GetSliceNode()
   fov_red= redSliceNode.GetFieldOfView()
   redSliceNode.SetFieldOfView(fov_red[0]*zoomFactor, fov_red[1]*zoomFactor, fov_red[2])
  elif axis_selected == "sagital":
   yellow = lm.sliceWidget('Yellow')
   yellowLogic = yellow.sliceLogic()
   yellowSliceNode = yellowLogic.GetSliceNode()
   fov_yellow = yellowSliceNode.GetFieldOfView()
   sliceNode.SetFieldOfView(fov_yellow[0]*zoomFactor, fov_yellow[1]*zoomFactor, fov_yellow[2])
  elif axis_selected == "coronal":
   green = lm.sliceWidget('Green')
   greenLogic = green.sliceLogic()
   greenSliceNode = greenLogic.GetSliceNode()
   fov_green = greenSliceNode.GetFieldOfView()
   greenSliceNode.SetFieldOfView(fov_green[0]*zoomFactor, fov_green[1]*zoomFactor, fov_green[2])

 def brillo(self, brightnessFactor):
  volumeNode = getNode('MRHead')
  displayNode = volumeNode.GetDisplayNode()
  displayNode.AutoWindowLevelOff()
  displayNode.SetLevel(brightnessFactor)

 def contraste(self, contrasteFactor):
  volumeNode = getNode('MRHead')
  displayNode = volumeNode.GetDisplayNode()
  displayNode.AutoWindowLevelOff()
  displayNode.SetWindow(contrasteFactor) 

 def navegacion (self, axis_selected, offset):
  lm = slicer.app.layoutManager()
  if axis_selected == "axial": 
   red = lm.sliceWidget('Red')
   redLogic = red.sliceLogic()
   # Change slice position
   redLogic.SetSliceOffset(offset)
  elif (axis_selected == "sagital"):
   yellow = lm.sliceWidget('Yellow')
   yellowLogic = yellow.sliceLogic()
   # Change slice position
   yellowLogic.SetSliceOffset(offset)
  elif (axis_selected == "coronal"):
   green = lm.sliceWidget('Green')
   greenLogic = green.sliceLogic()
   # Change slice position
   greenLogic.SetSliceOffset(offset)
   
  
class LeapMotionListener(Leap.Listener):

 def __init__(self, controller):
  super(LeapMotionListener, self).__init__()  
  self.controller = controller
  self.finger_names = ['Thumb', 'Index','Middle','Ring','Pinky']
  self.enable_axis_change = False
  self.thumb_gesture_started = False 
  self.ending_gesture_started = False
  self.initial_gesture_done = False
  self.ending_gesture_done = False
  self.axis_selected = ""
  self.gesture_time_elapsed = 0
  self.first_time_position = True
  self.first_index_position = 0
  self.last_distance = 0
  self.distance_last_time = True
  self.choose_brillo_contraste_navegacion = False
  self.enable_brillo = False
  self.enable_contraste = False
  self.enable_navegacion = False
  self.distance = 0
  self.enable_zoom = False
  self.enable_nav_brillo_contr = False
  self.gestureDetected = ""
  self.zoomFactor = 1
  self.contrasteFactor = 0
  self.brightnessFactor = 0
  self.offset = 0


 def on_init(self,controller):
  print ("Inicializated")
     
 def on_connect(self,controller):
  print ("Motion Sensor Connected")

 def on_disconnect(self,controller):
  print ("Motion sensor disconnected")

 def on_exit(self, controller):
  print ("Exited")

 def start(self,controller):
  self.on_frame(controller)

 def on_frame(self, controller):
  self.frame = controller.frame()
  print self.frame
  print "hola"

  print "Frame ID: "      + str(self.frame.id)\
            + "Timestamp: "     + str(self.frame.timestamp)\
            + "# of hands: "    + str(len(self.frame.hands))\
            + "# of Fingers: "  + str(len(self.frame.fingers))\
            + "# of Tools: "    + str(len(self.frame.tools))\
            + "# of Gestures: " + str(len(self.frame.gestures()))
  
  for hand in self.frame.hands:
      print "mano"
      handType = "Left Hand" if hand.is_left else "Right Hand"
      lifetime_of_this_hand_object = hand.time_visible
      #print lifetime_of_this_hand_object
      # print handType + "Hand ID: " + str(hand.id) + " Palm position: " + str(hand.palm_position)
     
      for finger in hand.fingers:
          extended_finger_list = self.frame.fingers.extended()
          if len(extended_finger_list) == 0 and self.initial_gesture_done:
              print "Gesto final"
              if not self.ending_gesture_started:
                  self.ending_gesture_started = True
                  self.gesture_time_elapsed = time.time()

              if self.ending_gesture_started and (time.time() - self.gesture_time_elapsed >= 2):
                  self.ending_gesture_done = True
                  self.initial_gesture_done = False
                  self.ending_gesture_started = False
                  gestureDetected = "Final"
                  print "Deteccion deshabilitada"
              
          for finger in extended_finger_list:                    
              #print str(len(extended_finger_list))

              if not self.ending_gesture_done:
                  if len(extended_finger_list) == 5 and lifetime_of_this_hand_object >=5 and not self.initial_gesture_done:
                      gestureDetected ="inicial"
                      self.enable_axis_change = True
                      self.initial_gesture_done = True
                      self.gesture_time_elapsed = time.time()
                      gestureDetected = "Inicial"
                      print "Deteccion habilitada"
                      print "Modo seleccion de eje"

                  ################## Elegimos el eje en el que queremos realizar la transformacion#######################

                  if self.initial_gesture_done and self.enable_axis_change:

                      if hand.fingers.finger_type(finger.TYPE_INDEX)[0].is_extended and len(extended_finger_list) == 1 :
                          gestureDetected = "axial"
                          if self.axis_selected != "axial":
                              self.gesture_time_elapsed = time.time()
                          self.axis_selected = "axial"
                          print "Gesto axial" + str(self.enable_axis_change)
                          if time.time() - self.gesture_time_elapsed >= 2:
                              self.enable_axis_change = False
                              self.thumb_gesture_started = False
                              gestureDetected = "Axial"
                              print "Eje axial activado"

                      if self.finger_names[finger.type] == "Middle" and len(extended_finger_list) == 2 :
                          gestureDetected = "sagital"
                          if self.axis_selected != "sagital":
                              self.gesture_time_elapsed = time.time()
                          self.axis_selected = "sagital"
                          print "Gesto sagital" + str(self.enable_axis_change)
                          if time.time() - self.gesture_time_elapsed >= 2:
                              self.enable_axis_change = False
                              self.thumb_gesture_started = False
                              gestureDetected = "Sagital"
                              print "Eje sagital activado"

                      if self.finger_names[finger.type] == "Ring" and len(extended_finger_list) == 3 :
                          gestureDetected = "coronal"
                          if self.axis_selected != "coronal":
                              self.gesture_time_elapsed = time.time()
                          self.axis_selected = "coronal"
                          print "Gesto coronal" + str(self.enable_axis_change)

                          if time.time() - self.gesture_time_elapsed >= 2:
                              self.enable_axis_change = False
                              self.thumb_gesture_started = False
                              gestureDetected = "Coronal"
                              print "Eje coronal activado"

                      

                  ######################## Elegimos la transformacion que queremos relizar ##############################

                  if self.initial_gesture_done and not self.enable_axis_change:

                      ##########################################ZOOM########################################

                      if not self.enable_nav_brillo_contr  and len(extended_finger_list) == 2 and hand.fingers.finger_type(finger.TYPE_INDEX)[0].is_extended and hand.fingers.finger_type(finger.TYPE_THUMB)[0].is_extended:
                          self.enable_zoom = True
                          self.thumb_gesture_started = False
                          index_finger = hand.fingers.finger_type(finger.TYPE_INDEX)[0]
                          thumb = hand.fingers.finger_type(finger.TYPE_THUMB)[0]
                          
                          if self.distance_last_time:
                              self.last_distance = index_finger.tip_position.distance_to(thumb.tip_position)
                              self.distance_last_time = False
                              #print "Last distance: " + str(self.last_distance)
                              

                          if not self.distance_last_time:
                              distance = index_finger.tip_position.distance_to(thumb.tip_position)
                              zoomFactor = self.last_distance / distance
                              
                              if distance > self.last_distance and math.fabs(distance - self.last_distance) > 5:
                                  gestureDetected = "In"
                                  Slicer.zoom(self.axis_selected, zoomFactor)
                                  print "Zoom In"
                                  print "Resta ->" + str(math.fabs(distance - self.last_distance))
                                  print "ZoomFactor ->" + str(zoomFactor)
                                  self.distance_last_time = True
                              elif (distance < self.last_distance and math.fabs(distance - self.last_distance) > 5):
                                  gestureDetected = "Out"
                                  Slicer.zoom(self.axis_selected, zoomFactor)
                                  print "Zoom In"
                                  print "Zoom Out"
                                  print "Resta ->" + str(math.fabs(distance - self.last_distance))
                                  print "ZoomFactor ->" + str(zoomFactor)
                                  self.distance_last_time = True

                          
                          
                      ##################################### Navegacion, Brillo, Contraste #######################################

                      if not self.enable_zoom and len(extended_finger_list) == 2 and hand.fingers.finger_type(finger.TYPE_INDEX)[0].is_extended and hand.fingers.finger_type(finger.TYPE_MIDDLE)[0].is_extended :
                          self.enable_nav_brillo_contr = True
                          self.thumb_gesture_started = False
                          index_finger = hand.fingers.finger_type(finger.TYPE_INDEX)[0]
                          middle_finger = hand.fingers.finger_type(finger.TYPE_MIDDLE)[0]

                          if self.first_time_position:
                              self.first_index_position = index_finger.tip_position
                              self.first_time_position = False
                              self.choose_brillo_contraste_navegacion = True
                              print "First: " + str(self.first_index_position)


                          if self.choose_brillo_contraste_navegacion:
                              print "Elige Brillo, Contraste o Navegacion"
                              index_position_after_two_seconds = index_finger.tip_position 

                              if (math.fabs(index_position_after_two_seconds.x - self.first_index_position.x) > math.fabs(index_position_after_two_seconds.y - self.first_index_position.y)) and (math.fabs(index_position_after_two_seconds.x - self.first_index_position.x) > math.fabs(index_position_after_two_seconds.z - self.first_index_position.z)):
                                  self.enable_navegacion = True
                                  self.choose_brillo_contraste_navegacion = False
                                  print "Navegacion"
                              elif (math.fabs(index_position_after_two_seconds.y - self.first_index_position.y) > math.fabs(index_position_after_two_seconds.x - self.first_index_position.x)) and (math.fabs(index_position_after_two_seconds.y - self.first_index_position.y) > math.fabs(index_position_after_two_seconds.z - self.first_index_position.z)):
                                  self.enable_brillo = True
                                  self.choose_brillo_contraste_navegacion = False
                                  print "Brillo"
                              elif (math.fabs(index_position_after_two_seconds.z - self.first_index_position.z) > math.fabs(index_position_after_two_seconds.x - self.first_index_position.x)) and (math.fabs(index_position_after_two_seconds.z - self.first_index_position.z) > math.fabs(index_position_after_two_seconds.y - self.first_index_position.y)):
                                  self.enable_contraste = True
                                  self.choose_brillo_contraste_navegacion = False
                                  print "Contraste"


                          if not self.first_time_position and not self.choose_brillo_contraste_navegacion:

                              index_position = index_finger.tip_position

                              if self.enable_navegacion:
                               self.offset = index_position.x
                               Slicer.navegacion(self.axis_selected, self.offset)

                               if(index_position.x >= self.first_index_position.x and math.fabs(index_position.x) > math.fabs(index_position.y)):
                                  gestureDetected = "Navegacion_Derecha"
                                  print "Navegacion derecha -> " + str (index_position.x)
                               elif (index_position.x < self.first_index_position.x and math.fabs(index_position.x) > math.fabs(index_position.y)):
                                  gestureDetected = "Navegacion_Izquierda"
                                  print "Navegacion izquierda->" + str (index_position.x)


                              if self.enable_brillo:
                               self.brightnessFactor = index_position.y
                               slicer.brillo(self.brightnessFactor)

                               if (index_position.y > self.first_index_position.y and math.fabs(index_position.x) < math.fabs(index_position.y)):
                                   gestureDetected = "Brillo_Aumenta"
                                   print "Aumenta Brillo ->" + str (self.brightnessFactor)
                               elif (index_position.y < self.first_index_position.y and math.fabs(index_position.x) < math.fabs(index_position.y)):
                                   gestureDetected = "Brillo_Disminuye"
                                   print "Disminuye Brillo ->" + str (self.brightnessFactor)

                              if self.enable_contraste:
                               self.contrasteFactor = index_position.z
                               slicer.contrasteFactor(self.contrasteFactor)

                               if (index_position.z > 0):
                                  gestureDetected = "Contraste_Disminuye"
                                  print "Disminuye Contraste ->" + str (self.contrasteFactor)
                               elif (index_position.z < 0):
                                  gestureDetected = "Contraste_Aumenta"
                                  print "Aumenta Contraste ->" + str (self.contrasteFactor)


                      ########################### Salimos a elegir otro eje o finalizar ##############################
                      if hand.fingers.finger_type(finger.TYPE_THUMB)[0].is_extended and len(extended_finger_list) == 1:
                        print "Gesto pulgar"
                        if not self.thumb_gesture_started:
                            self.thumb_gesture_started = True
                            self.gesture_time_elapsed = time.time()
                        if self.thumb_gesture_started and (time.time() - self.gesture_time_elapsed >= 2):
                            self.gesture_time_elapsed = time.time()
                            self.enable_zoom = False
                            self.enable_nav_brillo_contr = False
                            self.enable_axis_change = True
                            self.thumb_gesture_started = False
                            self.axis_selected = ""
                            print "Gesto pulgar Activado" 
                            print "Modo seleccion de eje"


# def main():     

#     listener = LeapMotionListener()
#     controller = Leap.Controller()

#     controller.add_listener(listener)

#     print ("Press enter to quit")
#     try:
#         sys.stdin.readline()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         controller.remove_listener(listener)

# if __name__=="__main__":
#     main()


    

