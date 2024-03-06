import os

dataset_path = 'C:/Users/mauzi/.fastai/data/food-101/images'

category_folders = [folder for folder in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, folder))]

print(category_folders)
