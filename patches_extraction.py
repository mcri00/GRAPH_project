import subprocess
import os

def extract_patches(input_dir, output_dir):
    subprocess.run([
        "python", "extract_patches.py",
        f"--input_dir={input_dir}",
        f"--output_dir={output_dir}"
    ])

def run_wsi_processing(input_dir, output_dir, cache_path, mask_dir, proc_mag, ambiguous_size, chunk_shape, tile_shape, save_thumb, save_mask):
    subprocess.run([
        "./run_wsi.sh",
        f"--input_dir={input_dir}",
        f"--output_dir={output_dir}",
        f"--cache_path={cache_path}",
        f"--mask_dir={mask_dir}",
        f"--proc_mag={proc_mag}",
        f"--ambiguous_size={ambiguous_size}",
        f"--chunk_shape={chunk_shape}",
        f"--tile_shape={tile_shape}",
        f"--save_thumb={save_thumb}",
        f"--save_mask={save_mask}"
    ])

def main():
    # Imposta i percorsi corretti
    data_directory = "/percorso/dei/tuoi/dati"
    input_directory_wsi = "/percorso/dei/tuoi/dati/WSIs"  # sostituisci con il percorso corretto
    output_directory_wsi = "/percorso/di/output/wsi"  # sostituisci con il percorso desiderato
    cache_path_wsi = "/percorso/di/cache/wsi"  # sostituisci con il percorso desiderato
    mask_directory_wsi = "/percorso/dei/tuoi/dati/WSIs/masks"  # sostituisci con il percorso corretto
    proc_mag_wsi = 40
    ambiguous_size_wsi = 128
    chunk_shape_wsi = 10000
    tile_shape_wsi = 2048
    save_thumb_wsi = False
    save_mask_wsi = False

    # Estrai le patches
    extract_patches(data_directory, "/percorso/di/output/patches")  # sostituisci con il percorso desiderato

    # Esegui l'inferenza su WSIs
    run_wsi_processing(
        input_directory_wsi, output_directory_wsi, cache_path_wsi, mask_directory_wsi,
        proc_mag_wsi, ambiguous_size_wsi, chunk_shape_wsi, tile_shape_wsi,
        save_thumb_wsi, save_mask_wsi
    )

if __name__ == "__main__":
    main()
