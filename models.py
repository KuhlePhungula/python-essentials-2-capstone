# models.py defines the Student and HonoursStudent classes (module 3 - OOP)

# Student class
class Student:
    #class variables
    school_name = "Melsoft Academy"
    total_students = 0

    def __init__(self, name, student_id, score):
        # instance variables
        self.name = name
        self.student_id = student_id
        self.score = score

        Student.total_students += 1

    # returns a grade label based on score
    def get_grade(self):
        if self.score >= 80:
            return "Distinction"
        elif self.score >= 50:
            return "Pass"
        else:
            return "Fail"
        
    # returns True if Student's score is a passing score (50+)
    def has_passed(self):
        return self.score >= 50

    def __str__(self):
        return f"{self.student_id}: {self.name} | Score: {self.score} | Grade: {self.get_grade()}"


# inherits from Student + research topic
class HonoursStudent(Student):

    def __init__(self, name, student_id, score, research_topic):
        super().__init__(name, student_id, score)
        self.research_topic = research_topic

    def get_grade(self):
        if self.score >= 75:
            return "Distinction (Honours)"
        return super().get_grade()

    def __str__(self):
        s_line = super().__str__()
        return f"{s_line} | Research: {self.research_topic}"



