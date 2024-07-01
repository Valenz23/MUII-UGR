extends Camera3D

@onready var Yaw = get_parent() 	# nodo padre
@export var sensibility = 20		# velocidad de giro
@export var speed = 5				# velocidad de movimiento

var maxX = -.5
var minX = -8.5
var minZ = -4.5
var maxZ = 4

var modoInteraccion = false

func _ready():
	pass 
	
func _input(event):	
	
	var camara = get_node("/root/Test").camara		# variable que he guardado en un autoload
	if camara == "cam2" and not modoInteraccion:
		if event is InputEventMouseMotion:		
			Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)				# captura el raton		
			var mouse_delta = event.relative							# movimiento del raton		
			Yaw.rotation_degrees.y -= mouse_delta.x / sensibility		# YAW, mirar izquierda-derecha		
			rotation_degrees.x -= mouse_delta.y / sensibility			# PITCH, mirar arriba-abajo		
			rotation_degrees.x = clamp(rotation_degrees.x, -80, 80)		# limite mirar arriba-abajo
	
func get_Input():
	var mover = Vector3.ZERO
		
	# movimiento WASD
	if Input.is_action_pressed("moverADELANTE"):
		mover += -global_transform.basis.z
	if Input.is_action_pressed("moverATRAS"):
		mover += global_transform.basis.z
	if Input.is_action_pressed("moverIZQUIERDA"):
		mover += -global_transform.basis.x
	if Input.is_action_pressed("moverDERECHA"):
		mover += global_transform.basis.x
			
	mover.y = 0			# asi evitamos movernos en el Y
	mover = mover.normalized()
	return mover


func _process(delta):
	
		# cerramos aplicacion si pulsamos ESCAPE
	if Input.is_action_pressed("ui_cancel"):
		get_tree().quit()
	
	var camara = get_node("/root/Test").camara		# variable que he guardado en un autoload
	if camara == "cam2":
		
		# cambia el modo interactivo		
		if Input.is_action_just_released("interaccion"):
			modoInteraccion = not modoInteraccion
			
		if modoInteraccion:	 # no se mueve nada y hacemos el raton visible
			Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
		else:	# modo normal
			Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)		
			var input = get_Input()
			var movimiento = Yaw.global_transform.origin + input * speed * delta
			movimiento.x = clamp(movimiento.x, minX, maxX)
			movimiento.z = clamp(movimiento.z, minZ, maxZ)
			Yaw.global_transform.origin = movimiento
		

func _on_test_camara_2():
	set_current(true)
