import os
import torch


PAGE_CONFIG = dict (
    page_title="ICH Detection Assistant", 
    page_icon="🧠", 
    layout="wide"
    )

MEAN_IMG = [0.22363983, 0.18190407, 0.2523437]
STD_IMG = [0.32451536, 0.2956294,  0.31335256]
ORIG_IMG_SIZE = 512

TMP_DIR = 'tmp'
MODELS_DIR = 'models'
UPLOAD_DIR = os.path.join(TMP_DIR, 'uploads')
IMG_DIR = os.path.join(TMP_DIR, 'image')
FEATURE_EXTRACTOR_PTH = os.path.join(MODELS_DIR, 'resnext101_32x8d_wsl_checkpoint.pth')
SEQ_MODEL_PTH = os.path.join(MODELS_DIR, 'lstm_gepoch0_lstmepoch11_fold6.bin')

N_CLASSES = 6

DEVICE = torch.device('cuda')
N_GPU = torch.cuda.device_count()

AUTOCROP = True
BATCH_SIZE = 8
N_BAGS = 12
SIZE = 480
LABEL_COLS = ['epidural', 'intraparenchymal', 'intraventricular', 'subarachnoid', 'subdural', 'any']

HFLIPVAL =  0.0
TRANSPOSEVAL = 0.0

LSTM_UNITS = 2048