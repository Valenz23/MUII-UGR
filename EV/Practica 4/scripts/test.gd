extends Node3D

signal camara_1
signal camara_2

var camara = "cam1"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_action_pressed("camara1"):
		emit_signal("camara_1")
		camara = "cam1"
	if Input.is_action_pressed("camara2"):
		emit_signal("camara_2")
		camara = "cam2"
