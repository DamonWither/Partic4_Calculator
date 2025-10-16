class PaintCalculator:
    def __init__(self):
        # Базовая стоимость покраски
        self.base_price = 12000

        # Повышающие коэффициенты для деталей
        self.detail_coeffs = {
            "бампер": 2.0,
            "крыло": 2.1,
            "капот": 2.2,
            "крыша": 2.3,
            "дверь": 2.15
        }

        # Повышающие коэффициенты для цветов
        self.color_coeffs = {
            "белый": 1.0,
            "черный": 1.1,
            "красный": 1.2,
            "синий": 1.15,
            "металлик": 1.3
        }

    def calculate_price(self, detail: str, color: str) -> float:
        # Получаем коэффициенты (если нет — берём 1.0)
        detail_coeff = self.detail_coeffs.get(detail.lower(), 1.0)
        color_coeff = self.color_coeffs.get(color.lower(), 1.0)

        # Итоговая стоимость
        price = self.base_price * detail_coeff * color_coeff
        return price

class PaintApp:
    def __init__(self):
            self.calculator = PaintCalculator()

    def run(self):
        print("=== Калькулятор стоимости покраски ===")
        detail = input("Введите наименование детали (бампер, крыло, капот, крыша, дверь): ").strip()
        color = input("Введите цвет (белый, черный, красный, синий, металлик): ").strip()

        price = self.calculator.calculate_price(detail, color)
        print(f"\nСтоимость покраски детали '{detail}' цвета '{color}' составляет: {price:.2f} руб.\n")

if __name__ == "__main__":
    app = PaintApp()
    app.run()