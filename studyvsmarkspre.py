#study vs marks predictor

#training data
hours_data = [1, 2, 3, 4, 5]
marks_data = [35, 40, 50, 55, 65]

#calculate slope (m)
m = (marks_data[-1] - marks_data[0]) / (hours_data[-1] - hours_data[0])

#calculate bias (b)
b = marks_data[0] - m * hours_data[0]

#prediction function
def predict_marks(hours):
    return m * hours + b

#test prediction
study_hours = 6
predicted = predict_marks(study_hours)

print("studied hours:", study_hours)
print("predicted marks:", predicted)