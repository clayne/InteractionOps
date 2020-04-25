import bpy
from bpy.types import Menu

def get_text_and_icon(ui_type, dict):
    for k,v in dict.items():
        if v["ui"] == ui_type:
            return (k, v["icon"])

class IOPS_OT_Split_Area_Pie_1(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.split_area_pie_1"
    bl_label = "IOPS Split Area Pie 1"

    def execute(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        bpy.ops.iops.split_screen_area(area=prefs.split_area_pie_1_ui, pos=prefs.split_area_pie_1_pos, factor=prefs.split_area_pie_1_factor)         
        return {'FINISHED'}

class IOPS_OT_Split_Area_Pie_2(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.split_area_pie_2"
    bl_label = "IOPS Split Area Pie 2"

    def execute(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        bpy.ops.iops.split_screen_area(area=prefs.split_area_pie_2_ui, pos=prefs.split_area_pie_2_pos, factor=prefs.split_area_pie_2_factor)         
        return {'FINISHED'}

class IOPS_OT_Split_Area_Pie_3(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.split_area_pie_3"
    bl_label = "IOPS Split Area Pie 3"

    def execute(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        bpy.ops.iops.split_screen_area(area=prefs.split_area_pie_3_ui, pos=prefs.split_area_pie_3_pos, factor=prefs.split_area_pie_3_factor)         
        return {'FINISHED'}

class IOPS_OT_Split_Area_Pie_4(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.split_area_pie_4"
    bl_label = "IOPS Split Area Pie 4"

    def execute(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        bpy.ops.iops.split_screen_area(area=prefs.split_area_pie_4_ui, pos=prefs.split_area_pie_4_pos, factor=prefs.split_area_pie_4_factor)         
        return {'FINISHED'}

class IOPS_OT_Split_Area_Pie_6(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.split_area_pie_6"
    bl_label = "IOPS Split Area Pie 6"

    def execute(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        bpy.ops.iops.split_screen_area(area=prefs.split_area_pie_6_ui, pos=prefs.split_area_pie_6_pos, factor=prefs.split_area_pie_6_factor)         
        return {'FINISHED'}

class IOPS_OT_Split_Area_Pie_7(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.split_area_pie_7"
    bl_label = "IOPS Split Area Pie 7"

    def execute(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        bpy.ops.iops.split_screen_area(area=prefs.split_area_pie_7_ui, pos=prefs.split_area_pie_7_pos, factor=prefs.split_area_pie_7_factor)         
        return {'FINISHED'}

class IOPS_OT_Split_Area_Pie_8(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.split_area_pie_8"
    bl_label = "IOPS Split Area Pie 8"

    def execute(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        bpy.ops.iops.split_screen_area(area=prefs.split_area_pie_8_ui, pos=prefs.split_area_pie_8_pos, factor=prefs.split_area_pie_8_factor)         
        return {'FINISHED'}

class IOPS_OT_Split_Area_Pie_9(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.split_area_pie_9"
    bl_label = "IOPS Split Area Pie 9"

    def execute(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        bpy.ops.iops.split_screen_area(area=prefs.split_area_pie_9_ui, pos=prefs.split_area_pie_9_pos, factor=prefs.split_area_pie_9_factor)         
        return {'FINISHED'}

class IOPS_MT_Pie_Split(Menu):
    # bl_idname = "iops.pie_menu"
    bl_label = "IOPS Split"

    def draw(self, context):
        prefs = context.preferences.addons['InteractionOps'].preferences
        split_areas_dict = prefs.split_areas_dict

        pie_1_text, pie_1_icon = get_text_and_icon(prefs.split_area_pie_1_ui, split_areas_dict)
        pie_2_text, pie_2_icon = get_text_and_icon(prefs.split_area_pie_2_ui, split_areas_dict)
        pie_3_text, pie_3_icon = get_text_and_icon(prefs.split_area_pie_3_ui, split_areas_dict)
        pie_4_text, pie_4_icon = get_text_and_icon(prefs.split_area_pie_4_ui, split_areas_dict)
        pie_6_text, pie_6_icon = get_text_and_icon(prefs.split_area_pie_6_ui, split_areas_dict)
        pie_7_text, pie_7_icon = get_text_and_icon(prefs.split_area_pie_7_ui, split_areas_dict)
        pie_8_text, pie_8_icon = get_text_and_icon(prefs.split_area_pie_8_ui, split_areas_dict)
        pie_9_text, pie_9_icon = get_text_and_icon(prefs.split_area_pie_9_ui, split_areas_dict)

        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        if pie_4_text != "Empty":
            pie.operator("iops.split_area_pie_4", text=pie_4_text, icon=pie_4_icon) 
        else:
            pie.separator()       
        
        # 6 - RIGHT
        if pie_6_text != "Empty":
            pie.operator("iops.split_area_pie_6", text=pie_6_text, icon=pie_6_icon) 
        else:
            pie.separator()  
        
        # 2 - BOTTOM
        if pie_2_text != "Empty":
            pie.operator("iops.split_area_pie_2", text=pie_2_text, icon=pie_2_icon) 
        else:
            pie.separator()  
        
        # 8 - TOP
        if pie_8_text != "Empty":
            pie.operator("iops.split_area_pie_8", text=pie_8_text, icon=pie_8_icon) 
        else:
            pie.separator()  

        # 7 - TOP - LEFT
        if pie_7_text != "Empty":
            pie.operator("iops.split_area_pie_7", text=pie_7_text, icon=pie_7_icon) 
        else:
            pie.separator()  
        
        # 9 - TOP - RIGHT
        if pie_9_text != "Empty":
            pie.operator("iops.split_area_pie_9", text=pie_9_text, icon=pie_9_icon) 
        else:
            pie.separator()  

        # 1 - BOTTOM - LEFT 
        if pie_1_text != "Empty":
            pie.operator("iops.split_area_pie_1", text=pie_1_text, icon=pie_1_icon) 
        else:
            pie.separator()  
        # 3 - BOTTOM - RIGHT
        if pie_3_text != "Empty":
            pie.operator("iops.split_area_pie_3", text=pie_3_text, icon=pie_3_icon) 
        else:
            pie.separator()


class IOPS_OT_Call_Pie_Split(bpy.types.Operator):
    """IOPS Pie Split"""
    bl_idname = "iops.call_pie_split"
    bl_label = "IOPS Pie Split"

    def execute(self, context):        
        bpy.ops.wm.call_menu_pie(name="IOPS_MT_Pie_Split")         
        return {'FINISHED'}