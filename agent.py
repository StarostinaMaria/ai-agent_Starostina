# Файл с логикой операций
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
