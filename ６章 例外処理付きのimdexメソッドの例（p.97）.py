

def return_index(s):
    try:
        return "animals".index(s)
    except:
        return s + " is not found."


s = input("探したい一文字は？：")

print(return_index(s))



    
