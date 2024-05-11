from godot import exposed, export, Vector2, Input, StaticBody2D, signal

BASE_HEIGHT = 32.0
SCREEN_SIZE = Vector2(1024, 600)

@exposed
class BasePanel(StaticBody2D):

	speed = export(float, default=600.0)
	bounce = signal()

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

	def _ready(self):
		self._speed = self.speed
		self.direction = Vector2(0.0, 0.0)

	def _physics_process(self, delta):
		self.position += self.direction * delta
		self.global_position = Vector2(self.global_position.x, Helper.clamp(self.global_position.y, self.min_y, self.max_y))

class Helper():
	 def clamp(n, smallest, largest):
			return max(smallest, min(n, largest))
