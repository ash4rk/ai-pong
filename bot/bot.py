from godot import exposed

from source.p1_control import PlayerOneControl


@exposed
class BotPlayer(PlayerOneControl):

	upper_bound = 150
	lower_bound = 450

	def __init__(self, panel):
		super().__init__(panel)

	def _ready(self):
		super()._ready()

	def _physics_process(self, delta):

		if self.panel.global_position.y >= self.lower_bound:
			self.panel.move_up()

		if self.panel.global_position.y <= self.upper_bound:
			self.panel.move_down()

	def reset(self):
		super().reset()
		self.panel.move_down()
