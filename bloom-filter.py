import array
from utils import HashFunctions
import os

class BloomFilter():
    def __init__(self):
        self.bit_array = array.array("B", [0]*4796875)

    # check whether the words in the list are present or not 
    def check_presence(self,word_list):
        hash_func = HashFunctions()

        for word in word_list:
            if len(word) > 0:
                # just for reference to show bits in the array
                print(self.bit_array[hash_func.md5_hash(word) % len(self.bit_array)]," ",
                    self.bit_array[hash_func.sha1_hash(word) % len(self.bit_array)]," ",
                    self.bit_array[hash_func.sha256_hash(word) % len(self.bit_array)]," ",
                    self.bit_array[hash_func.sha512_hash(word) % len(self.bit_array)]," ",
                    self.bit_array[hash_func.crc32_hash(word) % len(self.bit_array)]," ",
                    self.bit_array[hash_func.murmur_hash(word) % len(self.bit_array)]," ",
                    self.bit_array[hash_func.fnv_hash(word) % len(self.bit_array)])
                if (
                    self.bit_array[hash_func.md5_hash(word) % len(self.bit_array)] and
                    self.bit_array[hash_func.sha1_hash(word) % len(self.bit_array)] and
                    self.bit_array[hash_func.sha256_hash(word) % len(self.bit_array)] and
                    self.bit_array[hash_func.sha512_hash(word) % len(self.bit_array)] and
                    self.bit_array[hash_func.crc32_hash(word) % len(self.bit_array)] and
                    self.bit_array[hash_func.murmur_hash(word) % len(self.bit_array)] and
                    self.bit_array[hash_func.fnv_hash(word) % len(self.bit_array)]
                ):
                    print(word,": Found")
                else:
                    print(word,": Not found")


    ''' 
    creates the bloom filter from .txt file
    For example i am considering
    no. of words = 300
    probability of false positive = 1% i.e 0.01
    Hence, size of bit array (m) = 3837
    no. of hash functions(k) = ~5​
    '''
    def fill_bloom_filter(self):
        with open("words2.txt", "r") as f:
            hash_func = HashFunctions()
            try:
                print("Creating Bin File...")
                for line in f:
                    word = line.strip()
                    self.bit_array[hash_func.md5_hash(word)% len(self.bit_array)] |= 1
                    self.bit_array[hash_func.sha1_hash(word)% len(self.bit_array)] |= 1
                    self.bit_array[hash_func.sha256_hash(word)% len(self.bit_array)] |= 1
                    self.bit_array[hash_func.sha512_hash(word)% len(self.bit_array)] |= 1
                    self.bit_array[hash_func.crc32_hash(word)% len(self.bit_array)] |= 1
                    self.bit_array[hash_func.murmur_hash(word)% len(self.bit_array)] |= 1
                    self.bit_array[hash_func.fnv_hash(word)% len(self.bit_array)] |= 1

                # write to bin file
                script_dir = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(script_dir, "bloom_filter.bin")

                with open(file_path, 'wb') as f:
                    self.bit_array.tofile(f)

                print("Created")
                words_file_size = os.path.getsize("words2.txt")
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
    # uncomment when new words are added
    bf.fill_bloom_filter()
    print('''Commands :
    1.  check word1 word2''')

    user_input_words = input("Enter command: ")
    user_input_words = user_input_words.replace("check","").split(" ")
    bf.check_presence(user_input_words[1:])

    