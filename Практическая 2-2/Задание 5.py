class Brick:
    def __init__(self, color = "Красный", material = "Глина"):
        self.color = color
        self.material = material
    def __del__(self):
        print(f"Кирпич {self.color} из {self.material} удален")
    def information_brick(self):
        return f"{self.color}, {self.material}"
user_input_color = input("Введите желаемый цвет кирпича: ")
if user_input_color:
    color_brick = user_input_color
else:
    color_brick = "Красный"
user_input_material = input("Введите желаемый материал кирпича: ")
if user_input_material:
    material_brick = user_input_material
else:
    material_brick = "Глина"
brick = Brick(color_brick, material_brick)
print(f"Кирпич: {brick.information_brick()}")
