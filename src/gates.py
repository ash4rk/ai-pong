from godot import exposed, export, StaticBody2D, signal

@exposed
class Gates(StaticBody2D):
    goal = signal()

    def _ready(self):
        self.connect("goal", self.get_node("../Game"), "on_goal")
