def CubedPlusEight(x):
    i = x**3 + 8
    return(i)




def main():
    print(CubedPlusEight(9))
    if(CubedPlusEight(9)>27):
        print("YAY!!")


if __name__=="__main__":
    main()