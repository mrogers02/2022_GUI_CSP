# p227_starter_one_button_shell.py
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command():
    subprocess.call("ping localhost")


# Modify the do_command function:
#   to use the new button as needed
def do_command(command):
    global command_textbox

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ::1', stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# set up button to run the do_command function


ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"))
ping_btn.pack()
ping_btn = tk.Button(frame, text="Click to run nslookup", command=lambda:do_command("nslookup"))
ping_btn.pack()
ping_btn = tk.Button(frame, text="Click to run tracert", command=lambda:do_command("tracert"))
ping_btn.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ",
    compound="center",
    font=("comic sans", 14),
    bd=0,
    relief=tk.FLAT,
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()
frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

save_btn = tk.Button(frame, text="Click to save", command=lambda:do_command("msave"))
save_btn.pack()

root.mainloop()