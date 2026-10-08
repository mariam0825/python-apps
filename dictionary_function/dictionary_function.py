class student_data:
    def __init__(self, student_name: str, age: int, courses: str, address: str):
        self.user_id = None
        self.student_name = student_name
        self.age = age
        self.courses = [courses]
        self.address = address
        self.courses_in_department =["computer", "Math","Physics", "Biology","chemistry","Statistics", "English","Economics",
                                      "Economics", "History","Philosophy","Sociology","Political Science","Geography",
                                      "Psychology","Art","Music","Engineering","law","medicine","Business"]

    def assign_user_id(self, user_id: str):
        if self.student_name != "Mariam":
            raise ValueError("You are not a student")
        self.user_id = user_id

    def display_student_records(self, student_name: str, age: int, courses: str, address: str, user_id: str):
        if self.student_name != "Mariam":
            raise ValueError("You are not a student")
        self.student_name = student_name
        self.age = age
        self.courses = [courses]
        self.address = address
        self.user_id = user_id

    def display_courses(self, course):
        if course not in self.courses_in_department:
            raise ValueError("Course is not available")
        self.courses.append(course)

    def display_zip_code(self):
        for index in range(len(self.address)):
            if self.address[index] == ",":
                return self.address[:index]

    def display_city(self):
        for index in range(len(self.address) - 1, -1, -1):
            if self.address[index] == ",":
                return self.address[index + 1:]
    def add_new_course(self, course: str courses :str):
        if course not in self.courses_in_department:
            raise ValueError("Course is not available")
        elif courses == courses :
            raise ValueError("no duplicate courses")
            return




