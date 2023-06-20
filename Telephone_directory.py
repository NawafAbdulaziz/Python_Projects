def dict():
    valu=None
    name_to_number={"Amal":1111111111,"Mohammed":2222222222,"Khadijah":3333333333,"Abdullah":4444444444,"Rawan":5555555555,"Faisal":6666666666
                    ,"Layla":7777777777}
    number_to_name={"1111111111":"Amal",2222222222:"Mohammed",3333333333:"Khadijah",4444444444:"Abdullah",5555555555:"Rawan",6666666666:"Faisal"
                    ,7777777777:"Layla"}
    while True:
        order=input("enter what you want(Search by name - Search by number - Add contacts -exsit )")
        #whi start
        if order=="Search by name" :
            valu = input("enter the name ")
            if (valu in name_to_number ):
                print(name_to_number[valu])
            else:
                print("Sorry, the number is not found ")

        elif order=="Search by number":

            valu = int(input("enter the number "))
            if (valu in number_to_name):
                print(number_to_name[valu])
            else:
                print("Sorry, the number is not found ")


        elif order=="Add contacts":
            valu = input("enter the name ")
            valu2 = input("enter the number ")
            if (valu2.isdigit()==True) and (len(valu2)<= 10):
                number_to_name[int(valu2)]=str(valu)
                name_to_number[valu]=int(valu2)
            else:
                print("This is invalid number")

        elif order == "exsit":
            break;
        # whi end







dict()










