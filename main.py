import os
from gateway import Gateway
from Utils.utils import Utils
from user import User
from ISD import ISD

gateway = 0

def initISDs():
    isdList = []
    for i in range(1,3):
        isdList.append(ISD())
    return isdList

def deploy(isd):
    print("Deploying")
    print("ISD SID: "+isd.__str__())
    return gateway.deployISD(isd)

def register():
    print("Entering User Mode")
    User.register()
    pass

def login():
    pass

def authenticate():
    pass

if __name__ == "__main__":
    gateway = Gateway()
    isdList = initISDs()
    deploy(isdList[1])
    register()
    login()
    authenticate()