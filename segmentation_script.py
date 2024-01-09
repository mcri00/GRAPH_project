import subprocess

# PATH scripts
'''convert_script = "./hover_net/convert_chkpt_tf2pytorch.py"
format_script = "./hover_net/convert_format.py"'''
infer_script = "./hover_net/run_infer.py"

# PATH files
type_info_path = "type_info.json"
model_path = "./hover_net/HN_weights/hovernet_original_consep_notype_tf2pytorch.tar"
input_dir = "./resized_images/" #tiles are all in a directory (no nested folders)
output_dir = "./segmented_images_with_consep/" #name to be changed depending on the model weights used

'''# Step 1: Converti il checkpoint del modello
subprocess.run(["python", convert_script])''' #sembra non servire perché li ho già convertiti

'''# Step 2: Converti il formato dell'output
subprocess.run(["python", format_script])''' #sembra non servire perchè ho già il formato giusto

# Inference
subprocess.run([
    "python", infer_script,
    "--gpu='0'", #check with nvidia-smi (gpu with usage percentage>0%)
    "--nr_types=0", #I'm using a model only for segmentation
    f"--type_info_path={type_info_path}",
    "--batch_size=128",
    "--model_mode=original", #because the model I'm using applied this mode
    f"--model_path={model_path}",
    "--nr_inference_workers=8",
    "--nr_post_proc_workers=16",
    "tile",
    f"--input_dir={input_dir}",
    f"--output_dir={output_dir}",
    "--mem_usage=0.1",
    "--draw_dot",
    "--save_qupath"
])
