class BaseProduct:
     def __init__(self, product_id, name, price):
        self.product_id = str(product_id)
        self.name = str(name)
        self.price = float(price)

     def display_info(self):
        print(f"รหัสสินค้า : {self.product_id}")
        print(f"ชื่อสินค้า : {self.name}")
        print(f"ราคา       : {self.price:.2f} บาท")
class Product(BaseProduct):
     def __init__(self, product_id, name, price, stock):
        # เรียกใช้งาน Constructor ของคลาสแม่
        super().__init__(product_id, name, price)
        self.stock = int(stock)

    # Overriding Method เพื่อแสดงผลข้อมูลส่วนของสต็อกเพิ่ม
     def display_info(self):
        super().display_info()  # เรียกใช้การแสดงผลของคลาสแม่
        print(f"จำนวน      : {self.stock} ชิ้น")