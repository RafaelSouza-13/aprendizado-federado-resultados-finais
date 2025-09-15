import h5py

file_path = "MNIST_FedAvg_test_0.h5"  # substitua pelo caminho do seu arquivo

with h5py.File(file_path, 'r') as f:
    def print_attrs(name, obj):
        print(f"Objeto: {name}")
        for key, val in obj.attrs.items():
            print(f"    Atributo: {key} = {val}")

    # Listar todos datasets e grupos
    def print_datasets(name, obj):
        if isinstance(obj, h5py.Dataset):
            print(f"Dataset: {name}, shape: {obj.shape}, dtype: {obj.dtype}")

    f.visititems(print_datasets)
