import json
import pandas as pd

# File paths
images_csv = r'c:/Users/mpbja/Downloads/abo-images-small/images/metadata/images.csv/images.csv'
balanced_jsonl = r'c:/Users/mpbja/Downloads/balanced_data.jsonl'
output_csv = r'c:/Users/mpbja/Downloads/matched_vqa.csv'

# Load images.csv
images_df = pd.read_csv(images_csv)
image_id_to_path = dict(zip(images_df['image_id'], images_df['path']))

# Prepare output rows
rows = []
with open(balanced_jsonl, 'r', encoding='utf-8') as f:
    for line in f:
        entry = json.loads(line)
        image_id = entry.get('main_image_id')
        if image_id in image_id_to_path:
            rows.append({
                'main_image_id': image_id,
                'image_path': image_id_to_path[image_id],
                'json_line': line.strip()
            })

# Write to CSV
out_df = pd.DataFrame(rows)
out_df.to_csv(output_csv, index=False)

print(f"Wrote {len(rows)} matched rows to {output_csv}")