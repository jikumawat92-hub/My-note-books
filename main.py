from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

FILE = "my_notes.txt"


class NotesApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        title = Label(
            text="📝 My Notes",
            font_size=30,
            size_hint_y=None,
            height=60
        )

        self.note = TextInput(
            hint_text="Write your note...",
            multiline=True
        )

        save_btn = Button(
            text="💾 Save Note",
            size_hint_y=None,
            height=60
        )

        view_btn = Button(
            text="📖 View Notes",
            size_hint_y=None,
            height=60
        )

        delete_btn = Button(
            text="🗑️ Delete Notes",
            size_hint_y=None,
            height=60
        )

        self.result = Label(
            text="",
            font_size=18
        )

        save_btn.bind(on_press=self.save_note)
        view_btn.bind(on_press=self.view_notes)
        delete_btn.bind(on_press=self.delete_notes)

        layout.add_widget(title)
        layout.add_widget(self.note)
        layout.add_widget(save_btn)
        layout.add_widget(view_btn)
        layout.add_widget(delete_btn)
        layout.add_widget(self.result)

        return layout

    def save_note(self, instance):
        text = self.note.text.strip()

        if text:
            with open(FILE, "a", encoding="utf-8") as f:
                f.write(text + "\n\n")

            self.result.text = "✅ Note Saved!"
            self.note.text = ""
        else:
            self.result.text = "⚠️ ആദ്യം note എഴുതുക"

    def view_notes(self, instance):
        if os.path.exists(FILE):
            with open(FILE, "r", encoding="utf-8") as f:
                notes = f.read()

            self.result.text = notes if notes.strip() else "📭 No notes"
        else:
            self.result.text = "📭 No notes"

    def delete_notes(self, instance):
        if os.path.exists(FILE):
            os.remove(FILE)

        self.result.text = "🗑️ All notes deleted"


NotesApp().run()
