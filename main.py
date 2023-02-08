import time
import pandas as pd
followers= []
following= []
uDontFollowBack = []
notFollowuBack = []

def data():
    followersCSV = pd.read_csv("/Users/Groot/Downloads/InstagramFollowingAndFollowers/files/followers.csv")
    followingCSV = pd.read_csv("/Users/Groot/Downloads/InstagramFollowingAndFollowers/files/following.csv")


    for each in followersCSV['userName']:
        followers.append(each)

    for each in followingCSV['userName']:
        following.append(each)
data()


def NotFollowUBack():
    for each in following:
        if(each not in followers):
            notFollowuBack.append(each)

def UDontFollowBack():
    for each in followers:
        if(each not in following):
            uDontFollowBack.append(each)

NotFollowUBack()

mainLoop = True
while(mainLoop):
    print("=========================================")
    print("|| choose the following options:       ||")
    print("|| 1. To see who dont follow you back. ||")
    print("|| 2. To see who you dont follow back. ||")
    print("=========================================")
    optionLoop = True
    while(optionLoop):
        try:
            option = int(input("What is your choose??: ")) 
            if(option == 1 or option == 2):
                if(option == 1):
                    NotFollowUBack()
                    print("==========================================")
                    print("You Follow But They Dont Follow You Back: Total("+str(len(notFollowuBack))+")")
                    for each in notFollowuBack:
                        print("\t"+each, end="\n")
                    print("==========================================")
                elif(option == 2):
                    UDontFollowBack()

                    print("==========================================")
                    print("You Dont Follow them Back: Total("+str(len(uDontFollowBack))+")")
                    for each in uDontFollowBack:
                        print("\t"+each, end="\n")
                    print("==========================================")

                yesNoLoop = True
                while(yesNoLoop):   
                    try:
                        yesNo = str(input("Do you want to continue?: ")).upper()
                        if(yesNo == "Y"):
                            yesNoLoop = False
                            optionLoop = True
                        elif(yesNo == "N"):
                            print("\nExiting....")
                            time.sleep(0.5)
                            yesNoLoop = False
                            optionLoop = False
                            mainLoop = False
                        else:
                            print("Invalid choice. please choose again betweeen (Y,N)")
                            yesNoLoop = True
                    except:
                        print("Invalid choice. please choose again betweeen (Y,N)")
                        yesNoLoop = True
            else:
                print("Invalid choice. please choose again betweeen (1,2)")

        except:
            print("Invalid choice. please choose again betweeen (1,2)")
    



            
        

