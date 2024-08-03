# import json
#
# def modify_instance_name(json_file_path, old_name, new_name):
#     with open(json_file_path, 'r') as json_file:
#         data = json.load(json_file)
#
#         for shape in data['shapes']:
#             if shape['label'] == old_name:
#                 shape['label'] = new_name
#
#     with open(json_file_path, 'w') as json_file:
#         json.dump(data, json_file, indent=4)
#
# # 指定要修改的JSON文件路径、旧的实例名称和新的实例名称
# json_file_path = r'D:\dataset\test-mine\09168.json'
# old_instance_name = 'salient_mollusk'
# new_instance_name = 'salient_corals'
#
# # 调用函数修改实例名称
# modify_instance_name(json_file_path, old_instance_name, new_instance_name)

import json
import tkinter as tk
from tkinter import filedialog, messagebox

def modify_instance_name(json_file_path, old_name, new_name):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    for shape in data['shapes']:
        if shape['label'] == old_name:
            shape['label'] = new_name

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    messagebox.showinfo("Success", "Instance name modified successfully!")

def select_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def main():
    root = tk.Tk()
    root.title("Modify JSON Instance Name")

    tk.Label(root, text="JSON File Path:").grid(row=0, column=0, padx=10, pady=10)
    file_path_entry = tk.Entry(root, width=50)
    file_path_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse...", command=lambda: select_file(file_path_entry)).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(root, text="Old Name:").grid(row=1, column=0, padx=10, pady=10)
    old_name_entry = tk.Entry(root)
    old_name_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="New Name:").grid(row=2, column=0, padx=10, pady=10)
    new_name_entry = tk.Entry(root)
    new_name_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(root, text="Modify", command=lambda: modify_instance_name(file_path_entry.get(), old_name_entry.get(), new_name_entry.get())).grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
