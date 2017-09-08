import pickle
import random
numerals={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
alpha={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",100:"Hundred",1000:"Thousand"}

file1=file("roman.tag","wb")
pickle.dump(numerals,file1)
file1.close()
file2=open("roman.tag","rb")
num=pickle.load(file2)
file2.close()
n=1
def cls():
    print "\n"*7
print "\t"*3," ","Roman calculator and jackpot"
print "\t"*4,"     000000000000     "
print "\t"*4,"    00          00    "
print "\t"*4,"   00  ---   --- 00   "
print "\t"*4,"   00  '0     0' 00  "
print "\t"*4,"   00     !!     00   "
print "\t"*4,"   00            00    "
print "\t"*4,"    00   \__/   00    "
print "\t"*4,"     000000000000    "
print "\n"*3,

while True:
    if n>=0:
        print "1.Convert Numerical to roman numerical"
        print "2.To play a game"
        print "3.Number to text convertor"
        print "4.Roman calculator"
        print "5.Exit"
        print "\t"*3," "
        choice=input("Enter the choice:")
        print "\n"
        if choice==1:
            print "\t"*3,
            n=int(raw_input("Enter the number:"))
            print "\n"*5,
            try:
                if n>0:
                    while n>0:
                        print "\t"*2,"Thr equivalent romsn numeral for",n,"is:",
                        s=""
                        while n>0:
                            if n>10 and n<40:
                                s+=(numerals[10]*(n/10))
                                n=n%10
                            elif n>40 and n<50:
                                s+=(numerals[40])
                                n=n%10
                            elif n>50 and n<90:
                                s+=(numerals[50]+numerals[10]*((n-50)/10))
                                n=n%10
                            elif n>90 and n<100:
                                s+=numerals[90]
                                n=n%10
                            elif n in [1,4,5,9,10,40,50,90,100,400,500,900,1000]:
                                s+=numerals[n]
                                n=0
                            elif n<10 and n>0:
                                while n<10 and n>0:
                                    if n>1 and n<4:
                                        s+=(numerals[1]*n)
                                        n=n/10
                                    elif n>4 and n<9:
                                        s+=(numerals[5]+numerals[1]*(n-5))
                                        n=n/10
                            elif n>100 and n<400:
                                s+=numerals[100]*(n/100)
                                n=n%100
                            elif n>400 and n<500:
                                s+=numerals[400]
                                n=n%100
                            elif n>500 and n<900:
                                s+=numerals[500]+numerals[100]*((n-500)/100)
                                n=n%100
                            elif n>900 and n<1000:
                                s+=numerals[900]
                                n=n%100
                            elif n>1000 and n<4000:
                                s+=numerals[1000]*(n/1000)
                                n=n%1000
                        print s,"\n"
                elif n<0:
                    print "\t"*3,
                    raise ValueError,"Number entered is negative"
            except ValueError,e:
                print e.message
                n=1
            cls()
        elif choice==2:
            count=0
            while count<4:
                a=random.randint(1,10)
                print a
                print "\t"*3,"  ",
                n=input("Enter the number:")
                print "\t"
                if int(n)==int(a):
                    print "\n"*3
                    print "\t"*4,"..Winner winner winner.."
                    print "\n"
                    print "\t"*4,"Jackpot Jackpot Jackpot"
                    print "\n"
                    print "\t"*4,"     000000000000     "
                    print "\t"*4,"    00          00    "
                    print "\t"*4,"   00 ---   ---  00   "
                    print "\t"*4,"   00 '0     0'  00  "
                    print "\t"*4,"   00    !!      00   "
                    print "\t"*4,"   00            00    "
                    print "\t"*4,"    00  \__/     00    "
                    print "\t"*4,"     0000000000000    "
                    print "\n"*3,
                    break
                    


                else:
                    print "Better luck next time"
                print "You have",3-count,"Chances left"
                count+=1
            print "\t"*4,"The jackpot number is",a,"\n","\t"
            cls()
        elif choice==3:
            print "\t"*3,"  ",
            n=int(raw_input("Enter the number:"))
            print "\t"
            while n>0 and n<100000:
                print "\t"*2,"The equivalent number for",n,"In words is:","\n"
                s=""
                while n>0:
                    if n>20 and n<30:
                        s=s+(alpha[20])
                        n=n%20
                    elif n>30 and n<40:
                        s+=(alpha[30])+""
                        n=n%30
                    elif n>40 and n<50:
                        s=s+(alpha[40])+""
                        n=n%40
                    elif n>50 and n<60:
                        s=s+(alpha[50])+""
                        n=n%50
                    elif n>60 and n<70:
                        s=s+alpha[60]+""
                        n=n%60
                    elif n>70 and n<80:
                        s=s+slpha[70]+""
                        n=n%70
                    elif n>80 and n<90:
                        s=s+alpha[80]+""
                        n=n%80
                    elif n>90 and n<100:
                        s=s+alpha[90]+""
                        n=n%90
                    elif n in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,1000]:
                        s=s+alpha[n]+""
                        n=0
                    elif n>100 and n<1000:
                        s=s+(alpha[n/100]+""+alpha[100])+""
                        n=n%100
                    elif n>1000 and n<21000:
                        s=s+alpha[n/1000]+""+alpha[1000]+""
                        n=n%1000
                print "\t"*3,"",s,"\n"
                cls()
        elif choice==4:
            print "1.For addition"
            print "2.For multiplication"
            print "3.For integer division"
            print "4.For exponential"
            print "5.For subtraction"
            print "\n","\t"*3,"  "
            choice=raw_input("Enter the choice:")
            print "\n"
            print "\t"*3,
            f=input("Enter the first number:")
            print "\n"
            print "\t"*3,
            p=input("Enter the second number:")
            print "\n"
            if choice=="1":
                n=f+p
                print "\t"*4,f,"+",p,"=",n
                print "\t"*3,
                print "The equivalent numeric value is",n,"\n"
            elif choice=="2":
                n=f*p
                print "\t"*4,f,"*",p,"=",n,"\n"
                print "\t"*3,
                print "The equivalent numeric value is",n,"\n"
            elif choice=="3":
                n=f/p
                print "\t"*4,f,"/",p,"=",n,"\n"
                print "\t"*3,
                print "The equivalent numeric value is",n,"\n"
            elif choice=="4":
                n=f**p
                print "\t"*4,"**",p,"=",n,"\n"
                print "\t"*3,
                print "The equivalent numeric value is",n,"\n"
            elif choice=="5":
                n=f-p
                print "\t"*4,f,"-",p,"=",n,"\n"
                print "\t"*3,
                print "The equivalent numeric value is",n,"\n"
            s=""
            while n>0:
                if n>10 and n<40:
                    s+=(numerals[10]*(n/10))
                    n=n%10
                elif n>50 and n<90:
                    s+=(numerals[50]+numerals[10]*((n-50)/10))
                    n=n%10
                elif n>90 and n<100:
                    s+=numerals[90]
                    n=n%10
                elif n in [1,4,5,9,10,40,90,100,400,500,900,1000]:
                    s+=numerals[n]
                    n=0
                elif n<10 and n>0:
                    while n<10 and n>0:
                        if n>1 and n<4:
                            s+=(numerals[1]*n)
                            n=n/10
                        elif n>4 and n<9:
                            s+=(numerals[5]+numerals[1]*(n-5))
                            n=n/10
                elif n>100 and n<400:
                    s+=numerals[100]*(n/100)
                    n=n%100
                elif n>400 and n<500:
                    s+=numerals[400]
                    n=n%100
                elif n>500 and n<900:
                    s=numerals[500]+numerals[100]*((n-500)/100)
                    n=n%100
                elif n>900 and n<1000:
                    s+=numerals[900]
                    n=n%100
                elif n>1000 and n<4000:
                    s+=numerals[1000]*(n/1000)
                    n=n%1000
            print "\t"*3,"The equivalent roman numeral is",s,"\n"
            cls()
        elif choice==5:
            print "\t"*3,"Thank you for running the program"
            break
        elif choice>5:
            print "\t"*3,"The choice entered is out of range"
            n=1
        elif choice<0:
            print "\t"*3,"The choice entered is out of range"
            n=1
            
                    
