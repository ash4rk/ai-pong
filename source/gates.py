from godot import exposed, export, StaticBody2D, signal

@exposed
class Gates(StaticBody2D):
    goal = signal()
