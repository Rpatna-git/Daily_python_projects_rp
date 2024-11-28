
def Mood_booster(choice,name):
    if choice == 1:
        msg=f"Thats Great,{name}! Keep spreading your joy"
    elif choice == 2:
        msg=f"Take a Deep breath, {name} You are doing Amazing!!!"

    else:
        msg=f"Rest up {name}. Tomorrow is a fresh start!"
    return msg

def main():

    try:
        name = input("Hello ! what is your name?")
        if name:
            message=int(input(f""" Hi {name}! what are you feeling today?
                    1. Happy
                    2. Stressed 
                    3. Tired 
                        Choose 1,2,3:"""))
            if message:
                print(Mood_booster(message,name))

    except ValueError:
        print("Enter valid Choice")




if __name__ =='__main__':
    main()