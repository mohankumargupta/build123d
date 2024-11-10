from build123d import Mode, BuildPart, Box, Cylinder, export_step, export_stl

def box_builder_mode():
    length, width, height = 80.0, 60.0, 10.0
    with BuildPart() as part:
        Box(length, width, height)
    return part    

def cylinder_builder_mode():
    radius, height = 80.0, 60.0
    with BuildPart() as part:
        Cylinder(radius, height)
    return part


def box_with_hole_builder_mode():
    length, width, height = 280.0, 60.0, 30.0
    hole_diameter, hole_height = 20.0, 100.0
    with BuildPart() as part:
        Box(length, width, height)
        Cylinder(hole_diameter / 2, hole_height, mode=Mode.SUBTRACT)
    return part

def box_algebra_mode():
    length, width, height = 80.0, 60.0, 10.0
    part = Box(length, width, height)
    return part

def cylinder_algebra_mode():
    radius, height = 60.0, 30.0
    part = Cylinder(radius, height)
    return part

# builder mode

#part_builder = box_builder_mode()
#part_builder = box_with_hole_builder_mode()
part_builder = cylinder_builder_mode()

part = part_builder.part


# algebra mode

#part = box_algebra_mode()
#part = cylinder_algebra_mode()


#boo
# export
export_step(part, "main.step")
export_stl(part, "main.stl")
#print(part)




