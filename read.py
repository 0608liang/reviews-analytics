data = []
count = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1 # 等同於count = count + 1
		if count % 1000 == 0 :
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_data = 0
for d in data :
	len(d)
	sum_data = sum_data + len(d)

print('全部留言的平均字數為', sum_data / len(data), '個字')

new = []
for d in data :
	if len(d) < 100 :
		new.append(d)
print('一共有', len(new), '筆留言長度小於100個字')
print(new[0])