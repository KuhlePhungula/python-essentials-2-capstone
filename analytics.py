# student analytics

# Generator: yield each student who passed, one at a time
def passing_students(students):
    for student in students:
        if student.has_passed():
            yield student


# Closure: returns a grader function that remembers pass_mark
def make_grader(pass_mark):
    def grader(score):
        return "Pass" if score >= pass_mark else "Fail"
    return grader

def class_average(students):
    scores = [s.score for s in students]
    return sum(scores) / len(scores)

def highest(students):
    return max(s.score for s in students)

def lowest(students):
    return min(s.score for s in students)

def pass_rate(students, pass_mark=50):
    passing = [s for s in students if s.score >= pass_mark]
    return (len(passing) / len(students)) * 100

def top_two_score(students):
    scores = sorted((s.score for s in students), reverse=True)
    scores_iter = iter(scores)
    return next(scores_iter)


