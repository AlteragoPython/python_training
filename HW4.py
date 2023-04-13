import datetime
from collections import defaultdict

class DeadlineError(Exception):
    pass

class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < self.created + self.deadline

class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkSolution(self, homework, solution)
        else:
            raise DeadlineError("You are late")

class Teacher:
    homework_done = defaultdict(set)

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_solution):
        if len(homework_solution.solution) > 5:
            cls.homework_done[homework_solution.homework].add(homework_solution)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework:
            cls.homework_done[homework] = set()
        else:
            cls.homework_done.clear()

class HomeworkSolution:
    def __init__(self, author, homework, solution):
        self.author = author
        self.homework = homework
        self.solution = solution





