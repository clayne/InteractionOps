import bpy
#from bpy.types import VIEW3D_PT_transform_orientations, VIEW3D_PT_pivot_point, VIEW3D_PT_snapping



# class IOPS_PT_iops_tm_panel(bpy.types.Panel):
#     """Creates a Panel from Tranformation,PivotPoint,Snapping panels"""
#     bl_label = "IOPS TPS"
#     bl_idname = "IOPS_PT_iops_tm_panel" 
#     bl_space_type = 'VIEW_3D'
#     bl_region_type = 'UI'
#     bl_category = 'Item'    

    

#     def draw(self, context):
#         tool_settings = context.tool_settings
#         layout = self.layout         
#         row = layout.row(align=True)
#         row.prop(tool_settings, "use_snap", text="")
#         row.prop(tool_settings, "use_mesh_automerge", text="")
#         row = layout.row(align=True)        
#         VIEW3D_PT_transform_orientations.draw(self, context)
#         VIEW3D_PT_pivot_point.draw(self, context)
#         VIEW3D_PT_snapping.draw(self,context)
        # row.popover('VIEW3D_PT_transform_orientations', text="Transform", text_ctxt="", translate=True, icon='ORIENTATION_GLOBAL', icon_value=0)
        # row.popover('VIEW3D_PT_pivot_point', text="PivotPoint", text_ctxt="", translate=True, icon='PIVOT_INDIVIDUAL', icon_value=0)
        # row.popover('VIEW3D_PT_snapping', text="Snapping", text_ctxt="", translate=True, icon='SNAP_ON', icon_value=0) 
    
    # def draw(self, context):
    #     tool_settings = context.tool_settings

    #     layout = self.layout
    #     layout.use_property_decorate = True
    #     layout.use_property_split = False
    #     layout.grid_flow(row_major=True, columns=3, even_columns=False, even_rows=False, align=False)
    #     layout.ui_units_x = 8.0        
    #     row = layout.row(align=True)        
    #     row.prop(tool_settings, "use_snap", text="")
    #     row.prop(tool_settings, "use_mesh_automerge", text="")

class IOPS_OT_transform_orientation_global(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.transform_orientation_global"
    bl_label = "Transformation orientation: GLOBAL"    

    def execute(self, context):
        bpy.ops.transform.select_orientation(orientation='GLOBAL')
        return {'FINISHED'}

class IOPS_OT_transform_orientation_local(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.transform_orientation_local"
    bl_label = "Transformation orientation: LOCAL"    

    def execute(self, context):
        bpy.ops.transform.select_orientation(orientation='LOCAL')
        return {'FINISHED'}

class IOPS_OT_transform_orientation_normal(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.transform_orientation_normal"
    bl_label = "Transformation orientation: NORMAL"    

    def execute(self, context):
        bpy.ops.transform.select_orientation(orientation='NORMAL')
        return {'FINISHED'}

class IOPS_OT_transform_orientation_gimbal(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.transform_orientation_gimbal"
    bl_label = "Transformation orientation: GIMBAL"    

    def execute(self, context):
        bpy.ops.transform.select_orientation(orientation='GIMBAL')
        return {'FINISHED'}

class IOPS_OT_transform_orientation_view(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.transform_orientation_view"
    bl_label = "Transformation orientation: VIEW"    

    def execute(self, context):
        bpy.ops.transform.select_orientation(orientation='VIEW')
        return {'FINISHED'}

class IOPS_OT_transform_orientation_cursor(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.transform_orientation_cursor"
    bl_label = "Transformation orientation: CURSOR"    

    def execute(self, context):
        bpy.ops.transform.select_orientation(orientation='CURSOR')
        return {'FINISHED'}

class IOPS_OT_pivot_point_bbox(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.pivot_point_bbox"
    bl_label = "Pivot point: Bounding box"    

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'
        return {'FINISHED'}

class IOPS_OT_pivot_point_cursor(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.pivot_point_cursor"
    bl_label = "Pivot point: 3D Cursor"    

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        return {'FINISHED'}

class IOPS_OT_pivot_point_individual_origins(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.pivot_point_individual_origins"
    bl_label = "Pivot point: Individual origins"    

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
        return {'FINISHED'}

class IOPS_OT_pivot_point_median_point(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.pivot_point_median_point"
    bl_label = "Pivot point: Median point"    

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
        return {'FINISHED'}

class IOPS_OT_pivot_point_active_element(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.pivot_point_active_element"
    bl_label = "Pivot point: Active element"    

    def execute(self, context):
        context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
        return {'FINISHED'}

class IOPS_OT_snap_target_closest(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.snap_target_closest"
    bl_label = "Snap target: Closest"    

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
        return {'FINISHED'}

class IOPS_OT_snap_target_center(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.snap_target_center"
    bl_label = "Snap target: Center"    

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target = 'CENTER'
        return {'FINISHED'}

class IOPS_OT_snap_target_median(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.snap_target_median"
    bl_label = "Snap target: Median"    

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target = 'MEDIAN'
        return {'FINISHED'}

class IOPS_OT_snap_target_active(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "iops.snap_target_active"
    bl_label = "Snap target: Active"    

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
        return {'FINISHED'}


class IOPS_PT_iops_tm_panel(bpy.types.Panel):
    """Creates a Panel from Tranformation,PivotPoint,Snapping panels"""
    bl_label = "IOPS TPS"
    bl_idname = "IOPS_PT_iops_tm_panel" 
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item' 

    def draw(self, context):
        tool_settings = context.tool_settings
        layout = self.layout
        layout.ui_units_x = 20.0
                 
        row = layout.row(align=True)
        row.prop(tool_settings, "use_snap", text="")
        row.prop(tool_settings, "use_mesh_automerge", text="")
        split = layout.split()        
        col = split.column(align=True) 
        col.label(text="Transformation") 
                  
        col.operator("iops.transform_orientation_global", text="Global", icon='ORIENTATION_GLOBAL')
        col.operator("iops.transform_orientation_local", text="Local", icon='ORIENTATION_LOCAL')
        col.operator("iops.transform_orientation_normal", text="Normal", icon='ORIENTATION_NORMAL')
        col.operator("iops.transform_orientation_gimbal", text="Gimbal", icon='ORIENTATION_GIMBAL')
        col.operator("iops.transform_orientation_view", text="View", icon='ORIENTATION_VIEW')
        col.operator("iops.transform_orientation_cursor", text="Cursor", icon='ORIENTATION_CURSOR')
        
        col = split.column(align=True) 
        col.label(text="PivotPoint") 
        col.operator("iops.pivot_point_bbox", text="Bbox center", icon='PIVOT_BOUNDBOX')
        col.operator("iops.pivot_point_cursor", text="3D Cursor", icon='PIVOT_CURSOR')
        col.operator("iops.pivot_point_individual_origins", text="Individual origins", icon='PIVOT_INDIVIDUAL')
        col.operator("iops.pivot_point_median_point", text="Median point", icon='PIVOT_MEDIAN')
        col.operator("iops.pivot_point_active_element", text="Active element", icon='PIVOT_ACTIVE')       
        col.prop(tool_settings, "use_transform_pivot_point_align", text="")
        
        col = split.column(align=True)        
        col.label(text="Snapping:")
        row = col.row(align=False)        
        row.prop(tool_settings, "snap_elements", text="")
        col.operator("iops.snap_target_closest", text="Closest")
        col.operator("iops.snap_target_center", text="Center")
        col.operator("iops.snap_target_median", text="Median")
        col.operator("iops.snap_target_active", text="Active")
        row = col.row(align=False)
        row.prop(tool_settings, "use_snap_translate", text="", icon='CON_LOCLIMIT')
        row.prop(tool_settings, "use_snap_rotate", text="", icon='CON_ROTLIMIT')
        row.prop(tool_settings, "use_snap_scale", text="", icon='CON_SIZELIMIT')


class IOPS_PT_iops_transform_panel(bpy.types.Panel):
    """Creates a Panel from Tranformation,PivotPoint,Snapping panels"""
    bl_label = "IOPS TM"
    bl_idname = "IOPS_PT_iops_transform_panel" 
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'    
    bl_options = {'DEFAULT_CLOSED'}    

    @classmethod
    def poll(self, context):
        return (context.area.type == "VIEW_3D" and                
                len(context.view_layer.objects.selected) != 0 and
                context.view_layer.objects.active.type == "MESH") 

    def draw(self, context):        
        obj = context.view_layer.objects.active
        layout = self.layout
        layout.ui_units_x = 8.0      
        col = layout.column(align=True)
        col.prop(obj, "location")
        col.prop(obj, "rotation_euler")
        col.prop(obj, "scale")
        col.prop(obj, "dimensions")
        


        


        



        
