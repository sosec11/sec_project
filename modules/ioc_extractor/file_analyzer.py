from .ioc_extractor import extract_iocs


def analyze_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    return extract_iocs(content)