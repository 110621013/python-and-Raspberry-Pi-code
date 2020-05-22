while True:
    try :
        num=input("enter:")
        e=input("e:")
        try:
            int(num)
        except:
            continue
        print(num,e)
    except ValueError:
        print("try again!!")
    