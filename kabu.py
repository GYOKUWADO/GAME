import random
import time

list_x = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
#list_x = [1,2,3,4,5,6,7,5,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

random.shuffle(list_x)

#print(list_x)

card_one = (list_x[0])
card_two = (list_x[1])
card_three = (list_x[2])
card_four = (list_x[3])
master_card = (list_x[4])

def NimaimeNoCard():
        print("二枚目のカードは",list_x[5],"です。")

def SanmaimeNoCard():
        print("三枚目のカードは",list_x[6],"です。")

def B():
         master_card_of_two_A = master_card + list_x[7]
         if str(master_card_of_two_A)[-1] == str(9):
          print("合計は",master_card_of_two_A,"です。")
          print("引けです。")
          if str(master_card_of_two_A)[-1] > str(test)[-1]:
           print("親の勝ちです")
           exit()
         elif str(master_card_of_two_A)[-1] < str(test)[-1]:
          print("三枚目を引きます。")
          master_card_of_three = master_card_of_two_A + list_x[8]
          print("合計は",master_card_of_three,"です。")
          if str(master_strcard_of_three)[-1] > str(test)[-1]:
           print("親の勝ちです")
           exit()
         elif str(master_card_of_two_A)[-1] <= str(8):
          if  str(master_card_of_two_A)[-1] == str(test)[-1]:
           print("三枚目を引きます。")
           master_card_of_three = master_card_of_two_A + list_x[8]
           print("合計は",master_card_of_three,"です。")
           if str(master_card_of_three)[-1] > str(test)[-1]:
            print("親の勝ちです")
            exit()

def master_card_of_two():
        time.sleep(5)
        print("########################################")
        print("親の一枚目のカードは",master_card,"です。")
        time.sleep(5)
        print("親の二枚目のカードは",list_x[7],"です。")
        master_card_of_two_A = master_card + list_x[7]
        #print("合計は",master_card_of_two_A,"です。")

        if string == 1:
         #NimaimeOne = one + list_x[6]
         #test= one + list_x[6]
         B()

        elif string == 2:
         #NimaimeTwo = two + list_x[6]
         #test = two + list_x[6]
         B()

        elif string == 3:
         #NimaimeThree = three + list_x[6]
         #test = three + list_x[6]
         B()

        elif string == 4:
         #NimaimeFour = four + list_x[6]
         #test = four + list_x[6]
         B()
        else:
         exit()


def ESC():
    esc = input("逃げますか?(y/n)")
    if esc == "y":
     exit()
    elif esc == "n":
          if string == 1:
            NimaimeOne = one + list_x[6]
            SanmaimeNoCard()
            print("合計は",NimaimeOne,"です。")
            master_card_of_two()
          elif string == 2:
            NimaimeTwo = two + list_x[6]
            SanmaimeNoCard()
            print("合計は",NimaimeTwo,"です。")
            master_card_of_two()
          elif string == 3:
            NimaimeThree = three + list_x[6]
            SanmaimeNoCard()
            print("合計は",NimaimeThree,"です。")
            master_card_of_two()
          elif string == 4:
            NimaimeFour = four + list_x[6]
            SanmaimeNoCard()
            print("合計は",NimaimeFour,"です。")
            master_card_of_two()
    else:
     ESC()

def D():
          if string == 1:
            NimaimeOne = one + list_x[6]
            SanmaimeNoCard()
            print("合計は",NimaimeOne,"です。")
            master_card_of_two()
          elif string == 2:
            NimaimeTwo = two + list_x[6]
            SanmaimeNoCard()
            print("合計は",NimaimeTwo,"です。")
            master_card_of_two()
          elif string == 3:
            NimaimeThree = three + list_x[6]
            SanmaimeNoCard()
            print("合計は",NimaimeThree,"です。")
            master_card_of_two()
          elif string == 4:
            NimaimeFour = four + list_x[6]
            SanmaimeNoCard()
            print("合計は",NimaimeFour,"です。")
            master_card_of_two()

def E():
   if str(test_b)[-1] == str(0):
    ESC()
   elif str(test_b)[-1] == str(1):
    D()
    master_card_of_two()
   elif str(test_b)[-1] == str(2):
    D()
    master_card_of_two()
   elif str(test_b)[-1] == str(3):
    D()
    master_card_of_two()
   elif str(test_b)[-1] == str(4):
    D()
    master_card_of_two()
   elif str(test_b)[-1] == str(5):
    NextCard_A()
   elif str(test_b)[-1] == str(6):
    NextCard_A()
   elif str(test_b)[-1] >= str(7):
    if string == 1:
     test_a = one
     C()
    elif string == 2:
     test_a = two
     C()
    elif string == 3:
     test_a = three
     C()
    elif string == 4:
     test_a = four
     C()

def C():
          time.sleep(5)
          print("########################################")
          print("親の一枚目のカードは",master_card,"です。")
          time.sleep(5)
          print("親の二枚目のカードは",list_x[6],"です。")
          NimaimeMaster_card = master_card + list_x[6]
          print("合計は",NimaimeMaster_card,"です。")
          if str(NimaimeMaster_card)[-1] == str(9):
           if str(NimaimeMaster_card)[-1] > str(test_a)[-1]:
            print("親の勝ちです")
            exit()
          elif str(NimaimeMaster_card)[-1] < str(test_a)[-1]:
           print("三枚目を引きます。")
           master_card_of_three = NimaimeMaster_card + list_x[7]
           print("合計は",master_card_of_three,"です。")
           if str(master_card_of_three)[-1] > str(test_a)[-1]:
            print("親の勝ちです")
            exit()
          elif str(master_card_of_three)[-1] <= 8:
           if  str(master_card_of_three)[-1] == str(test_a)[-1]:
            print("三枚目を引きます。")
            master_card_of_three = NimaimeMaster_card + list_x[7]
            print("合計は",master_card_of_three,"です。")
            if str(master_card_of_three)[-1] > str(test_a)[-1]:
             print("親の勝ちです")
             exit()
def NextCard_A():
        YorN = input("もう一枚引きますか?(y/n):")
        if YorN == "y":
          D()
        elif YorN == "n":
         if string == 1:
          C()
         elif string == 2:
          C()
         elif string == 3:
          C()
         elif string == 4:
          C()
        else:
          NextCard_A()

print("[1]番:",card_one," [2]番:",card_two," [3]番:",card_three," [4]番:",card_four,sep='')
string = int(input("番号を選んでください:"))
if string == 1:
   print("########################################")
   print("一枚目のカードは",card_one,"です。")
   NimaimeNoCard()
   one = card_one + list_x[5]
   print("合計は",one,"です。")
   test_b = one
   test_a = one
   test= one + list_x[6]
   E()

elif string == 2:
   print("########################################")
   print("一枚目のカードは",card_two,"です。")
   NimaimeNoCard()
   two = card_two + list_x[5]
   print("合計は",two,"です。")
   test_b = two
   test_a = two
   test= two + list_x[6]
   E()

elif string == 3:
   print("########################################")
   print("一枚目のカードは",card_three,"です。")
   NimaimeNoCard()
   three = card_three + list_x[5]
   print("合計は",three,"です。")
   test_b = three
   test_a = three
   test= three + list_x[6]
   E()

elif string == 4:
   print("########################################")
   print("一枚目のカードは",card_four,"です。")
   NimaimeNoCard()
   four = card_four + list_x[5]
   print("合計は",four,"です。")
   test_b = four
   test_a = four
   test= four + list_x[6]
   E()
else:
   exit()