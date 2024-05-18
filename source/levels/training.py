from godot import exposed, export, Node, signal
import time

INIT_GAME_SPEED = 1.0

@exposed
class Training(Node):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		self._score = int(str(value))
		self.ui.update(value)

	@property
	def game_speed(self):
		return self._game_speed

	@game_speed.setter
	def game_speed(self, value):
		print("game_speed changed!")
		self._game_speed = float(str(value))

	def _ready(self):
		self.game_speed = INIT_GAME_SPEED
		self.get_node("PlayerGates").connect("goal", self, "_on_goal")
		self.player_1 = self.get_node("Player")
		self.player_1.panel.connect("bounce", self, "_on_bounce")
		self.ball = self.get_node("Ball")
		self.ui = self.get_node("UI_Layer")
		self.ui.anim_player.connect("animation_finished", self, "_on_anim_finished")
		self.score = 0

	def _on_goal(self):
		self.ball.set_process(False)
		self.player_1.set_physics_process(False)
		self.player_1.set_process(False)
		self.ui.play_game_over_anim()

	def _on_anim_finished(self, anim_name):
		if str(anim_name) == "game_over":
			self.ball.reset()
			self.player_1.panel.stop()
			self.player_1.reset()
			self.score = 0
		elif str(anim_name) == "prepare":
			pass
		elif str(anim_name) == "go":
			self.ball.set_process(True)
			self.player_1.set_physics_process(True)
			self.player_1.set_process(True)

	def _on_bounce(self):
		self.score += 1
