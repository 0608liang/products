import os # operating system

products = []

if os.path.isfile('products.csv') : # .是指中文 的 的意思
	print('yeah! 找到檔案了')
	with open ('products.csv', 'r', encoding = 'utf-8')as f :
		for line in f : #因為讀取檔案室一行一行讀，所以取作line
			name, price = line.strip().split(',') # strip可以去除空格與換行字 # split適用於分割內容的()括號中寫上從哪分割
			products.append([name, price])
	print(products)
else :
	print('找不到檔案....')



with open ('products.csv', 'r', encoding = 'utf-8')as f :
	for line in f : #因為讀取檔案室一行一行讀，所以取作line
		name, price = line.strip().split(',') # strip可以去除空格與換行字 # split適用於分割內容的()括號中寫上從哪分割
		products.append([name, price])
		print(products)


while True :
	name = input('請輸入商品名稱: ')
	if name == 'q' :
		break
	price = input('請輸入產品價格: ')
	price = int(price)
	if price == 'q' :
		break
	products.append([name, price])
print(products)

products[0][0] #大清單的第0個中的第0格清單
print(products[0][0])

for p in products :
	print(p[0], '的價格是', p[1])

# encoding = 'utf-8' 是讓程式被讀取時編碼可以正確，致使不會出現亂碼現象。
with open('products.csv', 'w', encoding = 'utf-8') as f :
	f.write('商品,價格\n')
	for p in products :
		f.write(p[0] + ',' + str(p[1]) + '\n')