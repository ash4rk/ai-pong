from godot import exposed, export, HBoxContainer, Node, signal, NodePath
import time

@exposed(tool=False)
class DebugElem(HBoxContainer):
	value_changed = signal()

	path_to_node = export(NodePath)
	property_to_track = export(str, default="")

	@export(str)
	@property
	def value_name(self):
		return self._value_name

	@value_name.setter
	def value_name(self, value):
		self.get_node("NameLabel").text = str(value)
		self._value_name = value

	def _ready(self):
		if self.path_to_node is None or self.property_to_track == "":
			return

		self.value_label = self.get_node("ValueLabel")
		self.value_text_edit = self.get_node("ValueLineEdit")
		self.change_btn = self.get_node("ChangeButton")
		self.node_to_track = self.get_node(self.path_to_node)

		self.change_btn.connect("pressed", self, "_on_change_btn_pressed")

	def _process(self, delta):
		if not hasattr(self, "node_to_track"):
			return

		value = self.node_to_track.get(self.property_to_track)

		if isinstance(value, float):
			self.value_label.text = ("%.2f" % value)
		elif isinstance(value, int):
			self.value_label.text = ("%d" % value)
		else:
			pass
			# for debug purpuses
			# print("unhandled type for %s, value: %s with type: %s" % (self.name, value, type(value)))


	def _on_change_btn_pressed(self):
		 self.node_to_track.set(self.property_to_track, float(str(self.value_text_edit.text)))
