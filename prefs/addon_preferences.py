import bpy
import rna_keymap_ui
from mathutils import Vector
from bpy.types import (
    Operator,
    Menu,
    Panel,
    PropertyGroup,
    AddonPreferences,
)
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    PointerProperty,
    StringProperty,
    FloatVectorProperty,
)
from ..ui.iops_tm_panel import IOPS_PT_VCol_Panel

# Panels to update
panels = (IOPS_PT_VCol_Panel,)


def update_category(self, context):
    message = "Panel Update Failed"
    try:
        for panel in panels:
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

        for panel in panels:
            panel.bl_category = context.preferences.addons[
                "InteractionOps"
            ].preferences.category
            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format("InteractionOps", message, e))
        pass


class IOPS_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "InteractionOps"

    category: StringProperty(
        name="Tab Name",
        description="Choose a name for the category of the panel",
        default="iOps",
        update=update_category,
    )

    # list itens (identifier, name, description, icon, number,)
    # Area.type, Area.ui_type, Icon, PrefText
    tabs: bpy.props.EnumProperty(
        name="Preferences",
        items=[("PREFS", "Preferences", ""), ("KM", "Keymaps", "")],
        default="PREFS",
    )

    split_areas_dict = {
        "Empty": {"type": "EMPTY", "ui": "EMPTY", "icon": "NONE", "num": 0},
        "3D Viewport": {"type": "VIEW_3D", "ui": "VIEW_3D", "icon": "VIEW3D", "num": 1},
        "Image Editor": {
            "type": "IMAGE_EDITOR",
            "ui": "IMAGE_EDITOR",
            "icon": "IMAGE",
            "num": 2,
        },
        "UV Editor": {"type": "IMAGE_EDITOR", "ui": "UV", "icon": "UV", "num": 3},
        "Shader Editor": {
            "type": "NODE_EDITOR",
            "ui": "ShaderNodeTree",
            "icon": "NODE_MATERIAL",
            "num": 4,
        },
        "Compositor": {
            "type": "NODE_EDITOR",
            "ui": "CompositorNodeTree",
            "icon": "NODE_COMPOSITING",
            "num": 5,
        },
        "Texture Node Editor": {
            "type": "NODE_EDITOR",
            "ui": "TextureNodeTree",
            "icon": "NODE_TEXTURE",
            "num": 6,
        },
        "Video Sequencer": {
            "type": "SEQUENCE_EDITOR",
            "ui": "SEQUENCE_EDITOR",
            "icon": "SEQUENCE",
            "num": 7,
        },
        "Movie Clip Editor": {
            "type": "CLIP_EDITOR",
            "ui": "CLIP_EDITOR",
            "icon": "TRACKER",
            "num": 8,
        },
        "Dope Sheet": {
            "type": "DOPESHEET_EDITOR",
            "ui": "DOPESHEET",
            "icon": "ACTION",
            "num": 9,
        },
        "Timeline": {
            "type": "DOPESHEET_EDITOR",
            "ui": "TIMELINE",
            "icon": "TIME",
            "num": 10,
        },
        "Graph Editor": {
            "type": "GRAPH_EDITOR",
            "ui": "FCURVES",
            "icon": "GRAPH",
            "num": 11,
        },
        "Drivers": {
            "type": "GRAPH_EDITOR",
            "ui": "DRIVERS",
            "icon": "DRIVER",
            "num": 12,
        },
        "Nonlinear Animation": {
            "type": "NLA_EDITOR",
            "ui": "NLA_EDITOR",
            "icon": "NLA",
            "num": 13,
        },
        "Text Editor": {
            "type": "TEXT_EDITOR",
            "ui": "TEXT_EDITOR",
            "icon": "TEXT",
            "num": 14,
        },
        "Python Console": {
            "type": "CONSOLE",
            "ui": "CONSOLE",
            "icon": "CONSOLE",
            "num": 15,
        },
        "Info": {"type": "INFO", "ui": "INFO", "icon": "INFO", "num": 16},
        "Outliner": {
            "type": "OUTLINER",
            "ui": "OUTLINER",
            "icon": "OUTLINER",
            "num": 17,
        },
        "Properties": {
            "type": "PROPERTIES",
            "ui": "PROPERTIES",
            "icon": "PROPERTIES",
            "num": 18,
        },
        "File Browser": {
            "type": "FILE_BROWSER",
            "ui": "FILE_BROWSER",
            "icon": "FILEBROWSER",
            "num": 19,
        },
        "Preferences": {
            "type": "PREFERENCES",
            "ui": "PREFERENCES",
            "icon": "PREFERENCES",
            "num": 20,
        },
        "Geometry Nodes": {
            "type": "NODE_EDITOR",
            "ui": "GeometryNodeTree",
            "icon": "NODETREE",
            "num": 21,
        },
        "Spreadsheet": {
            "type": "SPREADSHEET",
            "ui": "SPREADSHEET",
            "icon": "SPREADSHEET",
            "num": 22,
        },
    }
    file_browser_name = "FILE_BROWSER"
    if bpy.app.version[1] >= 92:
        file_browser_name = "FILES"
        split_areas_dict["File Browser"]["ui"] = "FILES"
        split_areas_dict["Asset Browser"] = {
            "type": "FILE_BROWSER",
            "ui": "ASSETS",
            "icon": "ASSET_MANAGER",
            "num": 23,
        }
    if bpy.app.version[0] >= 3:
        file_browser_name = "FILES"
        split_areas_dict["File Browser"]["ui"] = "FILES"
        split_areas_dict["Asset Browser"] = {
            "type": "FILE_BROWSER",
            "ui": "ASSETS",
            "icon": "ASSET_MANAGER",
            "num": 23,
        }

    split_areas_list = [
        (v["ui"], k, "", v["icon"], v["num"]) for k, v in split_areas_dict.items()
    ]

    split_areas_position_list = [
        ("LEFT", "LEFT", "", "", 0),
        ("RIGHT", "RIGHT", "", "", 1),
        ("TOP", "TOP", "", "", 2),
        ("BOTTOM", "BOTTOM", "", "", 3),
    ]

    text_color: FloatVectorProperty(
        name="Color",
        subtype="COLOR_GAMMA",
        size=4,
        min=0,
        max=1,
        default=((*bpy.context.preferences.themes[0].text_editor.syntax_numbers, 0.75)),
    )

    text_color_key: FloatVectorProperty(
        name="Color key",
        subtype="COLOR_GAMMA",
        size=4,
        min=0,
        max=1,
        default=((*bpy.context.preferences.themes[0].text_editor.syntax_builtin, 0.75)),
    )

    text_size: IntProperty(
        name="Size",
        description="Modal operators text size",
        default=20,
        soft_min=1,
        soft_max=100,
    )

    text_pos_x: IntProperty(
        name="Position X",
        description="Modal operators Text pos X",
        default=60,
        soft_min=1,
        soft_max=10000,
    )

    text_pos_y: IntProperty(
        name="Position Y",
        description="Modal operators Text pos Y",
        default=60,
        soft_min=1,
        soft_max=10000,
    )

    text_shadow_color: FloatVectorProperty(
        name="Shadow",
        subtype="COLOR_GAMMA",
        size=4,
        min=0,
        max=1,
        default=(0.0, 0.0, 0.0, 1.0),
    )

    text_shadow_toggle: BoolProperty(name="ON/OFF", description="ON/Off", default=False)

    IOPS_DEBUG: BoolProperty(name="Query debug", description="ON/Off", default=False)

    text_shadow_blur: EnumProperty(
        name="Blur",
        description="Could be 0,3,5",
        items=[
            ("0", "None", "", "", 0),
            ("3", "Mid", "", "", 3),
            ("5", "High", "", "", 5),
        ],
        default="0",
    )

    text_shadow_pos_x: IntProperty(
        name="Shadow pos X",
        description="Modal operators Text pos X",
        default=2,
        soft_min=-50,
        soft_max=50,
    )
    text_shadow_pos_y: IntProperty(
        name="Shadow pos Y",
        description="Modal operators Text pos Y",
        default=-2,
        soft_min=-50,
        soft_max=50,
    )

    vo_cage_color: FloatVectorProperty(
        name="Cage color",
        subtype="COLOR_GAMMA",
        size=4,
        min=0,
        max=1,
        default=Vector((*bpy.context.preferences.themes[0].view_3d.object_active, 0.25))
        - Vector((0.3, 0.3, 0.3, 0)),
    )

    vo_cage_points_color: FloatVectorProperty(
        name="Cage points color",
        subtype="COLOR_GAMMA",
        size=4,
        min=0,
        max=1,
        default=(*bpy.context.preferences.themes[0].view_3d.wire_edit, 0.7),
    )

    vo_cage_ap_color: FloatVectorProperty(
        name="Active point color",
        subtype="COLOR_GAMMA",
        size=4,
        min=0,
        max=1,
        default=Vector((*bpy.context.preferences.themes[0].view_3d.object_active, 0.5))
        - Vector((0.2, 0.2, 0.2, 0)),
    )

    vo_cage_p_size: IntProperty(
        name="Cage point size",
        description="Visual origin cage point size",
        default=2,
        soft_min=2,
        soft_max=20,
    )

    vo_cage_ap_size: IntProperty(
        name="Active point size",
        description="Visual origin active point size",
        default=4,
        soft_min=2,
        soft_max=20,
    )

    align_edge_color: FloatVectorProperty(
        name="Edge color",
        subtype="COLOR_GAMMA",
        size=4,
        min=0,
        max=1,
        default=((*bpy.context.preferences.themes[0].view_3d.object_active, 0.5)),
    )
    # 1 - BOTTOM - LEFT
    split_area_pie_1_ui: EnumProperty(
        name="",
        description="Area Types",
        items=split_areas_list,
        default="ShaderNodeTree",
    )
    split_area_pie_1_pos: EnumProperty(
        name="",
        description="Area screen position",
        items=split_areas_position_list,
        default="BOTTOM",
    )
    split_area_pie_1_factor: FloatProperty(
        name="",
        description="Split factor",
        default=0.2,
        min=0.05,
        max=1.0,
        step=0.01,
        precision=2,
    )
    # 2 - BOTTOM
    split_area_pie_2_ui: EnumProperty(
        name="", description="Area Types", items=split_areas_list, default="TIMELINE"
    )
    split_area_pie_2_pos: EnumProperty(
        name="",
        description="Area screen position",
        items=split_areas_position_list,
        default="BOTTOM",
    )
    split_area_pie_2_factor: FloatProperty(
        name="",
        description="Split factor",
        default=0.5,
        min=0.05,
        max=1.0,
        step=0.01,
        precision=2,
    )
    # 3 - BOTTOM - RIGHT
    split_area_pie_3_ui: EnumProperty(
        name="", description="Area Types", items=split_areas_list, default="PROPERTIES"
    )
    split_area_pie_3_pos: EnumProperty(
        name="",
        description="Area screen position",
        items=split_areas_position_list,
        default="RIGHT",
    )
    split_area_pie_3_factor: FloatProperty(
        name="",
        description="Split factor",
        default=0.5,
        min=0.05,
        max=1.0,
        step=0.01,
        precision=2,
    )
    # 4 - LEFT
    split_area_pie_4_ui: EnumProperty(
        name="", description="Area Types", items=split_areas_list, default="OUTLINER"
    )
    split_area_pie_4_pos: EnumProperty(
        name="",
        description="Area screen position",
        items=split_areas_position_list,
        default="LEFT",
    )
    split_area_pie_4_factor: FloatProperty(
        name="",
        description="Split factor",
        default=0.5,
        min=0.05,
        max=1.0,
        step=0.01,
        precision=2,
    )
    # 6 - RIGHT
    split_area_pie_6_ui: EnumProperty(
        name="", description="Area Types", items=split_areas_list, default="UV"
    )
    split_area_pie_6_pos: EnumProperty(
        name="",
        description="Area screen position",
        items=split_areas_position_list,
        default="RIGHT",
    )
    split_area_pie_6_factor: FloatProperty(
        name="",
        description="Split factor",
        default=0.5,
        min=0.05,
        max=1.0,
        step=0.01,
        precision=2,
    )
    # 7 - TOP - LEFT
    split_area_pie_7_ui: EnumProperty(
        name="",
        description="Area Types",
        items=split_areas_list,
        default=file_browser_name,
    )
    split_area_pie_7_pos: EnumProperty(
        name="",
        description="Area screen position",
        items=split_areas_position_list,
        default="RIGHT",
    )
    split_area_pie_7_factor: FloatProperty(
        name="",
        description="Split factor",
        default=0.5,
        min=0.05,
        max=1.0,
        step=0.01,
        precision=2,
    )
    # 8 - TOP
    split_area_pie_8_ui: EnumProperty(
        name="", description="Area Types", items=split_areas_list, default="CONSOLE"
    )
    split_area_pie_8_pos: EnumProperty(
        name="",
        description="Area screen position",
        items=split_areas_position_list,
        default="TOP",
    )
    split_area_pie_8_factor: FloatProperty(
        name="",
        description="Split factor",
        default=0.5,
        min=0.05,
        max=1.0,
        step=0.01,
        precision=2,
    )
    # 9 - TOP - RIGHT
    split_area_pie_9_ui: EnumProperty(
        name="", description="Area Types", items=split_areas_list, default="TEXT_EDITOR"
    )
    split_area_pie_9_pos: EnumProperty(
        name="",
        description="Area screen position",
        items=split_areas_position_list,
        default="RIGHT",
    )
    split_area_pie_9_factor: FloatProperty(
        name="",
        description="Split factor",
        default=0.5,
        min=0.05,
        max=1.0,
        step=0.01,
        precision=2,
    )

    executor_column_count: IntProperty(
        name="Scripts per column",
        description="Scripts per column ",
        default=20,
        min=5,
        max=1000,
    )
    executor_scripts_folder: StringProperty(
        name="Scripts Folder",
        subtype="DIR_PATH",
        default=bpy.utils.script_path_user(),
    )

    texture_to_material_prefixes: StringProperty(
        name="Prefixes",
        description="Type prefixes what you want to clean",
        default="env_",
    )
    texture_to_material_suffixes: StringProperty(
        name="Suffixes",
        description="Type suffixes what you want to clean",
        default="_df,_dfa,_mk,_emk,_nm",
    )

    switch_list_axis: StringProperty(
        name="Axis Switch List",
        description="Axis Switch List, types should be with capital letters and separated by comma",
        default="GLOBAL, LOCAL, NORMAL, GIMBAL, VIEW, CURSOR",
    )

    switch_list_ppoint: StringProperty(
        name="PivotPoint Switch List",
        description="PivotPoint Switch List, types should be with capital letters and separated by comma",
        default="BOUNDING_BOX_CENTER, CURSOR, INDIVIDUAL_ORIGINS, MEDIAN_POINT, ACTIVE_ELEMENT",
    )

    switch_list_snap: StringProperty(
        name="Snap With.. Switch List",
        description="Snap With.. Switch List, types should be with capital letters and separated by comma ",
        default="CLOSEST, CENTER, MEDIAN, ACTIVE",
    )

    def draw(self, context):
        layout = self.layout
        tabs_row = layout.row()
        tabs_row.prop(self, "tabs", expand=True)
        column_main = layout.column()
        if self.tabs == "KM":

            # Hotkeys
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Hotkeys:")
            row = col.row(align=True)
            row.operator("iops.save_user_hotkeys", text="Save User's Hotkeys")
            row.separator()
            row.separator()
            row.separator()
            row.operator("iops.load_user_hotkeys", text="Load User's Hotkeys")
            row.separator()
            row.separator()
            row.separator()
            row.operator(
                "iops.load_default_hotkeys", text="Load Default Hotkeys", icon="ERROR"
            )
            col.separator()
            col.separator()
            col.separator()

            # Keymaps
            col = column_main.column(align=False)
            km_row = col.row(align=True)
            km_col = km_row.column(align=True)
            
            '''
            kc - keyconfigs
            km - keymap
            kmi - keymap item
            
            '''
            kc = context.window_manager.keyconfigs
            kc_user = context.window_manager.keyconfigs.user
            # IOPS keymaps
            keymaps = [kc_user.keymaps["Window"], kc_user.keymaps["Mesh"], kc_user.keymaps["Object Mode"], kc_user.keymaps["Screen Editing"]]
            for km in keymaps:
                for kmi in km.keymap_items:
                    if kmi.idname.startswith("iops."):
                        try:
                            rna_keymap_ui.draw_kmi(["ADDON", "USER", "DEFAULT"], kc, km, kmi, km_col, 0)
                        except AttributeError:
                            km_col.label(text="No modal key maps attached to this operator ¯\_(ツ)_/¯", icon="INFO")
                    elif kmi.idname.startswith("iops.split_area"):
                        try:
                            rna_keymap_ui.draw_kmi(["ADDON", "USER", "DEFAULT"], kc, km, kmi, km_col, 0)
                        except AttributeError:
                            km_col.label(text="No modal key maps attached to this operator ¯\_(ツ)_/¯", icon="INFO")


        if self.tabs == "PREFS":
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Category:")
            col.prop(self, "category")
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="3D View Overlay Text Settings:")
            row = box.row(align=True)
            split = row.split(factor=0.5, align=False)
            col_text = split.column(align=True)
            col_shadow = split.column(align=True)
            row = col_text.row(align=True)
            row.prop(self, "text_color")
            row.prop(self, "text_color_key")
            row = col_text.row(align=True)
            row.prop(self, "text_size")
            row = col_text.row(align=True)
            row.prop(self, "text_pos_x")
            row.prop(self, "text_pos_y")

            # Shadow
            row = col_shadow.row(align=False)
            row.prop(self, "text_shadow_color")
            row.prop(self, "text_shadow_blur")
            row = col_shadow.row(align=True)
            row.prop(self, "text_shadow_toggle", toggle=True)
            row = col_shadow.row(align=True)
            row.prop(self, "text_shadow_pos_x")
            row.prop(self, "text_shadow_pos_y")
            col.separator()
            # Align to edge
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Align to edge:")
            row = box.row(align=True)
            row.alignment = "LEFT"
            row.prop(self, "align_edge_color")
            col.separator()
            # Visual origin
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Visual origin:")
            row = box.row(align=True)
            split = row.split(factor=0.5, align=False)
            col_ap = split.column(align=True)
            col_p = split.column(align=True)
            col.separator()
            # Active point column
            col = col_p.column(align=True)
            col.label(text="Cage points:")
            col.prop(self, "vo_cage_p_size", text="Size")
            col.prop(self, "vo_cage_points_color", text="")

            # Cage points column
            col = col_ap.column(align=True)
            col.label(text="Active point:")
            col.prop(self, "vo_cage_ap_size", text="Size")
            col.prop(self, "vo_cage_ap_color", text="")

            # Cage color

            col = box.column(align=True)
            col.prop(self, "vo_cage_color")
            col.separator()
            # Split Pie preferences
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="IOPS Split Pie Setup:")
            row = col.row(align=True)

            # TOP LEFT
            box_1 = row.box()
            col = box_1.column(align=True)
            col.prop(self, "split_area_pie_7_ui")
            col.prop(self, "split_area_pie_7_pos")
            col.prop(self, "split_area_pie_7_factor")
            row.separator()
            # TOP
            box_2 = row.box()
            col = box_2.column(align=True)
            col.prop(self, "split_area_pie_8_ui")
            col.prop(self, "split_area_pie_8_pos")
            col.prop(self, "split_area_pie_8_factor")
            row.separator()
            # TOP RIGHT
            box_3 = row.box()
            col = box_3.column(align=True)
            col.prop(self, "split_area_pie_9_ui")
            col.prop(self, "split_area_pie_9_pos")
            col.prop(self, "split_area_pie_9_factor")

            col = box.column(align=True)
            row = col.row(align=True)
            # LEFT
            box_1 = row.box()
            col = box_1.column(align=True)
            col.prop(self, "split_area_pie_4_ui")
            col.prop(self, "split_area_pie_4_pos")
            col.prop(self, "split_area_pie_4_factor")
            row.separator()
            # CENTER
            box_2 = row.box()
            col = box_2.column(align=True)
            col.label(text=" ")
            col.label(text=" ")
            col.label(text=" ")
            row.separator()
            # RIGHT
            box_3 = row.box()
            col = box_3.column(align=True)
            col.prop(self, "split_area_pie_6_ui")
            col.prop(self, "split_area_pie_6_pos")
            col.prop(self, "split_area_pie_6_factor")

            col = box.column(align=True)
            row = col.row(align=True)

            # BOTTOM LEFT
            box_1 = row.box()
            col = box_1.column(align=True)
            col.prop(self, "split_area_pie_1_ui")
            col.prop(self, "split_area_pie_1_pos")
            col.prop(self, "split_area_pie_1_factor")
            row.separator()
            # BOTTOM
            box_2 = row.box()
            col = box_2.column(align=True)
            col.prop(self, "split_area_pie_2_ui")
            col.prop(self, "split_area_pie_2_pos")
            col.prop(self, "split_area_pie_2_factor")
            row.separator()
            # BOTTOM RIGHT
            box_3 = row.box()
            col = box_3.column(align=True)
            col.prop(self, "split_area_pie_3_ui")
            col.prop(self, "split_area_pie_3_pos")
            col.prop(self, "split_area_pie_3_factor")

            # Executor
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Script Executor:")
            col = box.column(align=True)
            col.prop(self, "executor_scripts_folder")
            col.prop(self, "executor_column_count")
            col.separator()
            # Textures to materials
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Textures to Materials:")
            col = box.column(align=True)
            col.prop(self, "texture_to_material_prefixes")
            col.prop(self, "texture_to_material_suffixes")
            col.separator()
            # Switch lists
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Switch lists:")
            col = box.column(align=True)
            col.prop(self, "switch_list_axis")
            col.prop(self, "switch_list_ppoint")
            col.prop(self, "switch_list_snap")
            col.separator()

            # Preferences
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Addon preferences")
            row = col.row(align=True)
            row.operator("iops.save_addon_preferences", text="Save preferences")
            row.operator("iops.load_addon_preferences", text="Load preferences")
            col.separator()
            # Debug
            col = column_main.column(align=False)
            box = col.box()
            col = box.column(align=True)
            col.label(text="Debug:")
            row = box.row(align=True)
            row.alignment = "LEFT"
            row.prop(self, "IOPS_DEBUG")
