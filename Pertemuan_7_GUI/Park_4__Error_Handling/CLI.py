def main():
    while True:
        print("=====Menu======")
        print("1.Start")
        print("2.Exit")
        selection = input("Selection (1/2):")
        try:
            selection = int(selection)
            match selection:
                case 1 :
                    print("Start")
                case 2 :
                    print("End")
                    break
                case _ :
                    print("Invalid Input")
        except ValueError:
            print("Please input number not word!!")
main()