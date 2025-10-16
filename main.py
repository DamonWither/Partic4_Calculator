class PaintCalculator:
    def __init__(self):
        # Базовая стоимость покраски
        self.base_price = 12000

        # Повышающие коэффициенты для деталей
        self.detail_coeffs = {
            "бампер": 1.0,
            "крыло": 1.1,
            "капот": 1.2,
            "крыша": 1.3,
            "дверь": 1.15
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
    
if __name__ == "__main__":
    pass