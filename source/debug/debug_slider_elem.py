from godot import exposed, export, HBoxContainer, Node, signal, NodePath
import time

@exposed(tool=True)
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
		self.get_node("NameLabel").text = value
		self._value_name = value

	def _ready(self):
		if self.path_to_node is None or self.property_to_track == "":
			return

		self.value_line_edit = self.get_node("ValueLineEdit")
		self.slider = self.get_node("HSlider")
		self.node_to_track = self.get_node(self.path_to_node)

		self.slider.connect("value_changed", self, "_on_value_changed")
		self.value_line_edit.connect("text_entered", self, "_on_value_changed")
		self._set_initial_value()

	def _set_initial_value(self):
		if not hasattr(self.node_to_track, str(self.property_to_track)):
			return

		value = self.node_to_track.get(self.property_to_track)
		print("now i want to get")
		print(self.node_to_track.get(self.property_to_track))

		if isinstance(value, float):
			self.value_line_edit.text = ("%.2f" % value)
		elif isinstance(value, int):
			self.value_line_edit.text = ("%d" % value)
		else:
			pass
			# for debug purpuses
			# print("unhandled type for %s, value: %s with type: %s" % (self.name, value, type(value)))

	def _on_value_changed(self, value):
	 self.node_to_track.set(self.property_to_track, str(self.slider.value))
	 self.slider.value = float(str(value))
	 self.value_line_edit.text = str(value)
