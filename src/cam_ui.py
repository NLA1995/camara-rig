from maya import cmds
import main_camera

WINDOW_NAME = 'camera_ui'
TEXT_FIELD_NAME = 'camera_name'
TEXT_FIELD_NAME2 = 'ctrl_name'
TEXT_FIELD_NAME3 = 'index_num'

def show_ui():
    """Show camera  ui."""
    if cmds.window(WINDOW_NAME, query=True, exists=True):
        cmds.deleteUI(WINDOW_NAME)

    cmds.window(WINDOW_NAME, title='Camera')

    cmds.showWindow(WINDOW_NAME)

    cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
    cmds.rowLayout(numberOfColumns=2, adjustableColumn=2)
    cmds.text(label='Camera Name:')
    cmds.textField(TEXT_FIELD_NAME)
    cmds.setParent('..')
    cmds.rowLayout(numberOfColumns=2, adjustableColumn=2)
    cmds.text(label='Control Name:')
    cmds.textField(TEXT_FIELD_NAME2)
    cmds.setParent('..')
    cmds.rowLayout(numberOfColumns=2, adjustableColumn=2)
    cmds.text(label='Index Number:')
    cmds.textField(TEXT_FIELD_NAME3)
    cmds.setParent('..')
    cmds.button(label='Camera', height=30, command=on_camera_button_pressed)


def on_camera_button_pressed(*args):
    """Callback function for the camera button."""
    camera_name = cmds.textField(TEXT_FIELD_NAME, query=True, text=True)
    control_name = cmds.textField(TEXT_FIELD_NAME2, query=True, text=True)
    index_num = int(cmds.textField(TEXT_FIELD_NAME3, query=True, text=True))

    main_camera.create_camera_with_ctrls(control_name, camera_name, index_num)

