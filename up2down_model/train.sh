HOME_DIR=$(cd `dirname $0`; pwd)

CODE_DIR=${HOME_DIR}/tensor2tensor-1.2.9
export PYTHONPATH=${CODE_DIR}:${PYTHONPATH}
binFile=${CODE_DIR}/tensor2tensor/bin

TRAIN_DIR=${HOME_DIR}/train
LOG_DIR=${HOME_DIR}/log
USR_DIR=${HOME_DIR}/usr_dir
DATA_DIR=${HOME_DIR}/data

PROBLEM=translate_up2down
MODEL=transformer
HPARAMS_SET=transformer_small

mkdir -p ${TRAIN_DIR} ${LOG_DIR}

setting=default

python ${binFile}/t2t-trainer \
--t2t_usr_dir=${USR_DIR} \
--data_dir=${DATA_DIR} \
--problems=${PROBLEM} \
--model=${MODEL} \
--hparams_set=${HPARAMS_SET} \
--output_dir=${TRAIN_DIR} \
--keep_checkpoint_max=1000 \
--worker_gpu=1 \
--train_steps=200000 \
--save_checkpoints_secs=1800 \
--schedule=train \
--worker_gpu_memory_fraction=0.95 \
--hparams="batch_size=1024" 2>&1 | tee -a ${LOG_DIR}/train_${setting}.log
