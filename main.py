import string
from server import Server

# gather a list of letters
def alphabet():
    lowerCase = list(string.ascii_lowercase)
    # upperCase = list(string.ascii_uppercase)
    return lowerCase # + upperCase

# go through the list to find password
def main(alphabet,password):
    # print("Hello, world!")
    # z = 1
    guess = ""

    for x in alphabet:
        for y in alphabet:
            for z in alphabet:
                for u in alphabet:
                    for i in alphabet:
                        for o in alphabet:
                            guess = x + y + z + u + i + o
                            alpha = Server.getItem(guess)
                            # print(alpha)
                            if alpha: # it'll be something like, if alpha returns true
                                return alpha
        #                 guess = x + y + z + u + i
        #                 alpha = Server.getItem(guess)
        #                 if alpha.__eq__(password):
        #                     return alpha
        #             guess = x + y + z + u
        #             alpha = Server.getItem(guess)
        #             if alpha.__eq__(password):
        #                 return alpha
        #         guess = x + y + z
        #         alpha = Server.getItem(guess)
        #         if alpha.__eq__(password):
        #             return guess
        #     guess = x + y
        #     if alpha.__eq__(password):
        #         return alpha
        # guess = x
        # alpha = Server.getItem(guess)
        # if alpha.__eq__(password):
        #     return alpha
        
    return "Password not found!"


password = "astros"
word = main(alphabet(),password)
print("The password was ", word)