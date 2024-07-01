extends MeshInstance3D

var TAM = 1

func _ready():
	
	var surface_array = []
	surface_array.resize(Mesh.ARRAY_MAX)

	var vertices = PackedVector3Array()	
	var caras = PackedInt32Array()
	
	# VERTICES
	vertices.append_array([
		Vector3(-TAM, -TAM, -TAM),
		Vector3(TAM, -TAM, -TAM),
		Vector3(TAM, TAM, -TAM),
		Vector3(-TAM, TAM, -TAM),
		Vector3(-TAM, -TAM, TAM),
		Vector3(TAM, -TAM, TAM),
		Vector3(TAM, TAM, TAM),
		Vector3(-TAM, TAM, TAM)
	])
	
	# CARAS
	caras.append_array([
		0, 1, 2,
		0, 2, 3, 
		1, 5, 6, 
		1, 6, 2, 
		5, 4, 7, 
		5, 7, 6,
		4, 0, 3, 
		4, 3, 7,
		3, 2, 6, 
		3, 6, 7, 
		4, 5, 1, 
		4, 1, 0  
	])	

	surface_array[Mesh.ARRAY_VERTEX] = vertices
	surface_array[Mesh.ARRAY_INDEX] = caras

	mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, surface_array)

func _process(delta):
	pass
