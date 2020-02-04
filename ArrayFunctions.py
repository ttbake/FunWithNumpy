import numpy as np

student_gpas = np.array([[4, 3.285, 3.5, 4],
                         [3.2, 3.8, 4, 4],
                         [3.96, 3.92, 4, 4]], dtype=float)

print("student gpa mean axis 1: " + str(student_gpas.mean(axis=1)))
print("student gpa mean axis 0: " + str(student_gpas.mean(axis=0)))