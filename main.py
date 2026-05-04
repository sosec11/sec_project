from modules.log_analyzer.parser import read_log_file


def main():
    log_file = "data/sample_logs.log"

    lines = read_log_file(log_file)

    print("Log Analyzer started")
    print(f"Number of log lines: {len(lines)}")

    for line in lines:
        print(line.strip())


if __name__ == "__main__":
    main()