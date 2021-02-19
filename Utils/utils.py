import secrets,random
import numpy

class Utils:
    #static method to generate random hexadecimal numbers
    @staticmethod
    def rand_160():
        return random.getrandbits(160)
    
    def rand_320():
        return random.getrandbits(320)
    
    def concat_hash(part1,part2,isint=1):
        if isint:
            return int(hashlib.sha1((str(isd.sid)+str(self.__XGWn)).encode('utf8')).hexdigest(),16)
        else:
            return 0