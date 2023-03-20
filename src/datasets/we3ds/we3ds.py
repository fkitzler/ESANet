# -*- coding: utf-8 -*-
"""
.. codeauthor:: Florian Kitzler <florian.kitzler@boku.ac.at>
"""

import os


class WE3DSBase:
    SPLITS = ['train', 'test']
    SPLIT_FILELIST_FILENAMES = {SPLITS[0]: 'train.txt', SPLITS[1]: 'test.txt'}
    SPLIT_DIRS = {SPLITS[0]: 'train', SPLITS[1]: 'test'}

    DEPTH_DIR_SRC = "depth_refined"
    DEPTH_RAW_DIR_SRC = "depth"
    RGB_DIR_SRC = "images"
    LABELS_DIR_FMT_SRC = os.path.join("annotations", "segmentation", "SegmentationLabel")

    DEPTH_DIR = 'depth'
    DEPTH_RAW_DIR = 'depth_raw'
    RGB_DIR = 'rgb'
    LABELS_DIR_FMT = 'segmentation_label'

    # number of classes without void
    N_CLASSES = 18

    CLASS_NAMES_en = ['void',
                      'soil',
                      'broad bean',
                      'corn spurry',
                      'red-root amaranth',
                      'common buckwheat',
                      'pea',
                      'red fingergrass',
                      'common wild oat',
                      'cornflower',
                      'corn cockle',
                      'corn',
                      'milk thistle',
                      'rye brome',
                      'soybean',
                      'sunflower',
                      'narrow-leaved plantain',
                      'small-flower geranium',
                      'sugar beet']

    CLASS_COLORS = [(255, 255, 255),
                    (0, 0, 0),
                    (0, 128, 0),
                    (128, 128, 0),
                    (0, 0, 128),
                    (128, 0, 128),
                    (0, 128, 128),
                    (128, 128, 128),
                    (64, 0, 0),
                    (192, 0, 0),
                    (64, 128, 0),
                    (192, 128, 0),
                    (64, 0, 128),
                    (192, 0, 128),
                    (64, 128, 128),
                    (192, 128, 128),
                    (0, 64, 0),
                    (128, 64, 0),
                    (0, 192, 0)
                    ]
