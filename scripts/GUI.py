import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import subprocess
import os

# Function to run a script
def run_script(script):
    if script:
        script_path = f"./{script}"
        subprocess.run(["bash", script_path], check=True)
        result_label.config(text=f"Executed {script} successfully!")
    else:
        result_label.config(text="Please select a script.")

# Main application window setup
app = tk.Tk()
app.title("Script Runner GUI")

# Custom font for the widgets
custom_font = Font(family="Helvetica", size=16)

# Define a style for label frames
style = ttk.Style(app)
style.configure("TLabelframe.Label", font=custom_font, anchor='center')
style.configure('TButton', font=custom_font, anchor='center', justify='center')
style.configure('TCombobox', font=custom_font)

# Label to display results
result_label = tk.Label(app, text="Select a script and run it.", font=custom_font, anchor='center')
result_label.grid(column=0, row=4, padx=10, pady=10, sticky='ew')

# Function to create buttons for scripts in a given frame
def create_script_buttons(frame, scripts, font):
    for i, script in enumerate(scripts):
        button = tk.Button(frame, text=script, command=lambda s=script: run_script(s), font=font, anchor='center', justify='center')
        button.grid(column=0, row=i, padx=10, pady=10, sticky='ew')

# Frame for each script group with labels
group_frames = {
    "SRC": ["2_extract_image_from_data_src.sh", "4_data_src_extract_faces_S3FD.sh", "5_XSeg_generic_wf_data_src_apply.sh"],
    "DST": ["3_extract_image_from_data_dst.sh", "5_data_dst_extract_faces_S3FD.sh", "5_XSeg_generic_wf_data_dst_apply.sh"],
    "TRAIN": ["6_train_SAEHD.sh"],
    "MERGE": ["7_merge_SAEHD.sh", "8_merged_to_mp4.sh"]
}

# Creating frames and buttons for each group
row_index = 0
for group_name, scripts in group_frames.items():
    frame = ttk.LabelFrame(app, text=group_name, style="TLabelframe")
    frame.grid(column=0, row=row_index, padx=10, pady=5, sticky='ew')
    create_script_buttons(frame, scripts, custom_font)
    row_index += 1

# List of all scripts for dropdown
all_scripts = [
    '1_clear_workspace.sh',
    '2_extract_image_from_data_src.sh',
    '3.1_denoise_data_dst_images.sh',
    '3_extract_image_from_data_dst.sh',
    '4.1_download_CelebA.sh',
    '4.1_download_FFHQ.sh',
    '4.1_download_Quick96.sh',
    '4.1_download_XSeg_generic.sh',
    '4.2_data_src_sort.sh',
    '4.2_data_src_util_add_landmarks_debug_images.sh',
    '4.2_data_src_util_faceset_enhance.sh',
    '4.2_data_src_util_faceset_metadata_restore.sh',
    '4.2_data_src_util_faceset_metadata_save.sh',
    '4.2_data_src_util_faceset_pack.sh',
    '4.2_data_src_util_faceset_unpack.sh',
    '4.2_data_src_util_recover_original_filename.sh',
    '4_data_src_extract_faces_MANUAL.sh',
    '4_data_src_extract_faces_S3FD.sh',
    '5.2_data_dst_sort.sh',
    '5.2_data_dst_util_faceset_pack.sh',
    '5.2_data_dst_util_faceset_unpack.sh',
    '5.2_data_dst_util_recover_original_filename.sh',
    '5_data_dst_extract_faces_MANUAL.sh',
    '5_data_dst_extract_faces_MANUAL_RE-EXTRACT_DELETED_ALIGNED_DEBUG.sh',
    '5_data_dst_extract_faces_S3FD.sh',
    '5_data_dst_extract_faces_S3FD_+_manual_fix.sh',
    '5_XSeg_data_dst_mask_apply.sh',
    '5_XSeg_data_dst_mask_edit.sh',
    '5_XSeg_data_dst_mask_fetch.sh',
    '5_XSeg_data_dst_mask_remove.sh',
    '5_XSeg_data_dst_trained_mask_remove.sh',
    '5_XSeg_data_src_mask_apply.sh',
    '5_XSeg_data_src_mask_edit.sh',
    '5_XSeg_data_src_mask_fetch.sh',
    '5_XSeg_data_src_mask_remove.sh',
    '5_XSeg_data_src_trained_mask_remove.sh',
    '5_XSeg_generic_wf_data_dst_apply.sh',
    '5_XSeg_generic_wf_data_src_apply.sh',
    '5_XSeg_train.sh',
    '6_export_AMP_as_dfm.sh',
    '6_export_SAEHD_as_dfm.sh',
    '6_train_Quick96.sh',
    '6_train_Quick96_no_preview.sh',
    '6_train_SAEHD.sh',
    '6_train_SAEHD_no_preview.sh',
    '7_merge_Quick96.sh',
    '7_merge_SAEHD.sh',
    '8_merged_to_avi.sh',
    '8_merged_to_mov_lossless.sh',
    '8_merged_to_mp4.sh',
    '8_merged_to_mp4_lossless.sh'
]

# Combobox for selecting any script
script_combobox = ttk.Combobox(app, values=all_scripts, font=custom_font, state='readonly')
script_combobox.grid(column=0, row=5, padx=10, pady=10, sticky='ew')

# Button to execute the selected script
execute_button = tk.Button(app, text="Execute Script", command=lambda: run_script(script_combobox.get()), font=custom_font)
execute_button.grid(column=0, row=6, padx=10, pady=10, sticky='ew')

# Bind ESC to close the app
app.bind('<Escape>', lambda event: app.destroy())

# Start the application
app.mainloop()
