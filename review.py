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