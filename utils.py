import hashlib 
import zlib
import mmh3

class HashFunctions():
    def md5_hash(self,element):
        return int(hashlib.md5(element.encode()).hexdigest(), 16)
    def sha1_hash(self,element):
        return int(hashlib.sha1(element.encode()).hexdigest(), 16)
    def sha256_hash(self,element):
        return int(hashlib.sha256(element.encode()).hexdigest(), 16)
    def sha512_hash(self,element):
        return int(hashlib.sha512(element.encode()).hexdigest(), 16)
    def crc32_hash(self,element):
        return zlib.crc32(element.encode())
    def murmur_hash(self,element):
        return mmh3.hash(element)
    def fnv_hash(self,element):
        fnv_prime = 16777619
        hash_value = 2166136261
        for byte in element.encode():
            hash_value = (hash_value ^ byte) * fnv_prime
        return hash_value