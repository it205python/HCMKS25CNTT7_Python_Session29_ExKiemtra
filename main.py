from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self):
        super().__init__()
        self.__odometer = 0
    
    @property
    def odometer(self, odometer):
        return self.__odometer == odometer

    def calculate_efficiency(self):
        pass

    def drive(self, distance):
        if (self.distance > 0):
            self.odometer += distance
        else:
            raise ValueError
    
    def __lt__(self, other):
        return self.odometer < other.odometer
    
    @staticmethod
    def validate_license_plate(plate: str):
        if (len(plate) != 9 and not plate.startswith("29")):
            print("Biển số không hợp lệ")
            return False
        return True

class AutonomousFeature:
    def __init__(self):
        pass

    def calculate_efficiency(self):
        return 95.0

class ElectricBus(BaseVehicle):
    def __init__(self):
        super().__init__()

    def calculate_efficiency(self):
        cal_eff = 100 - (self.odometer * 0.005)

        if (cal_eff < 50):
            return 50.0
        return cal_eff
    

# class RoboBus(ElectricBus, AutonomousFeature):
#     def __init__(self, odometer):
#         super().__init__(odometer)

#     def calculate_efficiency(self):
#         self.calculate_efficiency + self.calculate_efficiency

def main():
    current_vehicle = None
    base_vehicle = BaseVehicle()
    while True:
        user_choice = input(""" === SMART TRANSIT MENU ===
1. Khởi tạo & đăng ký xe lái RoboBus mới
2. Giả lập vận hành & kiểm tra hiệu suất
3. Thoát
Chọn chức năng (1-2): """)
        match user_choice:
            case "1":
                print("--- KHỞI TẠO XE LÁI ROBOBUS ---")
                while True:
                    input_plate = input("Nhập biển số xe (9 ký tự, bắt đầu bằng 29): ").strip().upper()
                    if base_vehicle.validate_license_plate(input_plate):
                        print("[Thành công]: Khởi tạo phương tiện RoboBus thành công!")
                        current_vehicle = input_plate
                        print(f"[MRO Architecture]: ")
                        break
            case "2":
                pass
            case "3":
                print("Thoát chương trình")
                break

if __name__ == "__main__":
    main()