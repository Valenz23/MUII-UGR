extends Node3D

var velocidad = 5

var rotacionY = 0
var minY = -270
var maxY = 270

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):	

	var movimientoY = 0
	
	if Input.is_action_pressed("camara izquierda"):
		if rotacionY > minY:
			movimientoY -= velocidad * delta
			rotacionY -= velocidad
		
	if Input.is_action_pressed("camara derecha"):
		if rotacionY < maxY:
			movimientoY += velocidad * delta
			rotacionY += velocidad
			
	#print(rotacionY)
	
	rotate_y(movimientoY)

