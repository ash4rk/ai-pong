from godot import exposed, export, Node, signal

@exposed
class Training(Node):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		self._score = value
		self.ui.update(value)

	def _ready(self):
		self.get_node("PlayerGates").connect("goal", self, "_on_goal")
		self.player_1 = self.get_node("PlayerOneControl")
		self.player_1.panel.connect("bounce", self, "_on_bounce")
		self.ui = self.get_node("UI_Layer")
		self.score = 0

	def _on_goal(self):
		print("GOAL FROM TRAINING")

	def _on_bounce(self):
		self.score += 1
		print("BOUNCE FROM TRAINING")
