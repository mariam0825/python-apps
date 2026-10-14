class student_class(object):

    def __init__(self, name: str, ) -> None:
        self.name = name.lower()
        self.grade_level = 0

    def student_level(self, grade_level: int):
        if grade_level < 0:
            raise ValueError("Nothing like grade 0")
        self.grade_level = grade_level

    def promotion(self, grade_level: int):
        if grade_level < 0:
            raise ValueError("Nothing like grade 0")
        self.grade_level += 1

    def scores(self, score: int):
        if score < 0:
            raise ValueError("You can never make it!!!")
        elif score < 50:
            self.score = score
            return "failed"
        else:
            self.score = score
            return "passed"

    def update_name(self, new_name: str):
        if new_name is None:
            raise ValueError("Oga input your name !!!")
        self.name = new_name.lower()
        return self.name

    def is_graduating(self, grade_level: str):
        if grade_level < 12:
            return "still a student"
        else:
            return "Graduating students"
        self.grade_level = grade_level