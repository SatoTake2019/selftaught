Dictionary1ofBirthday = {"Hemingway": "7.21.1899",
                      "Fitzgerald": "9.24.1896"}
Dictionary2ofBirthday = {"Takeshi": 1966,
                         "Takashi": 1969}

print("前半：辞書１、辞書２をリストの要素として扱う。")

list_of_dictionary = [Dictionary1ofBirthday, Dictionary2ofBirthday]
print(list_of_dictionary)

print("\nリストからの要素取り出し")
print(list_of_dictionary.pop()) # リストからの要素取り出し

print("\n取り出した後のリストの内容")
print(list_of_dictionary)

print("\nリストへの要素追加")
list_of_dictionary.append(Dictionary2ofBirthday)
print(list_of_dictionary)

print("\nリストの中の辞書のバリューを変更")
list_of_dictionary[1]["Takeshi"] = "2.24.1966"
print(list_of_dictionary)

print("\n後半：辞書１、辞書２をタプルの要素として扱う。")

Dictionary1ofBirthday = {"Hemingway": "7.21.1899",
                      "Fitzgerald": "9.24.1896"}
Dictionary2ofBirthday = {"Takeshi": 1966,
                         "Takashi": 1969}

tuple_of_dictionary = (Dictionary1ofBirthday, Dictionary2ofBirthday)
print(tuple_of_dictionary)

print("\nタプルはイミュータブルなので、pop()メソッドもappendも使えません。")

print("\nタプルの中の辞書のバリューは変更できるようです。")
tuple_of_dictionary[1]["Takeshi"] = "2.24.1966"
print(tuple_of_dictionary)

