extends Node3D

var velocidad = 5

var rotacionZ = 0
var minZ = -25
var maxZ = 150

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):	

	var movimientoZ = 0	
		
	if Input.is_action_pressed("camara arriba"):
		if rotacionZ < maxZ:
			movimientoZ += velocidad * delta
			rotacionZ += velocidad
		
	if Input.is_action_pressed("camara abajo"):
		if rotacionZ > minZ:
			movimientoZ -= velocidad * delta
			rotacionZ -= velocidad				
	
	#print(rotacionZ)

	rotate_z(movimientoZ)
