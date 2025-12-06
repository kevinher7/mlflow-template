# Donwloading Data with Frameworks

When downloading datasets through frameworks

```
from torchvision import datasets

data_dir = Path("data") // pwd is the project root

train_dataset = datasets.MNIST(root=data_dir, train=True, download=True)
```

this will create a directory for the specific dataset inside the data directory

```
.
├── LICENSE
├── Makefile
├── README.md
├── data
│   ├── MNIST
│   │   └── raw
│   │       ├── t10k-images-idx3-ubyte
│   │       ├── t10k-images-idx3-ubyte.gz
│   │       ├── t10k-labels-idx1-ubyte
│   │       ├── t10k-labels-idx1-ubyte.gz
│   │       ├── train-images-idx3-ubyte
│   │       ├── train-images-idx3-ubyte.gz
│   │       ├── train-labels-idx1-ubyte
│   │       └── train-labels-idx1-ubyte.gz
│   ├── README.md
```

# Creating your own datasets

The user is encouraged to create a directory with the dataset name inside the data directory and follow the aforementioned convention

```
.
├── LICENSE
├── Makefile
├── README.md
├── data
│   ├── custom_dataset
│   │   ├── raw
│   │   └── processed
│   ├── README.md
```
