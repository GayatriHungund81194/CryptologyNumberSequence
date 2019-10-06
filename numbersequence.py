if __name__=="__main__":
    count3_1 = 0
    count4_1 = 0
    count5_1 = 0
    count6_1 = 0
    count7_1 = 0
    count8_1 = 0
    count9_1 = 0
    count10_1 = 0
    count11_1 = 0
    number = 4
    flag5 = 0
    flag4 = 0
    flag6 = 0
    flag7 = 0
    flag8 = 0
    flag9 = 0
    flag10 = 0
    flag11 = 0
    coun = 0
    flagExecuted = 0
    for i in range(10000):
        flagExecuted = 0
        count3_1 = count3_1 + 1
        count4_1 = count4_1 + 1
        count5_1 = count5_1 + 1
        count6_1 = count6_1 + 1
        count7_1 = count7_1 + 1
        count8_1 = count8_1 + 1
        count9_1 = count9_1 + 1
        count10_1 = count10_1 + 1
        count11_1 = count11_1 + 1
        coun = coun +1
        print("Generic Count:",coun)
        if (count3_1 == 3 or count3_1 == 4):
            print("Inside 3 loop")
            number = number + 3
            print("Increment by 3 ",number)
            if (count3_1 == 4):
                count3_1 = 0
            else:
                flagExecuted = 1

        elif (((count4_1 == 1 or count4_1 == 6) and flag4 == 0) or ((count4_1 == 3 or count4_1 == 8) and flag4 == 1)):
            print("Inside 4 loop")
            if ((count4_1 == 1 or count4_1 == 6) and flag4 == 0):
                number = number + 4
                print("Increment by 4 ",number)
                if (count4_1 == 6):
                    count4_1 = 0
                    flag4 = 1
            elif ((count4_1 == 3 or count4_1 == 8) and flag4 == 1):
                number = number + 4
                print("Increment by 4 ",number)
                if (count4_1 == 8):
                    count4_1 = 0
            else:
                flagExecuted = 1

        elif (((count5_1 == 2 or count5_1 == 13) and flag5 == 0) or ((count5_1 == 5 or count5_1 == 16) and flag5 == 1)):
            print("Inside 5 loop",count5_1)
            print("6 count",count6_1)
            if ((count5_1 == 2 or count5_1 == 13) and flag5 == 0):
                number = number + 5
                print("Increment by 5 ",number)
                if (count5_1 == 13):
                    count5_1 = 0
                    flag5 = 1
            elif ((count5_1 == 5 or count5_1 == 16) and flag5 == 1):
                number = number + 5
                print("Increment by 5 ",number)
                if (count5_1 == 16):
                    count5_1 = 0
            else:
                flagExecuted = 1

        elif (((count6_1 == 5 or count6_1 == 26) and flag6 == 0) or ((count6_1 == 11 or count6_1 == 32) and flag6 == 1)):
            print("Inside 6 loop")
            if ((count6_1 == 5 or count6_1 == 26) and flag6 == 0):
                number = number + 6
                print("Increment by 6 ",number)
                if (count6_1 == 26):
                    count6_1 = 0
                    flag6 = 1
            elif (((count6_1 == 11 or count6_1 == 32) and flag6 == 1)):
                number = number + 6
                print("Increment by 6 ",number)
                if (count6_1 == 32):
                    count6_1 = 0
            else:
                flagExecuted = 1

        elif (((count7_1 == 10 or count7_1 == 53) and flag7 == 0) or ((count7_1 == 21 or count7_1 == 64) and flag7 == 1)):
            print("Inside 7 loop")
            if ((count7_1 == 10 or count7_1 == 53) and flag7 == 0):
                number = number + 7
                print("Increment by 7 ",number)
                if (count7_1 == 53):
                    count7_1 = 0
                    flag7 = 1
            elif (((count7_1 == 21 or count7_1 == 64) and flag7 == 1)):
                number = number + 7
                print("Increment by 7 ",number)
                if (count7_1 == 64):
                    count7_1 = 0
            else:
                flagExecuted = 1
        
        elif (((count8_1 == 21 or count8_1 == 106) and flag8 == 0) or ((count8_1 == 43 or count8_1 == 128) and flag8 == 1)):
            print("Inside 8 loop")
            if ((count8_1 == 21 or count8_1 == 106) and flag8 == 0):
                number = number + 8
                print("Increment by 8 ",number)
                if (count8_1 == 106):
                    count8_1 = 0
                    flag8 = 1
            elif (((count8_1 == 43 or count8_1 == 128) and flag8 == 1)):
                number = number + 8
                print("Increment by 8",number)
                if (count8_1 == 128):
                    count8_1 = 0
            else:
                flagExecuted = 1

        elif (((count9_1 == 42 or count9_1 == 213) and flag9 == 0) or ((count9_1 == 85 or count9_1 == 256) and flag9 == 1)):
            print("Inside loop 9")
            if ((count9_1 == 42 or count9_1 == 213) and flag9 == 0):
                number = number + 9
                print("Increment by 9 ",number)
                if (count9_1 == 213):
                    count9_1 = 0
                    flag9 = 1
            elif (((count9_1 == 95 or count9_1 == 256) and flag9 == 1)):
                number = number + 9
                print ("Increment by 9",number)
                if (count9_1 == 256):
                    count9_1 = 0

        elif (((count10_1 == 85 or count10_1 == 426) and flag10 == 0) or ((count10_1 == 171 or count10_1 == 512) and flag10 == 1)):
            print("Inside loop 10")
            if ((count10_1 == 85) and flag10 == 0):
                number = number + 10
                print("Increment by 10 ",number)
            elif (((count10_1 == 171 or count10_1 == 512) and flag10 == 1)):
                number = number + 10
                print ("Increment by 10",number)
                if (count10_1 == 512):
                    count10_1 = 0
            
        # elif ((count11_1 == 170) and flag11 == 0):
        #     print("Inside loop 11")
        #     if ((count11_1 == 170) and flag11 == 0):
        #         number = number + 11
        #         print("Increment by 11 ",number)
        else:
            number = number + 11
            print("Increment by 11 ",number)
            print("X")
        print("\n")



        # if (count4_1 == 2 or count4_1 == 7):
        #     number = number + 4
        #     print("Increment by 4 ",number)
        #     if (count4_1 == 7):
        #         count4_1 = 0
        # if (count5_1 == 3 and flag5 == 0):
        #     number = number + 5
        #     print("Increment by 5 ",number)
        #     count5_1 = 0
        #     flag5 = 1
        # elif (count5_1 == 10 and flag5 == 1):
        #     number = number + 5
        #     print("Increment by 5 ",number)
        # elif (count5_1 == 15 and flag5 == 1):
        #     number = number + 5
        #     print("Increment by 5",number)
        #     count5_1 = 0
        # if (count6_1 == 6 or count6_1 == 31):
        #     number = number + 6
        #     print("Increment by 6 ",number)
        #     if (count6_1 == 31):
        #         count6_1 = 0
        # if (count7_1 == 11 ):
        #     number = number + 7
        #     print("Increment by 7 ",number)
        



    