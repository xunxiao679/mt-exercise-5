import os
import re
import json
import csv
import matplotlib.pyplot as plt

def extract_info_from_log(log_file):
    beam_size = None
    bleu_score = None
    time_taken = None
    
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        # Extract beam size
        if 'Beam search with beam_size=' in line:
            beam_size = int(re.search(r'beam_size=(\d+)', line).group(1))
        
        # Extract BLEU score
        if '"score"' in line:
            bleu_score = float(re.search(r'"score":\s*([\d\.]+)', line).group(1))
        
        # Extract time taken
        if 'seconds' in line:
            match = re.search(r'([\d\.]+)\sseconds', line)
            if match:
                time_taken = float(match.group(1))

    
    return beam_size, bleu_score, time_taken

def process_logs(log_dir, output_csv):
    results = []
    for log_file in os.listdir(log_dir):
        if log_file.endswith('.txt'):
            full_path = os.path.join(log_dir, log_file)
            beam_size, bleu_score, time_taken = extract_info_from_log(full_path)
            if beam_size is not None and bleu_score is not None and time_taken is not None:
                results.append({
                    'log_file': os.path.basename(log_file),
                    'beam_size': beam_size,
                    'bleu_score': bleu_score,
                    'time_taken': time_taken
                })
    
    # Sort results by beam_size
    sorted_results = sorted(results, key=lambda x: x['beam_size'])
    # Write results to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['log_file', 'beam_size', 'bleu_score', 'time_taken']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in sorted_results:
            writer.writerow(result)


def read_csv(file_path):
    beam_sizes = []
    bleu_scores = []
    times_taken = []
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            beam_sizes.append(int(row['beam_size']))
            bleu_scores.append(float(row['bleu_score']))
            times_taken.append(float(row['time_taken']))
    
    return beam_sizes, bleu_scores, times_taken

def plot_graphs(beam_sizes, bleu_scores, times_taken):
    # Plot beam size vs BLEU score
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(beam_sizes, bleu_scores, marker='o')
    plt.xlabel('Beam Size')
    plt.ylabel('BLEU Score')
    plt.title('Beam Size vs BLEU Score')
    plt.grid(True)
    
    # Plot beam size vs time taken
    plt.subplot(1, 2, 2)
    plt.plot(beam_sizes, times_taken, marker='o')
    plt.xlabel('Beam Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Beam Size vs Time Taken')
    plt.grid(True)
    
    # Adjust layout and show plot
    plt.tight_layout()
    plt.show()

def main():
    log_dir = 'beam_size_evaluation_bpe_3000'
    output_csv = 'beam_size_evaluation_results.csv'
    process_logs(log_dir, output_csv)
    beam_sizes, bleu_scores, times_taken = read_csv(output_csv)
    plot_graphs(beam_sizes, bleu_scores, times_taken)

if __name__ == '__main__':
    main()
