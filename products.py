products = []
while True :
	name = input('請輸入商品名稱: ')
	if name == 'q' :
		break
	price = input('請輸入產品價格: ')
	price = int(price)
	if price == 'q' :
		break
	p = [name, price]
	products.append(p)
print(products)

products[0][0] #大清單的第0個中的第0格清單
print(products[0][0])

for p in products :
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f :
	f.write('商品,價格\n')
	for p in products :
		f.write(p[0] + ',' + str(p[1]) + '\n')