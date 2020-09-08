
#讀取檔案

products = []

with open ("products.csv" , "r" , encoding="utf-8") as f :
    for line in f :
        if "商品 , 價格" in line :
            continue
        name , price = line.strip().split(",")
        products.append([name ,price])
print (products)

#讓使用者輸入

products = []
while True :
    name = input("輸入商品名稱 :")
    if name == "q" :
        break
    price = input("請輸入價格 :")
    p = []
    p.append(name)
    p.append(price)
    # 8-10 => p = ["name" , "price"]
    products.append(p)
print(products)

#印出清單
for p in products :
    print(p[0] , "的價格是" , p[1])

#讀取清單
with open ("products.csv" , "w" , encoding = "utf-8") as f :
    f.write("商品 , 價格\n")
    for p in products : 
        f.write(p[0] + "," + str(p[1]) + "\n")





