from maya import cmds
import os

def create_camera_with_ctrls(ctrl_name, geo_name, index):
    # Create controls for rig
    ctrl = cmds.circle(name=ctrl_name, radius=3, normal=[0, 1, 0])
    cmds.color(ctrl, rgb=(.78, 0, 0.07))
    ctrl2 = cmds.circle(name=ctrl_name, radius=2.5, normal=[0, 1, 0])
    cmds.color(ctrl2, rgb=(.8, 0, 1))
    ctrl_node = ctrl[0]
    ctrl_node2 = ctrl2[0]

    # Create camera with a unique name
    camera_name = geo_name + "_%02d" % index
    cam = cmds.camera(name=camera_name, position=[0, 0, 0])

    # Get created node
    cam_node = cam[0]
    set_display_template(cam_node)

    # Create a locator at the camera's current position
    locator_name = geo_name + "_Locator_%02d" % index
    locator = cmds.spaceLocator(name=locator_name)[0]
    cmds.scale(.1, .1, .1, locator)
    camera_position = cmds.xform(cam_node, query=True, worldSpace=True, translation=True)
    cmds.xform(locator, worldSpace=True, translation=camera_position)

    # parent the global control
    cmds.parent(ctrl_node2, ctrl_node)

    # Parent the locator under the control
    cmds.parent(locator, ctrl_node2)

    # Parent the camera under the locator
    cmds.parent(cam_node, locator)

    # Deselect everything to avoid conflicts with previous selections
    cmds.select(clear=True)

    # Usage for dolly and travel and rotation Arrow and up and down arrow
    script_directory = os.path.dirname(os.path.abspath(__file__))
    ai_file_path = os.path.join(script_directory, "arrow.ai")
    curve_name = 'TravelCurve' + str(index)

    ai_file_path2 = os.path.join(script_directory, "rotation arrow.ai")
    curve_name2 = 'RotationArrow' + str(index)

    ai_file_path3 = os.path.join(script_directory, "arrow.ai")
    curve_name3 = 'UpDownArrow' + str(index)

    #import hud curve
    ai_file_path4 = os.path.join(script_directory, "hud.ai")
    curve_name4 = 'HUD' + str(index)

    # import all controls
    import_ai_file(ai_file_path, curve_name)
    import_ai_file(ai_file_path3, curve_name3)
    import_ai_file(ai_file_path2, curve_name2)
    import_ai_file(ai_file_path4, curve_name4)

    # Center the pivot of the curve
    cmds.xform(curve_name, centerPivots=True)
    cmds.xform(curve_name2, centerPivots=True)
    cmds.xform(curve_name3, centerPivots=True)
    cmds.xform(curve_name4, centerPivots=True)

    # Create a locator
    source_object = cmds.spaceLocator()[0]
    source_object2 = cmds.spaceLocator()[0]
    source_object3 = cmds.spaceLocator()[0]
    source_object4 = cmds.spaceLocator()[0]

    # move second locator
    cmds.xform(source_object2, t=[0, 0, 2])

    #move locator for HUD
    cmds.xform(source_object4, t=[0, 1.7, 0])

    # Get the translation values of the source object in world space
    tx, ty, tz = cmds.xform(source_object, query=True, translation=True, worldSpace=True)
    tx2, ty2, tz2 = cmds.xform(source_object2, query=True, translation=True, worldSpace=True)
    tx3, ty3, tz3 = cmds.xform(source_object3, query=True, translation=True, worldSpace=True)

    # Get the pivot position of the source object in world space
    source_pivot_position = cmds.xform(source_object, query=True, worldSpace=True, pivots=True)
    source_pivot_position2 = cmds.xform(source_object2, query=True, worldSpace=True, pivots=True)
    source_pivot_position3 = cmds.xform(source_object3, query=True, worldSpace=True, pivots=True)
    source_pivot_position4 = cmds.xform(source_object4, query=True, worldSpace=True, pivots=True)

    # Get the pivot position of the curve in world space
    curve_pivot_position = cmds.xform(curve_name, query=True, worldSpace=True, pivots=True)
    curve_pivot_position2 = cmds.xform(curve_name2, query=True, worldSpace=True, pivots=True)
    curve_pivot_position3 = cmds.xform(curve_name3, query=True, worldSpace=True, pivots=True)
    curve_pivot_position4 = cmds.xform(curve_name4, query=True, worldSpace=True, pivots=True)


    # Ensure pivot positions are lists even if they have a single value
    source_pivot_position = source_pivot_position if isinstance(source_pivot_position, list) else [
        source_pivot_position]
    curve_pivot_position = curve_pivot_position if isinstance(curve_pivot_position, list) else [curve_pivot_position]
    source_pivot_position2 = source_pivot_position2 if isinstance(source_pivot_position2, list) else [
        source_pivot_position2]
    curve_pivot_position2 = curve_pivot_position2 if isinstance(curve_pivot_position2, list) else [
        curve_pivot_position2]
    source_pivot_position3 = source_pivot_position3 if isinstance(source_pivot_position3, list) else [
        source_pivot_position3]
    curve_pivot_position3 = curve_pivot_position3 if isinstance(curve_pivot_position3, list) else [
        curve_pivot_position3]
    source_pivot_position4 = source_pivot_position4 if isinstance(source_pivot_position4, list) else [
        source_pivot_position4]
    curve_pivot_position4 = curve_pivot_position4 if isinstance(curve_pivot_position4, list) else [
        curve_pivot_position4]

    # Calculate the offset between the locator's pivot and the curve's pivot
    offset = [tx - source_pivot_position[0] - curve_pivot_position[0],
              ty - source_pivot_position[1] - curve_pivot_position[1],
              tz - source_pivot_position[2] - curve_pivot_position[2]]

    offset2 = [tx2 - source_pivot_position2[0] - curve_pivot_position2[0],
               ty2 - source_pivot_position2[1] - curve_pivot_position2[1],
               source_pivot_position2[2] - curve_pivot_position2[2]]

    offset3 = [tx3 - source_pivot_position3[0] - curve_pivot_position3[0],
               ty3 - source_pivot_position3[1] - curve_pivot_position3[1],
               tz3 - source_pivot_position3[2] - curve_pivot_position3[2]]

    offset4 = [source_pivot_position4[0] - curve_pivot_position4[0],
               source_pivot_position4[1] - curve_pivot_position4[1],
               source_pivot_position4[2] - curve_pivot_position4[2]]

    # Move the curve to match the translation of the locator
    cmds.xform(curve_name, translation=offset, worldSpace=True)
    cmds.xform(curve_name2, translation=offset2, worldSpace=True)
    cmds.xform(curve_name3, translation=offset3, worldSpace=True)
    cmds.xform(curve_name4, translation=offset4, worldSpace=True)

    # Rotate curve 90 degrees
    cmds.xform(curve_name, r=True, ro=(90, 0, 0))
    cmds.xform(curve_name2, r=True, ro=(-90, 0, 0))
    cmds.xform(curve_name3, r=True, ro=(0, 0, 90))

    # scale up and down curve
    cmds.scale(.5, .8, .5, curve_name3)

    #scale HUD
    cmds.scale(.2,.2,.2, curve_name4)

    # color the arrows
    cmds.color(curve_name, rgb=(.25, .63, .21))
    cmds.color(curve_name2, rgb=(.25, .63, .9))
    cmds.color(curve_name3, rgb=(.75, .63, .9))
    cmds.color(curve_name4, rgb=(.96, .89, .27))

    # Duplicate the curve
    duplicated_curve_name = cmds.duplicate(curve_name)[0]
    duplicated_curve_name2 = cmds.duplicate(curve_name2)[0]
    cmds.color(duplicated_curve_name, rgb=(.5, .63, .21))
    cmds.color(duplicated_curve_name2, rgb=(.25, .63, .9))

    # Give a new name to the duplicated curve
    new_curve_name = 'DollyCurve' + str(index)
    new_curve_name2 = 'RotationArrow1' + str(index)
    cmds.rename(duplicated_curve_name, new_curve_name)
    cmds.rename(duplicated_curve_name2, new_curve_name2)

    # Rotate dolly 90 degrees
    cmds.xform(new_curve_name, r=True, ro=(0, 90, 0))

    # rotate rotation arrow 90 degrees
    cmds.xform(new_curve_name2, r=True, ro=(0, 0, 90))

    # Clean translation and rotation values (set to zero)
    cmds.makeIdentity(new_curve_name, apply=True, translate=True, rotate=True, scale=False)
    cmds.makeIdentity(curve_name, apply=True, translate=True, rotate=True, scale=False)
    cmds.makeIdentity(new_curve_name2, apply=True, translate=True, rotate=True, scale=False)
    cmds.makeIdentity(curve_name2, apply=True, translate=True, rotate=True, scale=False)
    cmds.makeIdentity(curve_name3, apply=True, translate=True, rotate=True, scale=True)
    cmds.makeIdentity(curve_name4, apply=True, translate=True, rotate=True, scale=True)

    #lock dolly values except for Z
    delete_attributes_except_z_translation(new_curve_name)

    # lock Travel values except for X
    delete_attributes_except_x_translation(curve_name)

    # lock UP AND DOWN  values except for Y
    delete_attributes_except_y_translation(curve_name3)

    # delete locator
    cmds.delete(source_object)
    cmds.delete(source_object2)
    cmds.delete(source_object3)
    cmds.delete(source_object4)

    # combine the Rotation Arrow into a single curve
    combined_curve = cmds.attachCurve(curve_name2, new_curve_name2, method=1, kmk=False)[0]

    # lock everything except rotate
    delete_attributes_except_rotation(combined_curve)

    # Delete the original curve2 (optional)
    cmds.delete(new_curve_name2)

    #parent curves
    cmds.parent(curve_name, ctrl_node2)
    cmds.parent(new_curve_name, curve_name)
    cmds.parent(curve_name3, new_curve_name)
    cmds.parent(combined_curve, new_curve_name)

    #group combined_curve
    name_rotate = 'Rotation_ctrl' + str(index)
    cmds.group(combined_curve, n=name_rotate)
    #parent a up and down arrow
    cmds.parent(name_rotate, curve_name3)

    #move pivot of curve to center of scene by copying the locators pivot info
    copy_pivot(locator, combined_curve)

    #constrain rotation curve to camera
    cmds.orientConstraint(combined_curve, cam_node)

    # constrain up and  down control to camera
    cmds.pointConstraint(curve_name3, cam_node)

    #lock all attributes in the camera
    lock_camera_attributes(cam_node)

    # eliminate attributes from HUD
    delete_attributes_except_z_translation(curve_name4)
    delete_attributes_except_rotation(curve_name4)
    #add attributes to HUD
    cmds.addAttr(curve_name4, ln="Lens", at="float", defaultValue=35.0, keyable=True)
    cmds.addAttr(curve_name4, ln="Near_Clip", at="float", defaultValue=-1.0, keyable=True)
    cmds.addAttr(curve_name4, ln="Far_Clip", at="float", defaultValue=1000000, keyable=True)
    cmds.addAttr(curve_name4, ln="DOF", at="bool", defaultValue=0, keyable=True)
    cmds.addAttr(curve_name4, ln="F_Stop", at="float", min=1.0, max=64.0, defaultValue=1.0, keyable=True)
    cmds.addAttr(curve_name4, ln="Focus_Region_Scale", at="float", min=1.0, defaultValue=1.0, keyable=True)

    #connect attributes from HUD to camera
    cmds.connectAttr('{}.F_Stop'.format(curve_name4), '{}.fStop'.format(cam[1]), force=True)
    cmds.connectAttr('{}.Lens'.format(curve_name4), '{}.focalLength'.format(cam[1]), force=True)
    cmds.connectAttr('{}.Far_Clip'.format(curve_name4), '{}.farClipPlane'.format(cam[1]), force=True)
    cmds.connectAttr('{}.Near_Clip'.format(curve_name4), '{}.nearClipPlane'.format(cam[1]), force=True)
    cmds.connectAttr('{}.DOF'.format(curve_name4), '{}.depthOfField'.format(cam[1]), force=True)
    cmds.connectAttr('{}.Focus_Region_Scale'.format(curve_name4),'{}.focusRegionScale'.format(cam[1]), force=True)


    #group the control
    hud_group = cmds.group(curve_name4, n='HUD_{}'.format(index))
    #parent group under rotation arrow
    cmds.parent(hud_group, combined_curve)

    #make the final group
    cmds.group(ctrl[0], n='CameraRig' + str(index))

    #make sure the camera name is right
    cmds.rename(cam[0], camera_name)

    #Camera film gate
    cmds.setAttr("{}.displayResolution".format(cam[1]), 1)

    # Set overscan attribute to 1.3
    cmds.setAttr("{}.overscan".format(cam[1]), 1.3)

    return camera_name, locator_name


def lock_camera_attributes(camera_node):

    attrs_to_lock = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY',
                     'scaleZ']
    for attr in attrs_to_lock:
        cmds.setAttr(camera_node + '.' + attr, lock=True)


def import_ai_file(ai_file, curve_name):

    # Import the AI file as a NURBS curve
    imported_curve = cmds.file(ai_file, i=True, type="Adobe(R) Illustrator(R)", rnn=True, returnNewNodes=True)[0]

    # Rename the imported curve
    cmds.rename(imported_curve, curve_name)

def set_display_template(obj_name):

    # Check if the object exists
    if cmds.objExists(obj_name):
        # Set the 'template' attribute to 1 (True) on the transform node
        cmds.setAttr(obj_name + ".template", 1)

def delete_attributes_except_z_translation(controller_name):

    # Unlock and keyable the 'translate' compound attribute
    cmds.setAttr(controller_name + '.translate', lock=False, keyable=True)

    # Lock and hide 'translateX' and 'translateY' components
    cmds.setAttr(controller_name + '.translateX', lock=True, keyable=False)
    cmds.setAttr(controller_name + '.translateY', lock=True, keyable=False)

    # Lock and hide other attributes except for 'translateZ'
    all_attributes = cmds.listAttr(controller_name, keyable=True, scalar=True, multi=False)
    for attr in all_attributes:
        if attr != 'translateZ':
            cmds.setAttr(controller_name + '.' + attr, lock=True, keyable=False)

def delete_attributes_except_x_translation(controller_name):

    # Unlock and keyable the 'translate' compound attribute
    cmds.setAttr(controller_name + '.translate', lock=False, keyable=True)

    # Lock and hide 'translateX' and 'translateY' components
    cmds.setAttr(controller_name + '.translateZ', lock=True, keyable=False)
    cmds.setAttr(controller_name + '.translateY', lock=True, keyable=False)

    # Lock and hide other attributes except for 'translateZ'
    all_attributes = cmds.listAttr(controller_name, keyable=True, scalar=True, multi=False)
    for attr in all_attributes:
        if attr != 'translateX':
            cmds.setAttr(controller_name + '.' + attr, lock=True, keyable=False)

def delete_attributes_except_y_translation(controller_name):

    # Unlock and keyable the 'translate' compound attribute
    cmds.setAttr(controller_name + '.translate', lock=False, keyable=True)

    # Lock and hide 'translateX' and 'translateY' components
    cmds.setAttr(controller_name + '.translateZ', lock=True, keyable=False)
    cmds.setAttr(controller_name + '.translateX', lock=True, keyable=False)

    # Lock and hide other attributes except for 'translateZ'
    all_attributes = cmds.listAttr(controller_name, keyable=True, scalar=True, multi=False)
    for attr in all_attributes:
        if attr != 'translateY':
            cmds.setAttr(controller_name + '.' + attr, lock=True, keyable=False)

def delete_attributes_except_rotation(controller_name):

    # Unlock and keyable the 'translate' compound attribute
    cmds.setAttr(controller_name + '.rotate', lock=False, keyable=True)

    # Lock and hide other attributes except for 'translateZ'
    all_attributes = cmds.listAttr(controller_name, keyable=True, scalar=True, multi=False)
    for attr in all_attributes:
        if attr not in ['rotateX', 'rotateY', 'rotateZ']:
            cmds.setAttr(controller_name + '.' + attr, lock=True, keyable=False)


def copy_pivot(source_locator, target_object):
    # Get the pivot position of the source locator
    source_pivot = cmds.xform(source_locator, query=True, worldSpace=True, translation=True)

    # Set the pivot position of the target object
    cmds.xform(target_object, worldSpace=True, pivots=source_pivot)


