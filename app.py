import argparse

def main():
    parser = argparse.ArgumentParser(description='Marine Life Classifier')
    parser.add_argument('--mode', type=str, required=True, help='Mode to run the script in (train/test)')
    parser.add_argument('--model', type=str, required=True, help='Model name')
    parser.add_argument('--data_path', type=str, required=True, help='Path to the training data')
    parser.add_argument('--input_type', type=str, required=True, help='Type of input (e.g., dual)')
    parser.add_argument('--input_source', type=str, required=True, help='Source of input data')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs for training')

    args = parser.parse_args()
    print(f"Running in {args.mode} mode with model {args.model}")

if __name__ == "__main__":
    main()
