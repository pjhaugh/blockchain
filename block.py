import hashlib
import time

class Block:

    def __init__(self, index, prev_hash, data):
        self.index = index
        this.prev_hash = prev_hash
        self.timestamp = int(time.time())
        #I feel a little more comfortable from a type perspective when all the relevant values are integers
        self.data = data
        try:
            this.hash = hashlib.sha256(index + int(prev_hash, 16) + self.timestamp + hash(data))
        except TypeError as e:
            raise TypeError('Block data must be immutable and hashable') from e
            #Obviously we don't want someone to try and get blockchain confirmation on say a list
            #They could go back and change the list contents without necessarily changing the hash of said list



