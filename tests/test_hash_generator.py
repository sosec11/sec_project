from modules.hash_generator.hash_generator import generate_hashes

md5_hash, sha256_hash = generate_hashes("hello")

assert md5_hash == "5d41402abc4b2a76b9719d911017c592"

print("Hash test passed")