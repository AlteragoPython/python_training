from datetime import datetime


class DeadlineError(Exception):
    pass


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.datetime.now() + deadline

    def is_active(self):
        return datetime.datetime.now() < self.deadline



class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def do_homework(self, homework):
        if not homework.is_active():
            raise DeadlineError("You are late")

        solution = input("Enter your solution: ")
        if len(solution) < 5:
            raise ValueError("Solution is too short")

        self.homework = homework
        self.solution = solution


class Teacher:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def create_homework(self, text, deadline):
        homework = {"text": text, "deadline": deadline}
        self.homeworks.append(homework)
        return homework

    def check_homework(self, homework_solution):
        homework_text = homework_solution["text"]
        solution = homework_solution["solution"]
        if len(solution) < 5:
            return False
        if homework_text not in self.homework_solutions:
            self.homework_solutions[homework_text] = []
        self.homework_solutions[homework_text].append(solution)
        return True


