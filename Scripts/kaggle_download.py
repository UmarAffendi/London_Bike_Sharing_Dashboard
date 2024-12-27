import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_unzip_kaggle_dataset(dataset, download_path):
    
    # Ensure the download directory exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()
    
    # Download and unzip the dataset
    print(f"Downloading dataset: {dataset}...")
    api.dataset_download_files(dataset, path=download_path, unzip=True)
    print(f"Dataset downloaded and unzipped to: {download_path}")

if __name__ == "__main__":
    # Dataset identifier from Kaggle URL
    dataset_identifier = "hmavrodiev/london-bike-sharing-dataset"
    
    # Path to download and unzip the dataset
    output_directory = "../Data_Files"
    
    # Download and unzip the dataset
    download_and_unzip_kaggle_dataset(dataset_identifier, output_directory)
