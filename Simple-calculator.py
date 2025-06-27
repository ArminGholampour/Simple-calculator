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
        if a % b == 0:
            print(int(a), "/", int(b), "=", int(a / b))
        elif a % 2 == 0:
            print(int(a), "/", b, "=", int(a) / b)
        elif b % 2 == 0:
            print(a, "/", int(b), "=", a / int(b))
        else:
            print(a, "/", b, "=", a / b)
        return

    elif c == "*":
        if a % b == 0:
            print(int(a), "*", int(b), "=", int(a * b))
        elif a % 2 == 0:
            print(int(a), "*", b, "=", int(a) * b)
        elif b % 2 == 0:
            print(a, "*", int(b), "=", a * int(b))
        else:
            print(a, "*", b, "=", a * b)
        return
        
    #if c == "**" :   #Under development
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
            else:
                print("error please enter (* , / , + , -)")
        return


def loop():
    while True:
        raw = input("yek chiz vared konid for exam :: 5 + 1 or ('exit') :").strip()  #Receives a number from the user (with a space)
        
        if raw.lower() in ("exit", "break", "quit", "quit()"): 
            print("bye bye")
            break
        
        try:
            a_str, c, b_str = raw.split()
            a = float(a_str)
            b = float(b_str)
        except:
            print("pleas enter correct number's.")
            continue
        
        main1(a, b, c)

loop()
