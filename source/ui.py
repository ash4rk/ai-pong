from godot import exposed, export, CanvasLayer, Label

@exposed
class UI(CanvasLayer):

	@property
	def score_label(self):
		return self._score_label

	@score_label.setter
	def score_label(self, value):
		self._score_label = value

	def _ready(self):
		self.score_label = self.get_node("ScoreLabel")

	def update(self, new_score):
		self.score_label.text = f"Score: {new_score}"
