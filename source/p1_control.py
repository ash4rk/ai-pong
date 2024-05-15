from godot import Input, Node2D, ResourceLoader, export, exposed

PANEL_SCENE = ResourceLoader.load("res://source/base_panel.tscn")


@exposed
class PlayerOneControl(Node2D):
	def __init__(self, panel):
		self.panel = panel

	@export(Node2D)
	@property
	def panel(self):
		return self._panel

	@panel.setter
	def panel(self, value):
		self._panel = value

	def _ready(self):
		self.panel = PANEL_SCENE.instance()
		self.add_child(self.panel)
		self.reset()

	def _physics_process(self, delta):
		if Input.is_action_just_pressed("p1_move_up"):
			self.panel.move_up()
		if Input.is_action_just_pressed("p1_move_down"):
			self.panel.move_down()
		if Input.is_action_just_released("p1_move_up") and not Input.is_action_pressed("p1_move_down"):
			self.panel.stop()
		if Input.is_action_just_released("p1_move_down") and not Input.is_action_pressed("p1_move_up"):
			self.panel.stop()

	def reset(self):
		self.panel.global_position = self.global_position
