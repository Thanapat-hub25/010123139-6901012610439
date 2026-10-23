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
        #อ่านข้อมูลจากไฟล์ขึ้นมาเก็บใน 2D Array
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
    def _save_to_file(self):
        """บันทึกข้อมูลจาก 2D Array ลงไฟล์"""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                for row in self.products_data:
                    file.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")
    def add_product(self):
        print("\n===== เพิ่มสินค้า =====")
        product_id = input("รหัสสินค้า: ")

        # เช็คไอดีซ้ำใน 2D Array
        for row in self.products_data:
            if row[0] == product_id:
               print("รหัสสินค้านี้มีอยู่ในระบบแล้ว")
               return

        name = input("ชื่อสินค้า: ")

        try:
            price = float(input("ราคาสินค้า: "))
            stock = int(input("จำนวนสินค้า: "))
            if price < 0 or stock < 0:
               print("ราคาและจำนวนต้องไม่ติดลบ")
               return
        except ValueError:
            print("ข้อผิดพลาด: กรุณากรอกตัวเลขให้ถูกต้อง")
            return

        # บันทึกลง 2D Array
        self.products_data.append([product_id,name, price, stock])
        self._save_to_file()
        print("เพิ่มสินค้าสำเร็จ!")

    def show_product(self):
        print("\n===== สินค้าทั้งหมด =====")
        if not self.products_data:
            print("ยังไม่มีสินค้า")
            return

        # ดึงข้อมูลจาก 2D Array มาสร้างเป็น Object ของคลาสลูก (Product)
        for row in self.products_data:
            p = Product(row[0], row[1], row[2], row[3])
            print("-------------------------")
            p.display_info()
        print("-------------------------")

    def search_product(self):
        print("\n===== ค้นหาสินค้า =====")
        search = input("กรอกรหัสสินค้า: ")

        for row in self.products_data:
            if row[0] == search:
                p = Product(row[0], row[1], row[2], row[3])
                print("พบสินค้า")
                print("-------------------------")
                p.display_info()
                print("-------------------------")
                return
        print("ไม่พบสินค้านี้")

    def stock_in(self):
        print("\n===== รับสินค้าเข้า =====")
        search = input("กรอกรหัสสินค้า: ")

        for row in self.products_data:
            if row[0] == search:
                try:
                    amount = int(input("จำนวนที่รับเข้า: "))
                    if amount <= 0:
                        print("จำนวนต้องมากกว่า 0")
                        return

                    row[3] += amount  # อัปเดตสต็อกใน 2D Array
                    self._save_to_file()

                    print("รับสินค้าเข้าสำเร็จ")
                    print(f"จำนวนคงเหลือ : {row[3]} ชิ้น")
                    return
                except ValueError:
                    print("ข้อผิดพลาด: กรุณากรอกตัวเลขจำนวนเต็ม")
                    return
        print("ไม่พบสินค้านี้")

    def stock_out(self):
        print("\n===== ขายสินค้าออก =====")
        search = input("กรอกรหัสสินค้า: ")

        for row in self.products_data:
            if row[0] == search:
                try:
                    amount = int(input("จำนวนที่ขาย: "))
                    if amount <= 0:
                        print("จำนวนต้องมากกว่า 0")
                        return

                    if amount <= row[3]:
                        row[3] -= amount
                        total = amount * row[2]
                        self._save_to_file()

                        print("ขายสินค้าสำเร็จ")
                        print(f"จำนวนที่ขาย : {amount}")
                        print(f"ราคา        : {total:.2f} บาท")
                        print(f"เหลือสินค้า : {row[3]} ชิ้น")
                    else:
                        print("สินค้าในคลังไม่เพียงพอ")
                    return
                except ValueError:
                    print("ข้อผิดพลาด: กรุณากรอกตัวเลขจำนวนเต็ม")
                    return
        print("ไม่พบสินค้านี้")

    def low_stock(self):
        print("\n===== สินค้าใกล้หมด =====")
        found = False
        for row in self.products_data:
            if row[3] <= 5:
                p = Product(row[0], row[1], row[2], row[3])
                print(f"{p.product_id} {p.name} เหลือ {p.stock} ชิ้น")
                found = True
        if not found:
            print("ไม่มีสินค้าใกล้หมด")


# =========================
# Main Program
# =========================
if __name__ == "__main__":
    manager = Inventory()

    while True:
        print("\n==============================")
        print("     ระบบจัดการคลังสินค้า")
        print("==============================")
        print("1. เพิ่มสินค้า")
        print("2. แสดงสินค้าทั้งหมด")
        print("3. ค้นหาสินค้า")
        print("4. รับสินค้าเข้า")
        print("5. ขายสินค้าออก")
        print("6. ตรวจสอบสินค้าใกล้หมด")
        print("0. ออกจากโปรแกรม")

        choice = input("เลือกเมนู: ")

        if choice == "1":
            manager.add_product()
        elif choice == "2":
            manager.show_product()
        elif choice == "3":
            manager.search_product()
        elif choice == "4":
            manager.stock_in()
        elif choice == "5":
            manager.stock_out()
        elif choice == "6":
            manager.low_stock()
        elif choice == "0":
            print("จบการทำงาน")
            break
        else:
            print("กรุณาเลือกเมนู 0-6")
