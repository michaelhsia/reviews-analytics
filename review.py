data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: #print 跑很慢, 故讓他每1000筆顯示一次, %代表某數除以一個數的餘數
            print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

#計算留言平均長度
sum_len = 0
for d in data:
    sum_len += len(d) #sum_len = sum_len + len(d), 將每筆留言長度及目前總數做加總
print('留言的平均長度為', sum_len/len(data))

#範例：篩選每筆字數小於100的留言
new = []
for d in data:
    if len(d) < 100:
        new.append(d) #當 data 清單中的 每一筆留言'd' 有字數小於100的, 就存入 new 這個清單中
print('一共有', len(new), '筆留言長度小於100') #此行要在 for 框架之外, 否則每跑一次 for 就印一次

#範例：篩選每筆含有good的留言
good = []
for d in data:
    if 'good' in d:    #是非題, '字串' in 清單/'字串' -> True / False
        good.append(d) #data 數據中每一筆出來後, 只要 good 在裡面就會被裝進 good 清單 
                       #但 .append() 框框內也可裝其他資料型別 ex:True / 123...
print('一共有', len(good), '筆留言提到good')

#list comprehension(清單快寫法)
#good = [d for d in  data if 'good' in data] 完全等於第25-28行的篩選

#bad = ['bad' in d for d in data], 'bad' in d 會產出布林值 True / False
#'bad' in d 也可用任何資料型別取代, 快寫法很具彈性