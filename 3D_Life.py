bl_info = {
	"name": "3D Life",
	"category": "Object",
}
import bpy
import math
from bpy_extras.object_utils import object_data_add
import mathutils
import numpy as np
import random

class ThreeD_Life(bpy.types.Operator):
	"""3D Game of Life"""
	bl_idname = "object.three_life"
	bl_label = "3D Life"
	bl_options = {'REGISTER', 'UNDO'}

	dim = bpy.props.IntProperty(name="Simulation Dimensions",default=10,min=3,max=50)
	frames = bpy.props.IntProperty(name="Simulation Frames",default=50,min=3,max=1000)
	step = bpy.props.IntProperty(name="Keyframe Step",default=5,min=1,max=100)

	def execute(self, context):
		scene = context.scene
		dim = self.dim
		status = []
		next = np.empty(math.pow(dim,3))
		cubes = []
		for z in range(0,dim):
			for y in range(0,dim):
				for x in range(0,dim):
					my_list = [0] * 9 + [1] * 1
					status.append(random.choice(my_list))
					bpy.ops.mesh.primitive_cube_add(location=(2*x,2*y,2*z))
					cubes.append(bpy.context.active_object)
					scalekey(cubes[x+dim*y+dim*dim*z],status[x+dim*y+dim*dim*z],0)
		for i in range(self.step,(self.frames+1)*self.step,self.step):
			for z in range(0,dim):
				for y in range(0,dim):
					for x in range(0,dim):
						current = status[x+dim*y+dim*dim*z]
						nextstep = newstatus(checkneighbors(x,y,z,status,dim),current)
						if(current!=nextstep):
							scalekey(cubes[x+dim*y+dim*dim*z],current,i-self.step)
							scalekey(cubes[x+dim*y+dim*dim*z],nextstep,i)
						next[x+dim*y+dim*dim*z]=nextstep
			status = np.empty_like(next)
			status[:] = next
		return {'FINISHED'}
		
def scalekey(obj,s,f):
	obj.scale = (s,s,s)
	obj.keyframe_insert(data_path="scale", frame=f)

def checkneighbors(a,b,c,status,dim):
	living = 0
	for z in range(-1,2):
		for y in range(-1,2):
			for x in range(-1,2):
				if(status[((a+x)%(dim-1))+(dim*((b+y)%(dim-1)))+(dim*dim*((c+z)%(dim-1)))]==1):
					if(abs(x)+abs(y)+abs(z)!=0):
						living+=1
	return living

def newstatus(neighbs,status):
	if(status==0):
		if(neighbs==5):
			return 1
	else:
		if(neighbs==4 or neighbs==5):
			return 1
	return 0

def menu_func(self, context):
	self.layout.operator(ThreeD_Life.bl_idname) 
	
def register():
	bpy.utils.register_class(ThreeD_Life)
	bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
	bpy.utils.unregister_class(ThreeD_Life)
	bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
	register()
