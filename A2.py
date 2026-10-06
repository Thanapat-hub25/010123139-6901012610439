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
class Inventory:
    def __init__(self):
        # ใช้ 2D Array ในการเก็บข้อมูล [ [id, name, price, stock], ... ]
        self.products_data = []
        self.filename = "inventory.txt"
        self._load_from_file()
   def _load_from_file(self):
      """อ่านข้อมูลจากไฟล์ขึ้นมาเก็บใน 2D Array"""
      try:
         with open(self.filename, "r", encoding="utf-8") as file:
               self.products_data = []
               for line in file:
                  data = line.strip().split(",")
                  if len(data) == 4:
                     self.products_data.append([
                        data[0],
                        data[1],
                        float(data[2]),
                        int(data[3])
                        ])
      except FileNotFoundError:
         self.products_data = []
      except Exception as e:
         print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
