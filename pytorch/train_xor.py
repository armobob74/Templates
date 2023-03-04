import numpy as np
import torch
import torch.nn as nn
from simple_mlp import MLP

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
targets = np.array([[0], [1], [1], [0]], dtype=np.float32)

# convert numpy arrays to PyTorch tensors
inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)

# initialize the MLP
mlp = MLP(input_size=2, hidden_size=2, num_classes=1)

# define the loss function and optimization algorithm
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(mlp.parameters(), lr=0.01)

# train the MLP
def train_model(mlp):
    num_epochs = 1000
    for epoch in range(num_epochs):
        # forward pass
        outputs = mlp(inputs)
        loss = criterion(outputs, targets)

        # backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch+1) % 100 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

train_model(mlp)

# test the trained MLP
def test_model(mlp):
    with torch.no_grad():
        outputs = mlp(inputs)
        predictions = (outputs > 0.5).float()
        correct = (predictions == targets).sum().item()
        accuracy = correct / targets.size(0)
        print(f'Accuracy: {accuracy:.2f}')

test_model(mlp)
