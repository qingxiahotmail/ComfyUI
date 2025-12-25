import torch
import transformers

print("Python version:", torch.__version__)
print("PyTorch version:", torch.__version__)
print("Transformers version:", transformers.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA device:", torch.cuda.get_device_name(0))
    print("CUDA memory:", torch.cuda.get_device_properties(0).total_memory / 1024**3, "GB")

print("Test completed successfully!")