#notes app using python and tkinter
import tkinter as tk
from tkinter import messagebox
import os
import json
NOTES_FILE = "notes.json"
class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes App")
        self.notes = self.load_notes()
        self.create_widgets()
        self.refresh_notes_list()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, height=15, width=50)
        self.text_area.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Note", command=self.add_note)
        self.add_button.pack(pady=5)

        self.notes_listbox = tk.Listbox(self.root, width=50)
        self.notes_listbox.pack(pady=10)
        self.notes_listbox.bind('<<ListboxSelect>>', self.display_note)

        self.delete_button = tk.Button(self.root, text="Delete Note", command=self.delete_note)
        self.delete_button.pack(pady=5)

    def load_notes(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, 'r') as f:
                return json.load(f)
        return []

    def save_notes(self):
        with open(NOTES_FILE, 'w') as f:
            json.dump(self.notes, f)

    def add_note(self):
        note_text = self.text_area.get("1.0", tk.END).strip()
        if note_text:
            self.notes.append(note_text)
            self.save_notes()
            self.refresh_notes_list()
            self.text_area.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Input Error", "Note cannot be empty.")

    def delete_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.notes[index]
            self.save_notes()
            self.refresh_notes_list()
            self.text_area.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Selection Error", "No note selected.")

    def refresh_notes_list(self):
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            self.notes_listbox.insert(tk.END, note[:30] + ("..." if len(note) > 30 else ""))

    def display_note(self, event):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            note_text = self.notes[index]
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, note_text)
if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
