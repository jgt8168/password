password='a123456'
count=0
while True:
    count+=1
    inpw=input("請輸入密碼:")
    if count<=3:        
        if inpw==password:
            print("登入成功")
            break
        else :    
            if count==3:
                print("最多輸入3次密碼")
                break        
            print("密碼錯誤!還有",3-count,"次機會")
   