from datetime import datetime, timedelta

class DeadlineError(Exception):
    pass

class Homework:
    def __init__(self, text, deadline_days):
        self.text = text
        self.deadline = datetime.now() + timedelta(days=deadline_days)

    def is_active(self):
        return datetime.now() < self.deadline

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.homework_done = {}
        self.surname = surname

    def do_homework(self, homework, solution):
        if not homework.is_active():
            raise DeadlineError("You are late")
        return solution
class Teacher:
    homework_done = {}
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_solution):
        homework = homework_solution.homework
        solution = homework_solution.solution
        if len(solution) < 5:
            return False
        if homework not in cls.homework_done:
            cls.homework_done[homework] = []
        cls.homework_done[homework].append(solution)
        return True

    @classmethod
    def reset_results(cls, homework=None):
        if homework is None:
            cls.homework_done.clear()
        elif homework in cls.homework_done:
            cls.homework_done[homework] = []


