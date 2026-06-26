import sys
from validator import DataValidator

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    validator = DataValidator()

    print(f"Running data quality checks on: {file_path}")
    is_valid, report = validator.validate(file_path)

    print(report)

    if is_valid:
        print("Data quality checks passed.")
        sys.exit(0)
    else:
        print("Data quality checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
