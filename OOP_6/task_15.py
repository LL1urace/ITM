# Практика

# 15. Напишите класс, содержит 3 любые атрибута и при изменении
# логгировать всё в консоль (при изменении старое->новое)
class StudentITM:
    """Класс, представляющий обучающегося в онлайн-школе ITM."""

    def __init__(self, current_topic: str, learning_progress: float = 0.0, education_status: bool = True) -> None:
        self.verify_current_topic(current_topic)
        self.verify_learning_progress(learning_progress)
        self.verify_education_status(education_status)

        self.__current_topic = current_topic # Текущая изучаемая тема
        self.__learning_progress = learning_progress # Прогресс обучения
        self.__education_status = education_status # Статус обучения (Учиться - true / Отчислен - false)
        print("[LOG] Создан новый экземпляр класса" , self)

    @classmethod
    def verify_current_topic(cls, current_topic) -> None:
        """Метод класса для верификации изучаемой темы."""
        if not isinstance(current_topic, str):
            raise TypeError("Текущая тема должна быть строкой!")

    @classmethod
    def verify_learning_progress(cls, learning_progress) -> None:
        """Метод класса для верификации прогресса обучения."""
        if not isinstance(learning_progress, (int, float)):
            raise TypeError("Прогресс обучения должен быть целым или вещественным числом!")
        if isinstance(learning_progress, bool):
            raise TypeError("Прогресс обучения должен быть числом, а не булевым значением!")
        if not 0 <= learning_progress <= 100:
            raise ValueError("Прогресс обучения должен находится в диапазоне между 0 и 100%!")

    @classmethod
    def verify_education_status(cls, education_status) -> None:
        """Метод класса для верификации статуса обучения."""
        if not isinstance(education_status, bool):
            raise TypeError("Статус обучения должен быть булевым значением!")

    # Сеттеры и геттеры
    @property
    def current_topic(self) -> str:
        return self.__current_topic

    @current_topic.setter
    def current_topic(self, current_topic) -> None:
        old_topic = self.__current_topic
        self.verify_current_topic(current_topic)
        self.__current_topic = current_topic
        print(f"[LOG] Изменение текущей изучаемой темы: {old_topic} -> {self.__current_topic}\n")

    @property
    def learning_progress(self) -> float:
        return self.__learning_progress

    @learning_progress.setter
    def learning_progress(self, learning_progress) -> None:
        old_progress = self.__learning_progress
        self.verify_learning_progress(learning_progress)
        self.__learning_progress = learning_progress
        print(f"[LOG] Изменение прогресса обучения: {old_progress} -> {self.__learning_progress}\n")

    @property
    def education_status(self) -> bool:
        return self.__education_status

    @education_status.setter
    def education_status(self, education_status) -> None:
        old_status = self.__education_status
        self.verify_education_status(education_status)
        self.__education_status = education_status
        print(f"[LOG] Изменение статуса обучения: {old_status} -> {self.__education_status}\n")

    def __str__(self) -> str:
        """Возвращает строковое представление класса StudentITM."""
        return (f"StudentITM:\n "
                f"Текущая изучаемая тема: {self.__current_topic}\n "
                f"Прогресс обучения: {self.__learning_progress}\n "
                f"Статус обучения: {self.__education_status}\n")




if __name__ == "__main__":
    studentITM_1 = StudentITM("Структуры данных", 1/50, True)

    studentITM_1.current_topic = "ООП"
    studentITM_1.learning_progress = 6/50
    studentITM_1.education_status = False

    print(studentITM_1)

    studentITM_2 = StudentITM("Структуры данных")