Takeshi = {
	"身長": 164.0,
	"体重":  74.0,
	"好きな色": "green",
	"好きな作家": "吉川英治"
	}

attrib = input("Takeshiの何が知りたいですか？入力してください：")

if attrib in Takeshi:
    print(Takeshi[attrib])
else:
    print("その情報はありません。")

    
 
