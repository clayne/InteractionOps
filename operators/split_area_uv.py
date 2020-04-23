import bpy

def ContextOverride():
    for window in bpy.context.window_manager.windows:      
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':            
                for region in area.regions:
                    if region.type == 'WINDOW':               
                        context_override = {'window': window, 
                                            'screen': screen, 
                                            'area': area, 
                                            'region': region, 
                                            'scene': bpy.context.scene, 
                                            'edit_object': bpy.context.edit_object, 
                                            'active_object': bpy.context.active_object, 
                                            'selected_objects': bpy.context.selected_objects
                                            } 
                        return context_override
    raise Exception("ERROR: VIEW_3D not found!")

def collapse_right(join_x, join_y):
    bpy.ops.screen.area_swap(cursor=(join_x, join_y))
    bpy.ops.screen.area_join(cursor=(join_x, join_y))
    context_override = ContextOverride()   
    bpy.ops.screen.screen_full_area(context_override)
    bpy.ops.screen.back_to_previous()

def collapse_left(join_x, join_y):
    bpy.ops.screen.area_swap(cursor=(join_x, join_y))
    bpy.ops.screen.area_join(cursor=(join_x, join_y))
    context_override = ContextOverride()   
    bpy.ops.screen.screen_full_area(context_override)
    bpy.ops.screen.back_to_previous()


class IOPS_OT_SplitAreaUV(bpy.types.Operator):
    bl_idname = "iops.split_area_uv"
    bl_label = "IOPS Split Area UV"

    @classmethod 
    def poll(self, context):
        return context.area.type in ["VIEW_3D","IMAGE_EDITOR"]

    def execute(self,context):
        current_area = context.area
        side_area = None
        join_x = current_area.x + current_area.width + 1
        join_y = int(current_area.y + current_area.height/2)
        current_type = context.area.type # VIEW_3D
        areas = list(context.screen.areas)

        for area in context.screen.areas:
            if area == current_area:
                continue
            elif area.x == join_x and area.y == current_area.y:
                side_area = area
                break

        if side_area and side_area.type == 'IMAGE_EDITOR':
            collapse_right(join_x, join_y)
            return {"FINISHED"}
        
        if current_area.type == 'IMAGE_EDITOR':
            collapse_left(current_area.x, join_y)
            return {"FINISHED"}
        
        else:
            context.area.type = "IMAGE_EDITOR"
            context.area.ui_type = 'UV'
            new_area = None
            bpy.ops.screen.area_split(direction="VERTICAL", factor=0.5)
            for area in context.screen.areas:
                if area not in areas:
                    new_area = area
                    break
            if new_area:
                new_area.type = current_type # VIEW_3D
                return {"FINISHED"}
        
        return {"CANCELLED"}