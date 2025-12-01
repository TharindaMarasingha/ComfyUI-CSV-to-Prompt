"""
@author: Tharinda Marasingha
@title: CSV to Prompt
@nickname: ThariNode
@description: A ComfyUI node to read prompts from CSV files with batch support.
"""

import os
import csv

class CSVToPrompts:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        # 1. Setup Folder Path
        current_node_folder = os.path.dirname(os.path.realpath(__file__))
        csv_directory = os.path.join(current_node_folder, "csv_files")
        
        # Create directory if it doesn't exist
        if not os.path.exists(csv_directory):
            try:
                os.makedirs(csv_directory)
            except:
                pass

        # Scan for CSV files
        files = []
        if os.path.exists(csv_directory):
            files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]
        
        if not files:
            files = ["Put_CSV_in_csv_files_folder.csv"]

        return {
            "required": {
                "csv_filename": (sorted(files), ),
                # Seed controls the row (Seed 1 = Row 1, Seed 2 = Row 2)
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_string", "negative_string")
    FUNCTION = "get_prompts"
    CATEGORY = "Custom/CSV"

    def get_prompts(self, csv_filename, seed):
        # Path Logic
        current_node_folder = os.path.dirname(os.path.realpath(__file__))
        csv_directory = os.path.join(current_node_folder, "csv_files")
        full_path = os.path.join(csv_directory, csv_filename)

        if "Put_CSV" in csv_filename:
            return ("Error", "Error")

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                
                if not rows:
                    return ("Empty CSV", "Empty CSV")

                # Use the seed to pick the row
                row_index = seed % len(rows)
                
                target_row = rows[row_index]
                
                # Fetch text
                pos = target_row.get('positive', '').strip()
                neg = target_row.get('negetive', target_row.get('negative', '')).strip()

                print(f"Batch Run: Seed {seed} -> Using CSV Row {row_index}")
                
                return (pos, neg)

        except Exception as e:
            return (f"Error: {str(e)}", "Error")

# Node Mappings
NODE_CLASS_MAPPINGS = {
    "CSVToPrompts": CSVToPrompts
}

# --- NAME CHANGED HERE ---
NODE_DISPLAY_NAME_MAPPINGS = {
    "CSVToPrompts": "CSV to Prompt"
}