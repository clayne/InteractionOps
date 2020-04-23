import bpy
import os
import json
from ... utils.functions import (register_keymaps, unregister_keymaps, get_addon)


def save_hotkeys():
    path = bpy.utils.script_path_user()
    folder = os.path.join(path, 'presets', 'keyconfig', "IOPS")
    user_hotkeys_file = os.path.join(path, 'presets', 'keyconfig', "IOPS", "iops_hotkeys_user.py")
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(user_hotkeys_file, 'w') as f:
        data = get_iops_keys()
        f.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in data) +
        ']\n')

def get_iops_keys():
    keys = []
    keyconfig = bpy.context.window_manager.keyconfigs['blender user']
    for keymap in keyconfig.keymaps:
        if keymap:
            keymapItems = keymap.keymap_items
            toSave = tuple(
                item for item in keymapItems if item.idname.startswith('iops.'))
            for item in toSave:
                entry = (item.idname, item.type, item.value, item.ctrl, item.alt, item.shift, item.oskey)
                keys.append(entry)
    for k in keys:
        print(k)
    return keys


class IOPS_OT_SaveUserHotkeys(bpy.types.Operator):
    bl_idname = "iops.save_user_hotkeys"
    bl_label = "Save User's Hotkeys"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        save_hotkeys()
        print("Saved user's hotkeys")
        return {"FINISHED"}
