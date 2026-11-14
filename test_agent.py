import unittest
import os
import agent


class TestAgent(unittest.TestCase):

    def setUp(self):
        # Подменяем имя файла на тестовое, чтобы не испортить основные данные
        self.test_file = "test_workouts.json"
        agent.DATA_FILE = self.test_file
        self.workouts = []

    def tearDown(self):
        # Удаляем тестовый файл после каждого теста
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_workout(self):
        """Проверяем добавление тренировки."""
        result = agent.add_workout(self.workouts, "Приседания")
        self.assertEqual(result, "Добавлено: Приседания")
        self.assertEqual(len(self.workouts), 1)
        # Проверяем, что статус "В планах"
        self.assertFalse(self.workouts[0]["done"])

    def test_mark_done(self):
        """Проверяем изменение состояния (отметку о выполнении)."""
        agent.add_workout(self.workouts, "Жим")
        result = agent.mark_done(self.workouts, 1)
        self.assertEqual(result, "Тренировка 'Жим' выполнена!")
        # Проверяем, что статус изменился
        self.assertTrue(self.workouts[0]["done"])

    def test_mark_done_error(self):
        """Проверяем ошибку при неверном ID."""
        result = agent.mark_done(self.workouts, 99)
        self.assertEqual(result, "Ошибка: Такого ID нет.")

    def test_save_and_load(self):
        """Проверяем, что данные сохраняются в файл и загружаются обратно."""
        agent.add_workout(self.workouts, "Бег")
        agent.save_workouts(self.workouts)

        loaded = agent.load_workouts()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["title"], "Бег")

    def test_load_no_file(self):
        """Проверяем первый запуск (когда файла еще нет)."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        loaded = agent.load_workouts()
        # Должен вернуться пустой список
        self.assertEqual(loaded, [])

    def test_show_workouts(self):
        """Проверяем вывод списка."""
        self.assertEqual(agent.show_workouts(self.workouts), "Список пуст.")
        agent.add_workout(self.workouts, "Йога")
        result = agent.show_workouts(self.workouts)
        self.assertIn("Йога", result)


if __name__ == "__main__":
    unittest.main()
