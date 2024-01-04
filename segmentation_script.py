import subprocess

# Esegui lo script per l'estrazione delle patch
subprocess.run(["python", "extract_patches.py"])

# Ottieni il percorso dell'output di extract_patches.py
output_dir = "dataset/training_data/consep/train/540x540_164x164/"

# Esegui lo script per l'inferenza WSI
subprocess.run([
    "python", "run_infer.py",
    "--gpu='0,1'",
    "--nr_types=6",
    "--type_info_path=type_info.json",
    "--batch_size=64",
    "--model_mode=fast",
    "--model_path=../pretrained/hovernet_fast_pannuke_type_tf2pytorch.tar",
    "--nr_inference_workers=8",
    "--nr_post_proc_workers=16",
    "wsi",
    f"--input_dir={output_dir}",
    f"--output_dir={output_dir}",
    "--save_thumb",
    "--save_mask"
])


#path per patches e maschere
#parte relativa al json file scritta sul readme del modello