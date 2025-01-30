import os.path


CURRENT_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_PATH)
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")


print(TMP_DIR)