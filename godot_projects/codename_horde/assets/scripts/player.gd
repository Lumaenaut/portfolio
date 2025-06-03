# The script inherits CharacterBody2D
extends CharacterBody2D

# Exported variables are visible in the inspector
# Type hint:
# 	var name: type (int, float, String, ...)
# Default value
#	var name = value
# Both are also acceptable
#	var name : type = value
#	var name := value
@export var speed := 200.0
@export var jump_velocity := -400.0
@export var gravity := 900.0

func _physics_process(delta):
	'''Runs every physics frame
	
	:param delta: float - elapsed time (seconds) since last frame of this function.
	:return: n/a - function doesn't return a value.
	
	Called during the physics phase of the main loop. The frame rate will be
	synchronized with it.
	The physics process will be enabled if this function is overriden or toggled
	with set_physics_process().
	
	The function will set the speed value and direction of x and y based on the key
	actions when pressed and if the player is in contact with the floor.
	
	'''
	
	var direction = 0.0

	# direction will be set to 1 or -1 depending on the key pressed
	if Input.is_action_pressed("ui_right"):
		direction += 1
	if Input.is_action_pressed("ui_left"):
		direction -= 1

	# velocity is a built-in feature of CharacterBody2D, setting the horizontal
	# speed
	velocity.x = direction * speed

	# if player is in the air the vertical speed will be applied by gravity
	# else it'll respond to jump velocity
	if not is_on_floor(): # <- how does is_on_floor() work?
		velocity.y += gravity * delta
	else:
		if Input.is_action_just_pressed("ui_up"): # <- difference?
			velocity.y = jump_velocity

	# This function handles the player's movement based on the velocity.
	# It will also update collision and "on floor" status.
	move_and_slide()
