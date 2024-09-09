class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        else:
            self.__objects = {}
