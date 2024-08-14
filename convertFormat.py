from utils.convert_annotations import convert
from utils.read_annotations import read_ra_labels_csv
import os

if __name__ == "__main__":
    data_dir = "./data/Automotive"
    seq_list = os.listdir(data_dir)
    seq_list.sort()
    is_true = True
    for seq in seq_list:
        path = os.path.join(data_dir, seq)
        convert(path)
        if is_true:
            is_true = False
            res = read_ra_labels_csv(path)
            print(len(res))

