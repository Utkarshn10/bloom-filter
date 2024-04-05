import array
from utils import HashFunctions
import os

class BloomFilter():
    # def __init__():
    # check whether the words in the list are present or not 
    def check_presence(word_list):
        print("Found")
        print("Not Found")



    ''' 
    creates the bloom filter from .txt file
    For example i am considering
    no. of words = 300
    probability of false positive = 1% i.e 0.01
    Hence, size of bit array (m) = 3837
    no. of hash functions(k) = ~5​
    '''
    def fill_bloom_filter(self):
        f = open("words.txt","r")
        bit_array = array.array("B", [0]*3837)
        hash_func = HashFunctions
        try:
            for word in f.readline():
                bit_array[hash_func.md5_hash(word)% len(bit_array)] |= 1
                bit_array[hash_func.sha1_hash(word)% len(bit_array)] |= 1
                bit_array[hash_func.sha256_hash(word)% len(bit_array)] |= 1
                bit_array[hash_func.sha512_hash(word)% len(bit_array)] |= 1
                bit_array[hash_func.crc32_hash(word)% len(bit_array)] |= 1

            # write to bin file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "bloom_filter.bin")

            with open(file_path, 'wb') as f:
                bit_array.tofile(f)

            print("Created")
            words_file_size = os.path.getsize("words.txt")
            bin_file_size = os.path.getsize("bloom_filter.bin")
            print('''Some stats for nerds
            Disk Usage
            txt File: {}
            bin File: {}
            '''.format(words_file_size, bin_file_size)),
        except Exception as e:
            print("Some error occurred ",e)
    

if __name__ == "__main__":
    bf = BloomFilter()
    bf.fill_bloom_filter()
    print('''Commands :
    1.  check word1 word2
    ''')
    

    