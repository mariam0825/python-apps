import unittest
from student_class import *


class studentClassTest(unittest.TestCase):
    def test_that_classroom_can_be_created(self):
        classroom = student_class("Winifred")
        self.assertEqual(classroom.grade_level, 0)
        self.assertEqual(classroom.name, "winifred")

    def test_that_Student_can_have_a_grade(self):
        classroom = student_class("Winifred")
        classroom.student_level(5)
        self.assertEqual(classroom.grade_level, 5)

    def test_that_Student_can_be_promoted(self):
        classroom = student_class("Winifred")
        classroom.student_level(5)
        classroom.promotion(6)
        self.assertEqual(classroom.grade_level, 6)

    def test_that_have_student_have_score(self):
        classroom = student_class("Winifred")
        classroom.student_level(5)
        self.assertEqual(classroom.scores(20), "failed")

    def test_that_have_student_have_score(self):
        classroom = student_class("Winifred")
        classroom.student_level(5)
        self.assertEqual(classroom.scores(80), "passed")

    def test_that_student_can_update_name(self):
        classroom = student_class("Winifred")
        self.assertEqual(classroom.update_name("Sandara"), "sandara")

    def test_for_Student_That_are_about_to_graduating(self):
        classroom = student_class("Winifred")
        self.assertEqual(classroom.is_graduating(12), "Graduating students")

