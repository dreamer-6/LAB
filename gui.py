import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class JobApplicationForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Job Application Form")

        # Create labels and entry fields
        self.name_label = ttk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1)

        self.email_label = ttk.Label(master, text="Email:")
        self.email_label.grid(row=1, column=0, sticky="w")
        self.email_entry = ttk.Entry(master, width=30)
        self.email_entry.grid(row=1, column=1)

        self.phone_label = ttk.Label(master, text="Phone Number:")
        self.phone_label.grid(row=2, column=0, sticky="w")
        self.phone_entry = ttk.Entry(master, width=30)
        self.phone_entry.grid(row=2, column=1)

        self.resume_label = ttk.Label(master, text="Resume:")
        self.resume_label.grid(row=3, column=0, sticky="w")
        self.resume_button = ttk.Button(master, text="Choose File", command=self.choose_resume)
        self.resume_button.grid(row=3, column=1)
        self.resume_path = ""

        self.cover_letter_label = ttk.Label(master, text="Cover Letter:")
        self.cover_letter_label.grid(row=4, column=0, sticky="w")
        self.cover_letter_button = ttk.Button(master, text="Choose File", command=self.choose_cover_letter)
        self.cover_letter_button.grid(row=4, column=1)
        self.cover_letter_path = ""

        # Create optional fields
        self.experience_label = ttk.Label(master, text="Experience (years):")
        self.experience_label.grid(row=5, column=0, sticky="w")
        self.experience_entry = ttk.Entry(master, width=10)
        self.experience_entry.grid(row=5, column=1)

        self.skills_label = ttk.Label(master, text="Skills:")
        self.skills_label.grid(row=6, column=0, sticky="w")
        self.skills_entry = ttk.Entry(master, width=30)
        self.skills_entry.grid(row=6, column=1)

        # Create submit button
        self.submit_button = ttk.Button(master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=7, column=1)

    def choose_resume(self):
        file_path = filedialog.askopenfilename(title="Choose Resume")
        if file_path:
            self.resume_path = file_path
            self.resume_label.config(text=f"Resume: {file_path}")

    def choose_cover_letter(self):
        file_path = filedialog.askopenfilename(title="Choose Cover Letter")
        if file_path:
            self.cover_letter_path = file_path
            self.cover_letter_label.config(text=f"Cover Letter: {file_path}")

    def submit_form(self):
        # Validate form data
        if not self.name_entry.get() or not self.email_entry.get() or not self.phone_entry.get() or not self.resume_path or not self.cover_letter_path:
            messagebox.showwarning("Error", "Please fill in all required fields.")
            return

        # Process form data
        print("\n--- Form submitted! ---")
        print("Name:", self.name_entry.get())
        print("Email:", self.email_entry.get())
        print("Phone:", self.phone_entry.get())
        print("Experience:", self.experience_entry.get())
        print("Skills:", self.skills_entry.get())
        print("Resume:", self.resume_path)
        print("Cover Letter:", self.cover_letter_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = JobApplicationForm(root)
    root.mainloop()