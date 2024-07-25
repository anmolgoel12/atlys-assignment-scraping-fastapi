import os

ROOT_DIrectory = "../"


class FileStorage:
    path = None

    def __init__(self, path):
        if not os.path.exists(os.path.join(ROOT_DIrectory, path)):
            os.mkdir(os.path.join(ROOT_DIrectory, path))
        self.path = os.path.join(ROOT_DIrectory, path)
