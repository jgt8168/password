password='a123456'
count=1
while True:
    if count<=3:
        inpw=input("請輸入密碼:")
        if inpw==password:
            print("登入成功")
            break
        else :
            count+=1
            print("密碼錯誤!還有",3-count,"次機會")
    else:
        print("最多輸入3次密碼")
        break
