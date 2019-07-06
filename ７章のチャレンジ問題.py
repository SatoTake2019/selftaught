
list0 = [1, 3, 5, 7, 9, 11, 13]

c = input("数字を当ててください。終了したいときは「q」を入力してください")

while c != "q" :
    print(c)

    if c.isdigit() == True:
        if int(c) in list0:
            print("正解")
        else:
            print("不正解")
    else:
    	print("数字を入力するか、qで終了します。")
	
    c = input("数字を当ててください。終了したいときは「q」を入力してください")




	
