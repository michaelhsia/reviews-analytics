data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: #print 跑很慢, 故讓他每1000筆顯示一次, %代表某數除以一個數的餘數
            print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d) #sum_len = sum_len + len(d), 將每筆留言長度及目前總數做加總
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d) #當 data 清單中的 d 有字數小於100的, 就存入 new 這個清單中
print('一共有', len(new), '筆資料長度小於100') #此行要在 for 框架之外, 否則每跑一次 for 就印一次
print(new[0])
print(new[1])