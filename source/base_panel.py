from godot import exposed, export, Vector2, Input, StaticBody2D

BASE_HEIGHT = 32.0
SCREEN_SIZE = Vector2(1024, 600)

@exposed
class BasePanel(StaticBody2D):

	speed = export(float)

	@export(float)
	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self.scale = Vector2(1.0, value / BASE_HEIGHT)
		self.min_y = 0.0 + value
		self.max_y = SCREEN_SIZE.y - value
		self._height = value

	def move_up(self):
		self.direction = -Vector2(0.0, self._speed)

	def move_down(self):
		self.direction = +Vector2(0.0, self._speed)

	def stop(self):
		self.direction = Vector2(0.0, 0.0)

	def register_bounce(self):
		#TODO: Add +1 to player data
		pass

	def _ready(self):
		self._speed = self.speed
		self.direction = Vector2(0.0, 0.0)

	def _physics_process(self, delta):
		self.position += self.direction * delta
		self.global_position = Vector2(self.global_position.x, Helper.clamp(self.global_position.y, self.min_y, self.max_y))

		# --- Actually, this block belongs to Player ---
		if Input.is_action_just_pressed("p1_move_up"):
			self.move_up()
		if Input.is_action_just_pressed("p1_move_down"):
			self.move_down()
		if (Input.is_action_just_released("p1_move_up")
			and not Input.is_action_pressed("p1_move_down")):
			self.stop()
		if (Input.is_action_just_released("p1_move_down")
			and not Input.is_action_pressed("p1_move_up")):
			self.stop()
		# ----------------------------------------------
class Helper():
	 def clamp(n, smallest, largest):
			return max(smallest, min(n, largest))
