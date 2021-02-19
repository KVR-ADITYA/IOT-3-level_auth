import os, sys, pickle, hashlib
from Utils.utils import Utils


class Gateway:
    def __init__(self):
        self.__XGWn = Utils.rand_160()
        print("XGWn: " + str(self.__XGWn))
        a = {"key": 23}
        pickle.dump(a, open("./GatewayData/isd_data.pickle", "wb"))
        # print(self.__XGWn.bit_length())

    def deployISD(self, isd):
        isd_dict = pickle.load(open("./GatewayData/isd_data.pickle", "rb"))

        # First check if it is already deployed if not deploy
        if isd.sid not in isd_dict.keys():
            SKey = int(
                hashlib.sha1(
                    (str(isd.sid) + str(self.__XGWn)).encode("utf8")
                ).hexdigest(),
                16,
            )
            Key = SKey ^ self.__XGWn
            print(f"Skey = {SKey}")
            print(f"Key = {Key}")
            # print(f"SKey = {Key^self.__XGWn}")
            isd.store(SKey)
            isd_dict[isd.sid] = Key
            f = open("./GatewayData/isd_data.pickle", "r+")
            f.truncate(0)
            f.close()
            pickle.dump(isd_dict, open("./GatewayData/isd_data.pickle", "wb"))
            return 1
        return 0

    def registerUser():
        pass

    def loginUser():
        pass
