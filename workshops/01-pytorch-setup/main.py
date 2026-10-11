import torch
import numpy

# Check if PyTorch is installed and print the version
print(f"PyTorch Version: {torch.__version__}")

# Create a tensor
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])

# Perform a simple addition
result = tensor_a + tensor_b

# Print the tensors and the result
print(f"Tensor A: {tensor_a}")
print(f"Tensor B: {tensor_b}")
print(f"Result (A + B): {result}")