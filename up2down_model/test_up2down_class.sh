PROBLEM=translate_up2down
MODEL=transformer
HPARAMS_SET=transformer_small

HOME_DIR=$(cd `dirname $0`; pwd)
CODE_DIR=$HOME_DIR/tensor2tensor-1.2.9
DATA_DIR=$HOME_DIR/data

USR_LIB_DIR=$HOME_DIR/usr_dir

#mosesdecoder=${HOME_DIR}/mosesdecoder

TRAIN_DIR=${HOME_DIR}/model
TEST_DIR=$HOME_DIR/test
LOG_DIR=$HOME_DIR/log
export PYTHONPATH=$CODE_DIR:$PYTHONPATH

mkdir -p $TEST_DIR $LOG_DIR

BEAM_SIZE=4
ALPHA=0.6
BATCH_SIZE=32

START_POINT=1
TEST_RESULT_DIR=$TEST_DIR/200000-BEAM4-ALPHA0.6

i=200000
rm -rf $TEST_RESULT_DIR
        mkdir -p $TEST_RESULT_DIR
        cp $TRAIN_DIR/model.ckpt-${i}.* $TEST_RESULT_DIR
        touch $TEST_RESULT_DIR/checkpoint
        echo model_checkpoint_path: \"model.ckpt-${i}\" >> $TEST_RESULT_DIR/checkpoint
        echo all_model_checkpoint_paths: \"model.ckpt-${i}\" >> $TEST_RESULT_DIR/checkpoint




        python $CODE_DIR/tensor2tensor/bin/test.py \
          --t2t_usr_dir=$USR_LIB_DIR \
          --data_dir=$DATA_DIR \
          --problems=$PROBLEM \
          --model=$MODEL \
          --hparams_set=$HPARAMS_SET \
          --hparams="batch_size=1024" \
          --output_dir=$TEST_RESULT_DIR \
          --decode_hparams="beam_size=$BEAM_SIZE,alpha=$ALPHA,batch_size=$BATCH_SIZE" \
          --worker_gpu=1 \
          --decode_from_file="lycc"
