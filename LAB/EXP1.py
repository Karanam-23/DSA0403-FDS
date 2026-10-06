import numpy as np

student_scores = np.array([
    [85, 90, 78, 92],
    [88, 85, 90, 80],
    [92, 95, 85, 88],
    [75, 80, 82, 79]
])

subjects = ['Math', 'Science', 'English', 'History']

subject_averages = np.mean(student_scores, axis=0)

best_subject_index = np.argmax(subject_averages)
best_subject = subjects[best_subject_index]
best_average = subject_averages[best_subject_index]

print("Average scores for each subject:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {subject_averages[i]:.2f}")

print(f"\nThe subject with the highest average score is {best_subject} with an average of {best_average:.2f}.")
