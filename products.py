products = []
while True :
	name = input('請輸入商品名稱: ')
	if name == 'q' :
		break
	price = input('請輸入產品價格: ')
	if price == 'q' :
		break
	p = [name, price]
	products.append(p)
print(products)

products[0][0] #大清單的第0個中的第0格清單
print(products[0][0])