import tkinter as tk
from tkinter import ttk
def submit_form():
   # Retrieve values from the form
   first_name = entry_first_name.get()
   last_name = entry_last_name.get()
   email = entry_email.get()
   contact_number = entry_contact_number.get()
   password = entry_password.get()
   gender = gender_var.get()


   # Display the submitted information in blue color
   result_label.config(text=f"Registration Form Successfully Created!\n"
                             f"First Name: {first_name}\n"
                             f"Last Name: {last_name}\n"
                             f"Email: {email}\n"
                             f"Contact Number: {contact_number}\n"
                             f"Password: {password}\n"
                             f"Gender: {gender}", foreground="blue")
root = tk.Tk()
root.title("Flood-Registration Form")
root.geometry("400x400")
root.configure(bg="lightgreen")
label_first_name = ttk.Label(root, text="First Name:", foreground="purple")
label_last_name = ttk.Label(root, text="Last Name:", foreground="purple")
label_email = ttk.Label(root, text="Email:", foreground="purple")
label_contact_number = ttk.Label(root, text="Contact Number:", foreground="purple")
label_password = ttk.Label(root, text="Password:", foreground="purple")
label_gender = ttk.Label(root, text="Gender:", foreground="purple")


# Create entry widgets
entry_first_name = ttk.Entry(root)
entry_last_name = ttk.Entry(root)
entry_email = ttk.Entry(root)
entry_contact_number = ttk.Entry(root)
entry_password = ttk.Entry(root, show="*")
# Create a Combobox for gender
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], state="readonly")
gender_combobox.set("Male")  # Default value
# Create submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form, style="TButton")
# Create label for displaying the result
result_label = ttk.Label(root, text="", foreground="blue")
label_first_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky="w")
label_contact_number.grid(row=3, column=0, padx=10, pady=5, sticky="w")
label_password.grid(row=4, column=0, padx=10, pady=5, sticky="w")
label_gender.grid(row=5, column=0, padx=10, pady=5, sticky="w")


entry_first_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_last_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_email.grid(row=2, column=1, padx=10, pady=5, sticky="w")
entry_contact_number.grid(row=3, column=1, padx=10, pady=5, sticky="w")
entry_password.grid(row=4, column=1, padx=10, pady=5, sticky="w")
gender_combobox.grid(row=5, column=1, padx=10, pady=5, sticky="w")


submit_button.grid(row=6, column=0, columnspan=2, pady=10)
result_label.grid(row=7, column=0, columnspan=2, pady=10)
# Configure style for the submit button
style = ttk.Style()
style.configure("TButton", foreground="red")
# Run the Tkinter main loop
root.mainloop()
