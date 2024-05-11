from godot import exposed, export, Vector2, KinematicBody2D

MAX_SPEED = 5000.0
START_DIRECTION = Vector2(1.0, 0.4)

@exposed
class Ball(KinematicBody2D):
	direction = START_DIRECTION
	speed = 10.0

	def _ready(self):
		pass

	def _process(self, delta):
		velocity = self.direction * self.speed
		collision = self.move_and_collide(velocity)
		if collision:
			reflection = self.direction - Vector2(2.0, 2.0) * self.direction.dot(collision.normal) * collision.normal
			self.direction = reflection

			if collision.collider.is_in_group("panels"):
				self.speed *= 1.05
				self.speed = min(self.speed, MAX_SPEED)
				collision.collider.register_bounce()
