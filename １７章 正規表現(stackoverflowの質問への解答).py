slist = ['犬はよく泣いています。', 'その家の犬は良く吠える犬です。', 'その犬はご飯を食べました。']
>>> for i, words in enumerate(slist):
	found = re.findall(".*犬.*犬.*", words)
	for match in found:
		print(match)
