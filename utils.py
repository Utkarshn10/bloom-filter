import hashlib 
import zlib
class HashFunctions():
    def md5_hash(element):
        return int(hashlib.md5(element.encode()).hexdigest(), 16)
    def sha1_hash(element):
        return int(hashlib.sha1(element.encode()).hexdigest(), 16)
    def sha256_hash(element):
        return int(hashlib.sha256(element.encode()).hexdigest(), 16)
    def sha512_hash(element):
        return int(hashlib.sha512(element.encode()).hexdigest(), 16)
    def crc32_hash(element):
        return zlib.crc32(element.encode())