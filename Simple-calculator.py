def main1(a, b, c):
    if c == "+":
        if a % b == 0:
            print(int(a), "+", int(b), "=", int(a + b))
        elif a % 2 == 0:
            print(int(a), "+", b, "=", int(a) + b)
        elif b % 2 == 0:
            print(a, "+", int(b), "=", a + int(b))
        else:
            print(a, "+", b, "=", a + b)
        return

    elif c == "-":
        if a % b == 0:
            print(int(a), "-", int(b), "=", int(a - b))
        elif a % 2 == 0:
            print(int(a), "-", b, "=", int(a) - b)
        elif b % 2 == 0:
            print(a, "-", int(b), "=", a - int(b))
        else:
            print(a, "-", b, "=", a - b)
        return

    if a == 0 and b == 0:
        print("please enter correct number's")
        return

    elif c == "/":
        if b == 0:
            print("Error: division by zero!")
            return
        elif a // 2 == 0:
            print(int(a), "/", b, "=", int(a) / b)
        elif b // 2 == 0:
            print(a, "/", int(b), "=", a / int(b))
        else:
            print(int(a), "/", int(b), "=", int(a / b))
        return

    elif c == "*":
        if a // 2 == 0:
            print(int(a), "*", b, "=", int(a) * b)
        elif b // 2 == 0:
            print(a, "*", int(b), "=", a * int(b))
        else:
            print(int(a), "*", int(b), "=", int(a * b))
        return
        
    if c == "**" :   #Under development
        if a == 0 :
            print("err 0 ** number's = incorrect")
        else :

            if b == 0 :
                    if a%2 == 0:
                        print(int(a) , "**" , "0" , "=" , "1")
                    else:
                        print(a , "**" , "0" , "=" , "1")
                    return
        
            elif b > 0 and b%2==0 :
                print(int(a) ,"**" , int(b) , "=" , int(a ** b) )
            elif b > 0 and b in (float) :
                print(int(a) , "**" , b , "=" , int(a)**b)
            #else :
                #print(int(a) , "**" , int(b) , "=" , int(a ** b))
                return
    else:
        print("error please enter (* , / , + , -)")
        return


def loop():
    while True :
        raw = input("pleas enter number -->").strip()
        if raw.lower() in ("exit" , "quit" , "quit()" , "break") :
             confirm = input("do you want close the app?? yes or exit to quit and no to continue -->").strip()
             if confirm.lower() in ("yes" , "exit") :
                 print("bye bye")
                 break
             elif confirm.lower() in ("no" , "...") :
                 continue
        try :
                 
            a_str , c , b_str = raw.split()
            a =float(a_str)
            b =float(b_str)

        except :
            print("--pleas enter correct number--")
            continue
        main(a , b ,c)

loop()
