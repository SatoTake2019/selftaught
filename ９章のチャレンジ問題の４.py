import csv

lists = ["トップガン", "リスキービジネス", "マイノリティーリポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレイニングデイ", "マンオンファイヤ", "フライト"]

with open("d:\\My Document Files\\WEBシステム\\独学プログラマ\\movies.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(lists[0])
    w.writerow(lists[1])
    w.writerow(lists[2])


    
