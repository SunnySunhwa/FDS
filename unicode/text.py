#f = open('cp949.txt', 'wt', encoding = 'cp949')
f = open('utf_8.txt', 'wt', encoding = 'utf-8')

s = "나는 사과를 먹었다\n"

f.write(s)
f.close()
