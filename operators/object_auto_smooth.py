import bpy
from math import radians

# Check box to put the modifier at the top of the stack or bottom

def move_modifier_to_top(obj, mod):
    if obj.modifiers:
        while obj.modifiers[0] != mod:
            bpy.ops.object.modifier_move_up(modifier=mod.name)

class IOPS_OT_AutoSmooth(bpy.types.Operator):
    bl_idname = "iops.object_auto_smooth"
    bl_label = "Add Auto Smooth Modifier"
    bl_options = {"REGISTER", "UNDO"}

    angle: bpy.props.FloatProperty(
        name="Smooth Angle",
        description="Smooth Angle",
        default=30.0,
        min=0.0,
        max=180.0,
    )

    ignore_sharp: bpy.props.BoolProperty(
        name="Ignore Sharp Edges",
        description="Ignore Sharp Edges",
        default=False,
    )

    stack_top: bpy.props.BoolProperty(
        name="Top of Stack",
        description="Add modifier to top of stack",
        default=True,
    )

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == "MESH":
                with context.temp_override(
                    active_object=obj,
                    selected_editable_objects=[obj],
                    selected_objects=[obj],
                ):
                    #Delete existing Auto Smooth modifier
                    for mod in obj.modifiers:
                        if "Auto Smooth" in mod.name and mod.type == "NODES":
                            bpy.ops.object.modifier_remove(modifier=mod.name)
                    
                    #Add Smooth by Angle modifier from Essentials library
                    bpy.ops.object.modifier_add_node_group(
                        asset_library_type="ESSENTIALS",
                        asset_library_identifier="",
                        relative_asset_identifier="geometry_nodes/smooth_by_angle.blend/NodeTree/Smooth by Angle",
                    )
                    mod = obj.modifiers[-1]
                    mod.name = "Auto Smooth"
                    mod["Input_1"] = radians(self.angle)
                    mod["Socket_1"] = self.ignore_sharp

                    if self.stack_top:
                        move_modifier_to_top(obj, mod)
    
        return {"FINISHED"}

