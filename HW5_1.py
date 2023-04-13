class KeyValueStorage:
    def __init__(self, file_path):
        self._data = {}
        with open(file_path, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')

                if key.isidentifier():
                    value = int(value) if value.isdigit() else value
                    self._data[key] = value
                else:
                    raise ValueError(f"Invalid key: {key}")

    def __getitem__(self, key):
        return self._data[key]

    def __getattr__(self, key):
        return self._data[key]

    def __setattr__(self, key, value):
        if key == "_data":
            super().__setattr__(key, value)
        else:
            raise AttributeError("Cannot set values directly, use the file to update values")
