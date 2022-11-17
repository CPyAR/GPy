code=input("insert http error code: ")
point=code
point=point[:1]
match point:
    case "1":
        print("Informational responses")
    case "2":
        print("Successful responses")
    case "3":
        print("Redirection messages")
    case "4":
        print("Client error messages")
    case "5":
        print("Servererror messages")
    case _:
        print("exit")