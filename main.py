# https://github.com/muodosta

import os
import sys

from tqdm import tqdm


def split_file(file_path, separator, output_dir) -> int:
    with open(file_path, 'rb') as file:
        content = file.read()

    parts = content.split(separator)

    base_name = os.path.basename(file_path)
    base_name_without_ext = os.path.splitext(base_name)[0]

    for index, part in enumerate(parts):
        
        if len(part) == 0:
            continue
        
        part_file_name = f"{base_name_without_ext}_{index + 1}.lb"
        part_file_path = os.path.join(output_dir, part_file_name)
        
        with open(part_file_path, 'wb') as part_file:
            # Включаем разделитель в каждую часть, кроме первой
            if index > 0:
                part_file.write(separator)
            part_file.write(part)
            
    return len(parts)

def process_directory(directory_path):
    separator = bytes.fromhex('55 6e 69 74 79 46 53')
    output_dir = os.path.join(directory_path, 'split_files')
    os.makedirs(output_dir, exist_ok=True)

    files = []
    
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.lb'):
            file_path = os.path.join(directory_path, file_name)
            files.append((file_path, separator, output_dir))
    
    splited_files_count = 0
    
    for file in tqdm(files):
        splited_files_count += split_file(*file)
        
    print(f'Success, {len(files)} files divided to {splited_files_count:,}')
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv[1])
        process_directory(sys.argv[1])
    else:
        print('Directory not specified')
