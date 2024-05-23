import os
import pandas as pd

def create_dataset(labels_file, data_dir):
    labels = {}
    with open(labels_file, 'r') as f:
        for line in f:
            line = line.strip() 
            if ':' in line:  
                filename, label = line.split(':')
                labels[filename.strip()] = label.strip()

    data = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            label = labels.get(filename, 'other')
            data.append({'text': text, 'label': label})

    df = pd.DataFrame(data)
    return df

labels_file = 'C:/Users/Ана/Desktop/ДИПЛОМ/dataset/labels.txt'
data_dir = 'C:/Users/Ана/Desktop/ДИПЛОМ/dataset/code'
dataset = create_dataset(labels_file, data_dir)

dataset.to_csv('dataset.csv', index=False)

print("Датасет успешно создан!")