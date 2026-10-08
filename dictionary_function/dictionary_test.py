import unittest
from dictionary_function import student_data

class DictionaryTest(unittest.TestCase):

    def test_that_student_information_is_created_and_stored(self):
        student_info = student_data("Mariam", 18, "Biology", "1021, 12A,sabo,Lagos")
        self.assertEqual(student_info.student_name, "Mariam")
        self.assertEqual(student_info.age, 18)
        self.assertEqual(student_info.courses, ["Biology"])
        self.assertEqual(student_info.address, "1021, 12A,sabo,Lagos")

    def test_that_student_can_have_username_as_id(self):
        student_info = student_data("Mariam", 18, "Biology", "Lagos")
        student_info.assign_user_id("Bio/23/021")
        self.assertEqual(student_info.user_id, "Bio/23/021")

    def test_that_nonstudent_can_not_have_username_as_id(self):
        student_info = student_data("John", 18, "Biology", "1021, 12A,sabo,Lagos")
        with self.assertRaises(ValueError):
            student_info.assign_user_id("Bio/23/021")

    def test_that_university_can_display_student_records(self):
        student_info = student_data("Mariam", 18, "Biology", "1021, 12A,sabo,Lagos")
        student_info.display_student_records("Mariam", 18, "Biology", "1021, 12A,sabo,Lagos", "Bio/23/021")
        self.assertEqual(student_info.student_name, "Mariam")
        self.assertEqual(student_info.age, 18)
        self.assertEqual(student_info.courses, ["Biology"])
        self.assertEqual(student_info.address, "1021, 12A,sabo,Lagos")
        self.assertEqual(student_info.user_id, "Bio/23/021")

    def test_that_a_student_can_offer_more_than_one_course(self):
        student_info = student_data("Mariam", 18, "Biology", "1021, 12A,sabo,Lagos")
        student_info.display_courses("medicine")
        student_info.display_courses("Math")
        self.assertEqual(student_info.student_name, "Mariam")
        self.assertEqual(student_info.courses, ["Biology", "medicine", "Math"])

    def test_that_student_zip_code_can_be_displayed(self):
        student_info = student_data("Mariam", 18, "Biology", "1021, 12A,sabo,Lagos")
        self.assertEqual(student_info.display_zip_code(), "1021")

    def test_that_student_city_can_be_displayed(self):
        student_info = student_data("Mariam", 18, "Biology", "1021, 12A,sabo,Lagos")
        self.assertEqual(student_info.display_city(), "Lagos")

    def test_that_student_can_take_new_courses(self):
        student_info = student_data("Mariam", 18, "Biology", "1021, 12A,sabo,Lagos")
        student_info.display_courses("medicine")
        student_info.display_courses("Math")
        student_info.add_new_courses("chemistry")
        self.assertEqual(student_info.student_name, "Mariam")
        self.assertEqual(student_info.courses, ["Biology", "medicine", "Math","chemistry"])




