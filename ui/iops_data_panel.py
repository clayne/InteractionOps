import bpy

class IOPS_PT_DATA_Panel(bpy.types.Panel):
    """Tranformation,PivotPoint,Snapping panel"""
    bl_label = "IOPS TPS"
    bl_idname = "IOPS_PT_DATA_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    # bl_category = 'Item'

    def draw(self, context):
        wm = context.window_manager        
        tool_settings = context.tool_settings
        scene = context.scene  
        props = wm.IOPS_AddonProperties 

        layout = self.layout
        layout.ui_units_x = 27.5
        row = layout.row(align=True)
             
        row.operator("iops.homonize_uvmaps_names", text="", icon='UV_DATA')
        # row.operator("iops.uvmaps_cleanup", text="", icon='BRUSH_DATA')
        row.separator()
        row.operator("iops.clean_uvmap_0", text="All")
        row.operator("iops.clean_uvmap_1", text="2+")
        row.operator("iops.clean_uvmap_2", text="3+")
        row.operator("iops.clean_uvmap_3", text="4+")
        row.operator("iops.clean_uvmap_4", text="5+")
        row.operator("iops.clean_uvmap_5", text="6+")
        row.operator("iops.clean_uvmap_6", text="7+")
        row.operator("iops.clean_uvmap_7", text="8")
            
        row.separator()

        if context.area.type == "VIEW_3D" and context.active_object.type == 'MESH':
            ob = context.object
            me = ob.data
            brush = context.tool_settings.vertex_paint.brush

            # split = layout.split()
            row_main = layout.row(align=True)                    
            col = row_main.column(align=True)                                       
            # UV Panel
            col.label(text="UVMaps:")
            row = col.row(align=True)
            row.template_list("MESH_UL_uvmaps", "uvmaps", me, "uv_layers", me.uv_layers, "active_index", rows=5)
            col = row.column(align=True)
            # col.operator("mesh.uv_texture_add", icon='ADD', text="")
            # col.operator("mesh.uv_texture_remove", icon='REMOVE', text="")            
            col.operator("iops.add_uvmap", icon='ADD', text="")
            col.operator("iops.remove_uvmap_by_active_name", icon='REMOVE', text="")
            col.operator("iops.active_uvmap_by_active_object", icon='LAYER_ACTIVE', text="")
            # SEPARATORS------------------------------------
            row_main.separator()
            row_main.separator()
            # ----------------------------------------------
            # VertexColor
            col = row_main.column(align=True) 
            col.label(text="VertexColor:")
            row = col.row(align=True)
            row.template_list("MESH_UL_vcols", "vcols", me, "vertex_colors", me.vertex_colors, "active_index", rows=5)
            col = row.column(align=True)
            col.operator("mesh.vertex_color_add", icon='ADD', text="")
            col.operator("mesh.vertex_color_remove", icon='REMOVE', text="")
            # SEPARATORS------------------------------------
            row_main.separator()
            row_main.separator()
            # ----------------------------------------------
            # VertexGroups
            group = ob.vertex_groups.active
            
            col_vg = row_main.column(align=True) 
            col_vg.label(text="VertexGroups:")
            row = col_vg.row(align=True)
            row.template_list("MESH_UL_vgroups", "", ob, "vertex_groups", ob.vertex_groups, "active_index", rows=5)
            col = row.column(align=True)                   
            col.operator("object.vertex_group_add", icon='ADD', text="")
            props = col.operator("object.vertex_group_remove", icon='REMOVE', text="")
            props.all_unlocked = props.all = False
            col.menu("MESH_MT_vertex_group_context_menu", icon='DOWNARROW_HLT', text="")

            if group:
                    col.separator()
                    col.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                    col.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

            if (
                    ob.vertex_groups and
                    (ob.mode == 'EDIT' or
                    (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH' and ob.data.use_paint_mask_vertex))
                ):

                col = col_vg.row(align=True)

                sub = col.row(align=True)
                sub.scale_x = 0.45
                # sub.ui_units_x = 2.0
                sub.operator("object.vertex_group_assign", text="Assign")
                sub.operator("object.vertex_group_remove_from", text="Remove")
                sub.separator()
                sub.operator("object.vertex_group_select", text="Select")
                sub.operator("object.vertex_group_deselect", text="Deselect")

                col = col_vg.row(align=True)
                col.prop(context.tool_settings, "vertex_group_weight", text="Weight")


class IOPS_OT_Call_Data_Panel(bpy.types.Operator):
    """Active object data(mesh) information"""
    bl_idname = "iops.call_data_panel"
    bl_label = "IOPS Data panel"

    @classmethod
    def poll(cls, context):
        return context.area.type == "VIEW_3D" and context.object.type == "MESH"

    def execute(self, context):
        bpy.ops.wm.call_panel(name="IOPS_PT_DATA_Panel", keep_open=True)
        return {'FINISHED'}

        