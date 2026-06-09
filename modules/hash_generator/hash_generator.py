import hashlib


def generate_hashes(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    return md5_hash, sha256_hash