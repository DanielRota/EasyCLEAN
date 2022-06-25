from ddx import gdb
from ddx.gdb import cad, view
from ddx.gdb import region
from sclcore import Vec3, do_debug
import math

# Returns the current Path


def current_path():
    part = cad.get_current_part()
    lay = cad.get_current_layer()
    path = gdb.join_path(part, lay)
    return path

# Hides everything except the selected area


def hide_useles():
    gdb.invert_selection()
    entities = gdb.get_selection()
    gdb.reset_selection()
    if len(entities) == 0:
        return None
    else:
        for entity in entities:
            gdb.show(entity, show_ent=False)

# Deletes texts, quotes, circles and surfaces


def clear_main_area(array):
    path = cad.get_current_part()
    types_to_delete = []
    if array[0]:
        types_to_delete.append(gdb.EntityType.TEXT)
    if array[1]:
        types_to_delete.append(gdb.EntityType.CIRC)
    if array[2]:
        types_to_delete.append(gdb.EntityType.DIM)
    if array[3]:
        types_to_delete.append(gdb.EntityType.POLYMESH)

    entities_to_delete = gdb.get_entitites_by_type(
        path, ent_filter=types_to_delete, only_visible=True, depth_level=1)

    for entity in entities_to_delete:
        gdb.delete(entity)

    # Doesn't reset anything
    if array[0] and array[1] and array[2] and array[3] == False:
        gdb.reset_selection()
        pass

# Gets the point where the tool has to start from


def get_origin_line():
    origin_line = gdb.get_selection()
    if len(origin_line) != 1:
        pass  # CONTROLLO
    else:
        gdb.reset_selection()
        return origin_line[-1]


def get_axis(origin_line):
    axis_line = gdb.get_selection()
    if len(axis_line) != 1:
        pass  # CONTROLLO
    else:
        gdb.reset_selection()
        cad.trim_extend(str(origin_line), str(axis_line[-1]), 0, 0)
# Get knives and extends them to the support's line, then gets the shape and returns it


def get_shape(origin_line):
    max_points = []
    path = current_path()
    part = cad.get_current_part()
    layers = cad.get_layers(part)
    knives = gdb.get_selection()
    if len(knives) == 0:
        return None
    else:
        origin_min, origin_max = gdb.get_extension(origin_line)
        for knife in knives:
            _, knife_max = gdb.get_extension(knife)
            max_points.append(knife_max.x)
        if max(max_points) >= origin_max.x:
            origin_point = origin_max
        else:
            origin_point = origin_min

        rotate_project(origin_line, origin_point, knives)
        vert_line = cad.add_line_2p(
            path, origin_point, Vec3(origin_point.x, 0), cad.StandardColors.BLACK)
        gdb.reset_selection()
        for knife in knives:
            min_point, max_point = gdb.get_extension(knife)
            if math.isclose(min_point.y, max_point.y, abs_tol=1e-9):
                try:
                    cad.trim_extend(str(knife), str(vert_line), 0, 0)
                except:
                    pass
        path = current_path()
        part = cad.get_current_part()
        shape_layer = gdb.join_path(part, 'ShapeLay')
        gdb.delete(shape_layer)
        gdb.add_layer(part, 'ShapeLay')
        with gdb.temp_layer(part, 'TempLay') as temp_layer:
            for knife in knives:
                gdb.change_layer(str(knife), temp_layer,
                                 create_copy=True, keep_pos=True)
            es_min, es_max = gdb.get_extension(origin_line)
            width = es_max.x - es_min.x
            end_tool, _ = gdb.get_extension(temp_layer)
            lenght = origin_point.y - end_tool.y
            
            origin_min, origin_max = gdb.get_extension(origin_line)
            cad.add_rectangle(temp_layer, origin_min, width, -lenght,
                              material=cad.StandardColors.YELLOW)
            region.get_loops_from_curves(temp_layer, shape_layer, Type=1)

        entities = gdb.get_entities(path)
        for entity in entities:
            if entity != vert_line:
                gdb.show(entity, show_ent=False)
        final_path = gdb.join_path(shape_layer, 'EXT_LOOP(1)')
        final_lines = gdb.get_entities(final_path)
        lays = cad.get_layers(part=None)
        for i in lays:
            item = gdb.join_path(part, i)
            if item == shape_layer:
                for final_lay in gdb.get_entities(shape_layer):
                    if final_lay == final_path:
                        for line in final_lines:
                            cad.set_material(
                                line, cad.StandardColors.BLUE_DARK)
                    else:
                        gdb.show(final_lay, show_ent=False)
            else:
                gdb.show(item, show_ent=False)
        gdb.merge_layer(final_path, shape_layer, keep_pos=True, keep_original=False)
        return shape_layer, origin_point, origin_line, origin_max

# Mirrors the shape if necessary and moves it to the origin


def mirror_move(shape_layer, origin_point, origin_line, origin_max):
    p_min, p_max = gdb.get_extension(shape_layer)
    shape_lines = gdb.get_entities(shape_layer)
    if p_max.x < origin_max.x or math.isclose(p_max.x, origin_max.x, abs_tol=1e-05):
        cad.mirror(cad.MirrorType.HORIZONTAL, shape_lines,
                   origin_point, keep_original=False)
    gdb.delete_entity(origin_line)
    p_min, p_max = gdb.get_extension(shape_layer)
    cad.move_entities(shape_lines, from_x=p_min.x, from_y=p_max.y)
    part = cad.get_current_part()
    lines = gdb.get_entitites_by_type(
        part, ent_filter=[gdb.EntityType.LINE], only_visible=True, depth_level=10)
    for entity in lines:
        e_min, e_max = gdb.get_extension(entity)
        if math.isclose(e_min.x, 0, abs_tol=1e-06) and math.isclose(e_max.x, 0, abs_tol=1e-06):
            gdb.delete_entity(entity)


def color_sharp():
    sharp = gdb.get_selection()
    if len(sharp) != 0:
        for entity in sharp:
            cad.set_material(entity, cad.StandardColors.RED)
        return True
    else:
        return False

# Rotates the whole ptoject


def rotate_project(origin_line, origin_point, knives):
    part = cad.get_current_part()
    
    origin_angle = gdb.get_angle(origin_line)

    gdb.add_layer(part, 'SideLay')

    with gdb.temp_layer(part, 'SideLay') as side_layer:
        for knife in knives:
            gdb.change_layer(str(knife), side_layer,
                             create_copy=True, keep_pos=True)

        if get_side(origin_line, side_layer):
            angle_change = -origin_angle
        else:
            angle_change = abs(180 - origin_angle)
        path = cad.get_current_part()
        layers = gdb.get_entities(path)
        
        if not math.isclose(angle_change, 180, abs_tol=1e-19):
            if not math.isclose(angle_change, -180, abs_tol=1e-19):
                if not math.isclose(angle_change, 0, abs_tol=1e-19):
                    for layer in layers:
                        lay_name, group = gdb.split_name_group(layer)
                        cad.set_current_layer(group, lay_name)
                        cad.rotate(layer, origin_point.x, origin_point.y,
                                   angle_change, keep=False)
        view.redraw_window()


def get_side(origin_line, side_layer):
    middle_origin = gdb.get_middle_point(origin_line)
    p_min, p_max = gdb.get_extension(side_layer)
    l = cad.add_line_2p(side_layer, p_min, p_max, cad.StandardColors.BLACK)
    middle = gdb.get_middle_point(l)
    c = cad.add_line_2p(side_layer, middle_origin,
                        middle, cad.StandardColors.BLACK)
    x = gdb.get_angle(c)
    angle = x % 360
    #gdb.delete_entity(l)
    #gdb.delete_entity(c)
    if angle <= 90 or angle > 270:
        return False
    elif 90 < angle or angle <= 270:
        return True
