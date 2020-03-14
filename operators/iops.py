import bpy
from ..utils.iops_dict import IOPS_Dict, get_iop


class IOPS_OT_Main(bpy.types.Operator):
    bl_idname = "iops.main"
    bl_label = "IOPS"
    bl_options = {"REGISTER", "UNDO"}

    # modes_3d = {0: "VERT", 1: "EDGE", 2: "FACE"}
    # modes_uv = {0: "VERTEX", 1: "EDGE", 2: "FACE", 3: "ISLAND"}
    # modes_gpen = {0: "EDIT_GPENCIL", 1: "PAINT_GPENCIL", 2: "SCULPT_GPENCIL"}
    # modes_curve = {0: "EDIT_CURVE"}
    # modes_text = {0: "EDIT_TEXT"}
    # modes_meta = {0: "EDIT_META"}
    # modes_lattice = {0: "EDIT_LATTICE"}
    # modes_armature = {0: "EDIT", 1: "POSE"}
    # supported_types = {"MESH", "CURVE", "GPENCIL", "EMPTY", "TEXT", "META", "ARMATURE", "LATTICE"}

    @classmethod
    def poll(cls, context):
        return (bpy.context.object is not None and
                bpy.context.active_object is not None)

    def get_mode_3d(self, tool_mesh):
        mode = ""
        if tool_mesh[0]:
            mode = "VERT"
        elif tool_mesh[1]:
            mode = "EDGE"
        elif tool_mesh[2]:
            mode = "FACE"
        return mode

    def execute(self, context):

        active_object = bpy.context.view_layer.objects.active
        tool_mesh = bpy.context.scene.tool_settings.mesh_select_mode

        type_area = bpy.context.area.type
        type_object = bpy.context.view_layer.objects.active.type
        mode_object = bpy.context.view_layer.objects.active.mode
        mode_mesh = self.get_mode_3d(tool_mesh)
        mode_uv = bpy.context.tool_settings.uv_select_mode
        flag_uv = bpy.context.tool_settings.use_uv_select_sync
        op = self.operator

        query = (type_area, type_object, mode_object, flag_uv, mode_mesh, mode_uv, op)

        tool = bpy.context.tool_settings

        function = get_iop(IOPS_Dict.iops_dict, query)
        function()

        return{"FINISHED"}
        