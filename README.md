# MT Exercise 5: Byte Pair Encoding, Beam Search
This repository is a starting point for the 5th and final exercise. As before, fork this repo to your own account and the clone it into your prefered directory.

## Requirements

- This only works on a Unix-like system, with bash available.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

## Steps

Clone your fork of this repository in the desired place:

    git clone https://github.com/[your-name]/mt-exercise-5

Create a new virtualenv that uses Python 3.10. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software as described in the exercise pdf.

Download data:

    ./scripts/download_iwslt_2017_data.sh
    
Before executing any further steps, you need to make the modifications described in the exercise pdf.

Take 100,000 samples from training data:
	
	sampling_data.py

Preprocessing for bpe models:
	
	./scripts/prepare_bpe.sh

Edit configs files for 3 models: 
	
	transformer_word_level_config.yaml
	transformer_bpe_2000_config.yaml
	transformer_bpe_3000_config.yaml

Modify the train.sh according to apply the modele configs files respectively: 

   eg. model_name, path_to_data, etc. 

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Evaluate a trained model with

    ./scripts/evaluate.sh
