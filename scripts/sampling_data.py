import random
import logging

def main(source_file, target_file, output_source_file, output_target_file, desired_sample_size):
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Read source and target sentences
    logging.info("Reading source and target files...")
    with open(source_file, "r", encoding="utf-8") as source, open(target_file, "r", encoding="utf-8") as target:
        source_lines = source.readlines()
        target_lines = target.readlines()
    
    # Ensure the number of lines in both files is the same
    assert len(source_lines) == len(target_lines), "Source and target files must have the same number of lines."
    logging.info(f"Read {len(source_lines)} lines from both files.")
    
    # Create and shuffle indices
    logging.info("Creating and shuffling indices...")
    indices = list(range(len(source_lines)))  # Create index list [0, 1, ..., N-1]
    random.shuffle(indices)  # Shuffle the index list
    
    # Select the first desired_sample_size indices from the shuffled list
    subsample_indices = indices[:desired_sample_size]
    logging.info(f"Selected {desired_sample_size} random indices.")
    
    # Write subsampled source and target data to new files
    logging.info("Writing subsampled data to new files...")
    with open(output_source_file, "w", encoding="utf-8") as output_source, open(output_target_file, "w", encoding="utf-8") as output_target:
        for idx in subsample_indices:
            output_source.write(source_lines[idx])
            output_target.write(target_lines[idx])
    
    logging.info("Subsampling complete. Subsampled data saved to %s and %s", output_source_file, output_target_file)

if __name__ == "__main__":
    source_file = "data/train.it-en.it"
    target_file = "data/train.it-en.en"
    output_source_file = "data/subsampled_train.it-en.it"
    output_target_file = "data/subsampled_train.it-en.en"
    desired_sample_size = 100000  # Desired number of sentence pairs
    
    main(source_file, target_file, output_source_file, output_target_file, desired_sample_size)
