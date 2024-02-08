import tkinter as tk

class ChatWindow:
    def __init__(self, master):
        self.master = master
        master.title("Chat Window")
        master.geometry("400x300")

        self.message_frame = tk.Frame(master)
        self.message_frame.pack(fill=tk.BOTH, expand=True)

        self.messages_text = tk.Text(self.message_frame, bg="black", fg="white")
        self.messages_text.pack(fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(master, bg="black")
        self.input_frame.pack(fill=tk.BOTH)

        self.input_entry = tk.Entry(self.input_frame, bg="black", fg="white")
        self.input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.send_button = tk.Button(self.input_frame, text="Send", bg="black", fg="white", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self):
        message = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.display_message("You: " + message)

    def display_message(self, message):
        self.messages_text.insert(tk.END, message + "\n")
        self.messages_text.see(tk.END)  # Scroll to the end of the messages

# Create an instance of the ChatWindow
root = tk.Tk()
chat_window = ChatWindow(root)

def main():
    root.mainloop()

if __name__ == "__main__":
    main()
