# a. Tạo một dict product_map từ products để tra cứu nhanh theo product_id với dạng:
def create_product_map(list_products: list[tuple]) -> dict:
    product_map = {}

    for product_id, name, price in list_products:
        product_map[product_id] = {"name": name, "price": price}

    return product_map


# b. Với mỗi hóa đơn trong orders, hãy tính tổng tiền của hóa đơn đó, lưu vào key mới "total" trong từng dict hóa đơn
def calculate_order_total(list_orders: list[dict], product_map: dict) -> None:
    for order in list_orders:
        total = 0

        for item_id in order["items"]:
            if item_id in product_map:
                total += product_map[item_id]["price"]

        order["total"] = total


# c. In ra danh sách hóa đơn theo format:
def print_orders(list_orders: list[dict]) -> None:
    for order in list_orders:
        items = order["items"]
        print(f"{order['order_id']}: {len(items)} san pham, Tong tien: {order['total']:,} VND")


# d. Tạo một set all_products_sold chứa tất cả product_id đã từng được bán trong mọi hóa đơn, sau đó in ra:
def get_all_products_sold(list_orders: list[dict]) -> set:
    all_products_sold = set()

    for order in list_orders:
        for item_id in order["items"]:
            all_products_sold.add(item_id)

    return all_products_sold


if __name__ == "__main__":
    # Mỗi sản phẩm là 1 tuple (product_id, name, price)
    products = [
        (1, "Ban Phim", 250_000),
        (2, "Chuot", 150_000),
        (3, "Man Hinh", 3_000_000),
        (4, "Tai Nghe", 500_000),
    ]

    # Danh sách đơn hàng (list dict)
    orders = [
        {"order_id": "HD01", "items": [1, 2, 4]},
        {"order_id": "HD02", "items": [2, 3]},
        {"order_id": "HD03", "items": [1, 4]},
    ]

    product_map = create_product_map(products)
    print("Product Map:")
    for product_id, info in product_map.items():
        print(f"{product_id}: {info}")

    calculate_order_total(orders, product_map)
    print("\nOrders with Total:")
    for order in orders:
        print(order)

    print("\nOrder Summary:")
    print_orders(orders)

    all_products_sold = get_all_products_sold(orders)
    print("\nAll Products Sold:")
    print(f"So luong san pham da ban: {len(all_products_sold)}")
