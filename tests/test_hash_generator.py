from modules.hash_generator.hash_generator import generate_hashes

md5_hash, sha256_hash = generate_hashes("hello")

assert md5_hash == "5d41402abc4b2a76b9719d911017c592"

assert sha256_hash == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

print("Hash test passed")