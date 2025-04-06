meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GG":"İyi Oyunlar",
            "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir",
            "IDK":"Bilmiyorum",
            "LMAO":"ÇOK GÜLMEK",
            "AFK":"Klavye'den uzakta",
            }

word=input("Anlamadıgınız kelimeyi yazınız")


if word in meme_dict.keys():
    print(meme_dict[word])

else:
   print("bu kelime yok")
