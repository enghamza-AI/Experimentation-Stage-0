#Self Improving Predictor

#training data

hours_data = [1, 2, 3, 4, 5]
marks_data = [35, 40, 50, 55, 65]

#initialize slope m and bias randomly

m = 0.0
b = 0.0

#hyperparameters
learning_rate = 0.01
num_epochs = 100

#Training loop

for epoch in range(num_epochs):
    total_loss = 0

    for x, y in zip(hours_data, marks_data):

        pred = m * x + b

        error = pred - y

        total_loss += error ** 2

        m = m - learning_rate * (2 * error * x)
        b = b - learning_rate * (2 * error)

    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}, Loss: {total_loss:.2f}, m: {m:.3f}, b: {b:.3f}")


test_hours = [6, 7, 8]
for h in test_hours:
    predicted_marks = m * h + b
    print(f"studied {h} hours -> predicted Marks: {predicted_marks:.2f}")