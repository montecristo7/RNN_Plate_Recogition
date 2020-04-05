# Import module and packages
import torch
from torch.utils.data import Dataset
import pandas as pd
from scipy.io import loadmat

import os
import os.path
from utils.variables import *

# Dataloader class
class LicenseLandmarksDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.landmarks_frame = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.landmarks_frame)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        img_name = self.root_dir+self.landmarks_frame.iloc[idx, 2]
        print(self.landmarks_frame.iloc[idx, 2])
        image = io.imread(img_name)
        landmarks = self.landmarks_frame.iloc[idx, 10]
        landmarks= landmarks.strip("][").replace("'",'')\
        .replace('"','').split(', ')
        landmarks = np.array(landmarks)
        landmarks = landmarks.astype('float')
        sample = {'image': image, 'landmarks': landmarks}

        if self.transform:
            sample = self.transform(sample)

        return sample
