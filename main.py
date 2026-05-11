from modules.log_analyzer.parser import read_logs
from modules.log_analyzer.detector import detect_suspicious_lines

path = input("Enter log file path: ")

logs = read_logs(path)

detect_suspicious_lines(logs)