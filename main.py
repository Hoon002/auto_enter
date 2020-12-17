filename = input("릴리즈: 201217\
    \n영훈이가 만든 성현이 웹 소설 편히 읽도록 도와주는 프로그램\n프로그램과 동일한 폴더에 소설 파일 넣고 (파일이름).txt\n입력: ")

with open(filename, "a", encoding="utf-8") as pre_target:
    pre_target.write("\n--엔터 추가 완료--")

with open(filename, encoding="utf-8") as target:
    all_texts = []
    strimed = []
    while True:
        raw = target.readline()
        if raw == "--엔터 추가 완료--": break        
        strimed = raw.split(".")
        for splited_ln in strimed:
            if splited_ln == "\n":
                pass
            else:
                splited_ln = splited_ln+"."
            inspection = list(splited_ln)
            if inspection[0] == "“":
                upper_splited = splited_ln.split("“")
                all_texts.append("“\n"+upper_splited[-1])
                continue
            elif inspection[-1] == "”":
                lower_splited = splited_ln.split("”")
                all_texts.append("\n”"+lower_splited[-1]+"\n")
                continue
            all_texts.append(splited_ln)
            all_texts.append("\n")

with open("result.txt", "w", encoding="utf-8") as result:
    for ln in all_texts:
        result.write(ln)

print("실행 폴더에 result.txt로 저장되었습니다.\n확인하십시오..!")