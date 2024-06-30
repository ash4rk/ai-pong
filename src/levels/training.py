from godot import exposed, export, Node, signal
import time

INIT_GAME_SPEED = 1.0

@exposed
class Training(Node):
	game_started = signal()
	game_over = signal()

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		self._score = int(str(value))
		if hasattr(self, "ui"):
			self.ui.update(value)

	@export(float)
	@property
	def game_speed(self):
		return self._game_speed

	@game_speed.setter
	def game_speed(self, value):
		self._game_speed = float(str(value))

	@export(Node)
	@property
	def player(self):
		return self._player

	@player.setter
	def player(self, value):
		print("player changed!")
		value.panel.connect("bounce", self, "_on_bounce")
		value.panel.set_physics_process(False)
		self._player = value

	@export(Node)
	@property
	def ball(self):
		return self._ball

	@ball.setter
	def ball(self, value):
		print("ball changed!")
		value.set_process(False)
		self._ball = value

	@export(Node)
	@property
	def ui(self):
		return self._ui

	@ui.setter
	def ui(self, value):
		print("ui changed!")
		value.anim_player.connect("animation_finished", self, "_on_anim_finished")
		self._ui = value
		self.score = 0

	def _ready(self):
		print("Training _ready")
		self.game_speed = INIT_GAME_SPEED

	def on_goal(self):
		self.call("emit_signal", "game_over", self.score)
		self.ball.set_process(False)
		self.player.panel.set_physics_process(False)
		self.ui.play_game_over_anim()

	def _on_anim_finished(self, anim_name):
		if str(anim_name) == "game_over":
			self.ball.reset()
			self.player.panel.stop()
			self.player.reset()
			self.score = 0
		elif str(anim_name) == "prepare":
			pass
		elif str(anim_name) == "go":
			self.call("emit_signal", "game_started")
			self.ball.set_process(True)
			self.player.panel.set_physics_process(True)

	def _on_bounce(self):
		self.score += 1
