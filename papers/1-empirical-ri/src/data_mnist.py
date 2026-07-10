"""data_mnist.py — MNIST loader without torchvision.

INSTRUCTIONS.md §1 step 1 specifies torchvision.datasets.MNIST purely to obtain
X (N,28,28 in [0,1]) and Z (N,) labels over the full 70k set (train+test
concatenated). We download the raw idx.gz files directly from the standard
PyTorch mirror and parse them with numpy — identical bytes, no torch dependency.
"""
import os, gzip, struct, urllib.request
import numpy as np

MIRRORS = [
    "https://ossci-datasets.s3.amazonaws.com/mnist/",
    "https://storage.googleapis.com/cvdf-datasets/mnist/",
]
FILES = {
    "train_images": "train-images-idx3-ubyte.gz",
    "train_labels": "train-labels-idx1-ubyte.gz",
    "test_images":  "t10k-images-idx3-ubyte.gz",
    "test_labels":  "t10k-labels-idx1-ubyte.gz",
}


def _download(fname, dest):
    last = None
    for m in MIRRORS:
        try:
            url = m + fname
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
                f.write(r.read())
            return
        except Exception as e:  # try next mirror
            last = e
    raise RuntimeError(f"could not download {fname}: {last}")


def _read_idx(path):
    with gzip.open(path, "rb") as f:
        magic, = struct.unpack(">I", f.read(4))
        ndim = magic & 0xFF
        dims = struct.unpack(">" + "I" * ndim, f.read(4 * ndim))
        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data.reshape(dims)


def load_mnist(root="data"):
    """Returns X (70000,28,28) float in [0,1] and Z (70000,) int labels."""
    os.makedirs(root, exist_ok=True)
    paths = {}
    for key, fname in FILES.items():
        dest = os.path.join(root, fname)
        if not os.path.exists(dest):
            _download(fname, dest)
        paths[key] = dest
    tr_x = _read_idx(paths["train_images"])
    tr_y = _read_idx(paths["train_labels"])
    te_x = _read_idx(paths["test_images"])
    te_y = _read_idx(paths["test_labels"])
    X = np.concatenate([tr_x, te_x]).astype(np.float64) / 255.0
    Z = np.concatenate([tr_y, te_y]).astype(np.int64)
    return X, Z


if __name__ == "__main__":
    X, Z = load_mnist()
    print("X", X.shape, "Z", Z.shape, "labels", sorted(set(Z.tolist())))
    print("per-class counts:", np.bincount(Z).tolist())
