"""
This script gets the world coordinates of the chosen (primitive) object.
"""

import bpy
import mathutils

print("\n" * 3)

def get_world_matrix(obj):
    if obj.parent:
        return obj.parent.matrix_world @ obj.matrix_local
    else:
        return obj.matrix_world

selected_object_name = "Cube"  # Change this to your selected object's name

selected_object = bpy.data.objects.get(selected_object_name)

object_vertices = []

if selected_object:
    if selected_object.type == "MESH":
        mesh = selected_object.data
        
        world_matrix = get_world_matrix(selected_object)
        
        print("Vertices of " + selected_object.name)
        for vertex in mesh.vertices:
            world_vertex = world_matrix @ vertex.co
            object_vertices.append(world_vertex.to_tuple())
        
        print(object_vertices)
        
        flattened = [value for vertex in object_vertices for value in vertex]
#        print(flattened)
            
    else:
        print("Selected object is not a mesh")
else:
    print("No selected object")
