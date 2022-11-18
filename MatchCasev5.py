code=input("insert http error code: ")
point=code
length=len(point)
point=point[:1]
match (point, length):
    case ("1" ,3):
        print("Informational responses")
    case ("2",3):
        print("Successful responses")
    case ("3",3):
        print("Redirection messages")
    case ("4",3):
        print("Client error messages")
    case ("5",3):
        print("Servererror messages")
    case _:
        print("exit")