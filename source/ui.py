from godot import exposed, export, CanvasLayer, Label, AnimationPlayer

@exposed
class UI(CanvasLayer):

	@property
	def score_label(self):
		return self._score_label

	@score_label.setter
	def score_label(self, value):
		self._score_label = value

	@export(AnimationPlayer)
	@property
	def anim_player(self):
	  return self._anim_player

	@anim_player.setter
	def anim_player(self, value):
	  self._anim_player = value

	def _ready(self):
		self.score_label = self.get_node("ScoreLabel")
		self.anim_player = self.get_node("AnimationPlayer")
		self.anim_player.connect("animation_finished", self, "_on_anim_finished")

	def update(self, new_score):
		self.score_label.text = f"Score: {new_score}"

	def play_game_over_anim(self):
		self.anim_player.play("game_over")

	def play_anim(self, anim_name):
		self.anim_player.play(anim_name)

	def _on_anim_finished(self, anim_name):
		anim_name = str(anim_name)
		if anim_name == 'game_over':
			self.anim_player.play("prepare")
		elif anim_name == "prepare":
			self.anim_player.play("go")
