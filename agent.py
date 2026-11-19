# Файл с логикой операций и работой с хранилищем

import json
import os

DATA_FILE = "workouts.json"
LOAD_ERROR = False


def load_workouts():
    """Загружает тренировки из файла."""
    global LOAD_ERROR
    LOAD_ERROR = False

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        LOAD_ERROR = True
        print("Ошибка чтения файла. Начинаем с пустого списка.")
        return []


def save_workouts(workouts):
    """Сохраняет тренировки в файл."""

    if LOAD_ERROR and not workouts:
        print("Сохранение отменено: файл был поврежден при загрузке.")
        return False

    try:
        with open(DATA_FILE, "w") as f:
            json.dump(workouts, f, ensure_ascii=False, indent=4)
        return True
    except IOError:
        print("Ошибка сохранения данных.")
        return False


def add_workout(workouts, title):
    """Добавляет тренировку в список."""
    workout = {"id": len(workouts) + 1, "title": title, "done": False}
    workouts.append(workout)
    return f"Добавлено: {title}"


def show_workouts(workouts):
    """Показывает все тренировки."""
    if not workouts:
        return "Список пуст."
    result = "\n--- Ваши тренировки ---\n"
    for w in workouts:
        status = "Выполнена" if w["done"] else "В планах"
        result += f"[{w['id']}] {w['title']} — {status}\n"
    return result


def mark_done(workouts, workout_id):
    """Отмечает тренировку выполненной."""
    for w in workouts:
        if w["id"] == workout_id:
            w["done"] = True
            return f"Тренировка '{w['title']}' выполнена!"
    return "Ошибка: Такого ID нет."
