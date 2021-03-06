DATASET="MELD"
NUM_CLASSES=7
SEEDS=0,1,2,3,4
NUM_UTT=2
WORKERS=60

TOTAL_NUM_UPDATES=1600                    # one epoch is around 160 updates for MELD, when MAX_SENTENCES=8 and UPDATE_FREQ=4
WARMUP_UPDATES=320                        # 20 percent of the number of updates
LR=1e-05                                  # Peak LR for polynomial LR scheduler.
MAX_SENTENCES=8                           # Batch size.
ROBERTA_SIZE=roberta_base
ROBERTA_PATH=models/roberta.base/model.pt # pre-trained roberta-base TODO: use roberta-large
PATIENCE=10                               # early stopping in number of training epochs
GPU_IDS=0,1
MAX_EPOCH=10
UPDATE_FREQ=4
SAVE_INTERVAL=1
WEIGHT_DECAY=0.1
DROP_OUT=0.1
ATTENTION_DROP_OUT=0.1
MAX_TOKENS=4400
MAX_POSITIONS=512
