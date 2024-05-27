#!/bin/bash

mkdir -p data/train_bpe_3000

TRAIN_SRC="data/subsampled_train.it-en.it"
TRAIN_TRG="data/subsampled_train.it-en.en"
CODES_FILE="data/train_bpe_3000/codes3000.bpe"
MERGED_TRAIN_FILE="data/train_bpe_3000/subsampled_train.it-en"
MERGED_VOCAB_FILE="data/train_bpe_3000/merged_vocab.txt"
NUM_SYMBOLS=3000  

cat $TRAIN_SRC $TRAIN_TRG > $MERGED_TRAIN_FILE

# Learn BPE codes and vocabulary
subword-nmt learn-joint-bpe-and-vocab --input $MERGED_TRAIN_FILE --output $CODES_FILE --write-vocabulary $MERGED_VOCAB_FILE --symbols $NUM_SYMBOLS

# Apply BPE to train, dev, and test sets
for SPLIT in subsampled_train dev test; do
    subword-nmt apply-bpe --codes $CODES_FILE --vocabulary $MERGED_VOCAB_FILE --vocabulary-threshold 50 < data/${SPLIT}.it-en.it > data/train_bpe_3000/${SPLIT}.it-en.it
    subword-nmt apply-bpe --codes $CODES_FILE --vocabulary $MERGED_VOCAB_FILE --vocabulary-threshold 50 < data/${SPLIT}.it-en.en > data/train_bpe_3000/${SPLIT}.it-en.en
done

# Remove frequency and whitespace from vocabulary
sed -i '' 's/[[:space:]]*[0-9]*$//' $MERGED_VOCAB_FILE


echo "BPE processing completed."
