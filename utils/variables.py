# Import required package
import torch
import torch.optim

##################################################################
"""
Hyper-parameters that can be changed
"""
device = 'cuda' if torch.cuda.is_available() else 'cpu'

train_batch_size = 32
test_batch_size = 256
# optimizer name: SGD or Adam
optimizer_name = 'Adam'
lr = 1e-3
scheduler_name = 'MultiStepLR'
milestones = [20]
num_epochs = 30

in_channels = 3
out_channels = 4
model_name = 'resnetSS'

train_csv = 'directory_training.csv'
train_path = 'dataset/resized/UFPR-ALPR dataset/training'
validate_csv = 'directory_validation.csv'
validate_path = 'dataset/resized/UFPR-ALPR dataset/validation'
test_csv = 'directory_testing.csv'
test_path = 'dataset/resized/UFPR-ALPR dataset/testing'
