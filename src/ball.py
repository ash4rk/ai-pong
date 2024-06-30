from godot import exposed, export, Vector2, KinematicBody2D, NodePath

MAX_SPEED = 5000.0
START_SPEED = 10.0
START_DIRECTION = Vector2(1.0, 0.4)
DEFAULT_ACCELERATION_FACTOR = 1.0

@exposed
class Ball(KinematicBody2D):

	direction = START_DIRECTION

	@property
	def speed(self):
		return self._speed

	@speed.setter
	def speed(self, value):
		self._speed = float(str(value))

	@property
	def acceleration_factor(self):
		return self._acceleration_factor

	@acceleration_factor.setter
	def acceleration_factor(self, value):
		self._acceleration_factor = float(str(value))

	def _ready(self):
		print("ball _ready")
		self.start_pos = self.global_position
		self.acceleration_factor = DEFAULT_ACCELERATION_FACTOR
		self.reset()
		self.game = self.get_node("../Game")
		self.game.ball = self

	def reset(self):
		self.global_position = self.start_pos
		self.direction = START_DIRECTION
		self.speed = START_SPEED

	def _process(self, delta):
		velocity = self.direction * self.speed * self.game.game_speed
		collision = self.move_and_collide(velocity)
		if collision:
			reflection = self.direction - Vector2(2.0, 2.0) * self.direction.dot(collision.normal) * collision.normal
			self.direction = reflection

			if collision.collider.is_in_group("panels"):
				self.speed *= self.acceleration_factor
				self.speed = min(self.speed, MAX_SPEED)
				collision.collider.call("emit_signal", "bounce")

			if collision.collider.is_in_group("gates"):
				collision.collider.call("emit_signal", "goal")
