import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Initialize weights and biases
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))
        self.lr = learning_rate

    # Sigmoid activation
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    # Derivative of sigmoid
    def sigmoid_derivative(self, a):
        return a * (1 - a)

    # Forward pass
    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

    # Backward pass
    def backward(self, X, y, output):
        m = X.shape[0]
        # Output layer error
        error_output = output - y
        dW2 = np.dot(self.a1.T, error_output * self.sigmoid_derivative(output)) / m
        db2 = np.sum(error_output * self.sigmoid_derivative(output), axis=0, keepdims=True) / m

        # Hidden layer error
        error_hidden = np.dot(error_output * self.sigmoid_derivative(output), self.W2.T)
        dW1 = np.dot(X.T, error_hidden * self.sigmoid_derivative(self.a1)) / m
        db1 = np.sum(error_hidden * self.sigmoid_derivative(self.a1), axis=0, keepdims=True) / m

        # Update weights and biases
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2

    # Training function
    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            if (epoch + 1) % 100 == 0:
                loss = np.mean((y - output) ** 2)
                print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")

    # Prediction
    def predict(self, X):
        output = self.forward(X)
        return (output > 0.5).astype(int)


# Example usage: XOR problem
if __name__ == "__main__":
    # XOR dataset
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])

    # Create and train the network
    nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1, learning_rate=0.5)
    nn.train(X, y, epochs=1000)

    # Predictions
    predictions = nn.predict(X)
    print("\nPredictions:")
    for inp, pred in zip(X, predictions):
        print(f"{inp} -> {pred[0]}")