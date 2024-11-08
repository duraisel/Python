import tkinter as tk
from tkinter import messagebox

class StudentDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Data Collection")

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.reg_no_label = tk.Label(root, text="Registration Number:")
        self.reg_no_label.pack()
        self.reg_no_entry = tk.Entry(root)
        self.reg_no_entry.pack()

        self.dob_label = tk.Label(root, text="Date of Birth (YYYY-MM-DD):")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(root)
        self.dob_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_data)
        self.submit_button.pack()

        self.data_list = []

    def submit_data(self):
        name = self.name_entry.get()
        reg_no = self.reg_no_entry.get()
        dob = self.dob_entry.get()

        if name and reg_no and dob:
            data = {"Name": name, "Registration Number": reg_no, "Date of Birth": dob}
            self.data_list.append(data)
            self.save_data_to_file(data)
            messagebox.showinfo("Success", "Data submitted successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.reg_no_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)

    def save_data_to_file(self, data):
        with open("student_data.txt", "a") as file:
            file.write(str(data) + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDataApp(root)
    root.mainloop()