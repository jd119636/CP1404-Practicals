from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Dynamic labels app"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names_to_show = {
            "Alice": 1,
            "Bob": 2,
            "Charlie": 3,
            "Diana": 4
        }

    def build(self):
        """Loads KV file"""
        self.root = Builder.load_file("dynamic_labels.kv")

        # Create a Label for each name
        for name in self.names_to_show.keys():
            temp_label = Label(text=name, font_size=24)

            # Add each label to the BoxLayout with id 'main'
            self.root.ids.main.add_widget(temp_label)

        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()
