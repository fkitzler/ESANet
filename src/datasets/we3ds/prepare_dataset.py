# -*- coding: utf-8 -*-
"""
.. codeauthor:: Florian Kitzler <florian.kitzler@boku.ac.at>
"""
import argparse as ap
import os
import numpy as np
import shutil
from tqdm import tqdm
import urllib.request
from zipfile import ZipFile

from we3ds import WE3DSBase

DATASET_URL = "https://zenodo.org/record/7457983/files/WE3DS.zip?download=1"


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_file(url, output_filepath, display_progressbar=False):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1],
                             disable=not display_progressbar) as t:
        urllib.request.urlretrieve(url,
                                   filename=output_filepath,
                                   reporthook=t.update_to)


if __name__ == '__main__':
    # argument parser
    parser = ap.ArgumentParser(
        description='Prepare WE3DS dataset for segmentation.')
    parser.add_argument('output_path', type=str,
                        help='path where to store dataset')
    parser.add_argument('source_path', type=str,
                        help='directory where the dataset is stored')
    args = parser.parse_args()

    # preprocess args and expand user
    output_path = os.path.expanduser(args.output_path)

    # create output path if not exist
    os.makedirs(output_path, exist_ok=True)

    # preprocess args and expand user
    source_path = os.path.expanduser(args.source_path)

    # create source path if not exist
    os.makedirs(source_path, exist_ok=True)

    we3ds_dir = os.path.join(source_path, 'WE3DS')

    # download and extract data
    if not os.path.exists(we3ds_dir):
        zip_file_path = os.path.join(source_path, 'WE3DS.zip')
#        download_file(DATASET_URL, zip_file_path,
#                      display_progressbar=True)
        with ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(zip_file_path))
        os.remove(zip_file_path)

    # get number of files
    f_names = [f for f in os.listdir(os.path.join(source_path, "images")) if ".png" in f]
    np.random.seed(42)
    train_test_split = 0.6
    perm_idx = np.random.permutation(len(f_names))
    train_idxs = perm_idx[:int(train_test_split * len(f_names))]
    test_idxs = perm_idx[int(train_test_split * len(f_names)):]

    # save images
    for set_ in ['train', 'test']:
        os.makedirs(os.path.join(output_path, set_), exist_ok=True)
        os.makedirs(os.path.join(output_path, set_, WE3DSBase.RGB_DIR), exist_ok=True)
        os.makedirs(os.path.join(output_path, set_, WE3DSBase.DEPTH_DIR), exist_ok=True)
        os.makedirs(os.path.join(output_path, set_, WE3DSBase.DEPTH_RAW_DIR), exist_ok=True)
        os.makedirs(os.path.join(output_path, set_, WE3DSBase.LABELS_DIR_FMT), exist_ok=True)

    for idx in train_idxs:
        src_path = os.path.join(source_path, WE3DSBase.RGB_DIR_SRC, 'img_' + str(idx).zfill(5) + ".png")
        dst_path = os.path.join(output_path, "train", WE3DSBase.RGB_DIR, str(idx).zfill(5) + ".png")
        shutil.copy(src_path, dst_path)
        src_path = os.path.join(source_path, WE3DSBase.DEPTH_DIR_SRC, 'img_' + str(idx).zfill(5) + ".png")
        dst_path = os.path.join(output_path, "train", WE3DSBase.DEPTH_DIR, str(idx).zfill(5) + ".png")
        shutil.copy(src_path, dst_path)
        src_path = os.path.join(source_path, WE3DSBase.DEPTH_RAW_DIR_SRC, 'img_' + str(idx).zfill(5) + ".png")
        dst_path = os.path.join(output_path, "train", WE3DSBase.DEPTH_RAW_DIR, str(idx).zfill(5) + ".png")
        shutil.copy(src_path, dst_path)
        src_path = os.path.join(source_path, WE3DSBase.LABELS_DIR_FMT_SRC, 'img_' + str(idx).zfill(5) + ".png")
        dst_path = os.path.join(output_path, "train", WE3DSBase.LABELS_DIR_FMT, str(idx).zfill(5) + ".png")
        shutil.copy(src_path, dst_path)

    for idx in test_idxs:
        src_path = os.path.join(source_path, WE3DSBase.RGB_DIR_SRC, 'img_' + str(idx).zfill(5) + ".png")
        dst_path = os.path.join(output_path, "test", WE3DSBase.RGB_DIR, str(idx).zfill(5) + ".png")
        shutil.copy(src_path, dst_path)
        src_path = os.path.join(source_path, WE3DSBase.DEPTH_DIR_SRC, 'img_' + str(idx).zfill(5) + ".png")
        dst_path = os.path.join(output_path, "test", WE3DSBase.DEPTH_DIR, str(idx).zfill(5) + ".png")
        shutil.copy(src_path, dst_path)
        src_path = os.path.join(source_path, WE3DSBase.DEPTH_RAW_DIR_SRC, 'img_' + str(idx).zfill(5) + ".png")
        dst_path = os.path.join(output_path, "test", WE3DSBase.DEPTH_RAW_DIR, str(idx).zfill(5) + ".png")
        shutil.copy(src_path, dst_path)
        src_path = os.path.join(source_path, WE3DSBase.LABELS_DIR_FMT_SRC, 'img_' + str(idx).zfill(5) + ".png")
        dst_path = os.path.join(output_path, "test", WE3DSBase.LABELS_DIR_FMT, str(idx).zfill(5) + ".png")
        shutil.copy(src_path, dst_path)

    # save meta files
    print("Writing meta files")
    np.savetxt(os.path.join(output_path, 'class_names.txt'),
               WE3DSBase.CLASS_NAMES_en,
               delimiter=',', fmt='%s')
    np.savetxt(os.path.join(output_path, 'class_colors.txt'),
               WE3DSBase.CLASS_COLORS,
               delimiter=',', fmt='%s')
    # splits
    np.savetxt(os.path.join(output_path,
                            WE3DSBase.SPLIT_FILELIST_FILENAMES['train']),
               train_idxs, fmt='%05d')
    np.savetxt(os.path.join(output_path,
                            WE3DSBase.SPLIT_FILELIST_FILENAMES['test']),
               test_idxs, fmt='%05d')
