from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Create dynamic labels"""

    def __init__(self):
        """Construct main app"""
        super().__init__()
        self.names = ["Pipin", "Gayle", "Ali", "Kylie"]

    def build(self):
        """Build kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list to names and add them to GUI"""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = (1, 0, 1, 1)
            temp_label.font_size = 42
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
