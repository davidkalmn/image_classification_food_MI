import os

# A mappa elérési útvonala, ahol a kategóriák találhatók
dataset_path = '/elérési/útvonal/a/datasethez'

# Gyűjtsd össze a mappa neveket
category_folders = [folder for folder in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, folder))]

# Kiírhatod a kapott mappa neveket
print(category_folders)
