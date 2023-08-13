import tensorflow as tf
import keras
from keras import layers


def main():
    # Prepare the data
    NUM_SAMPLES = 1000
    x_train = tf.random.uniform(shape=(NUM_SAMPLES, 2))
    print(x_train)

    y_train = x_train[:, 0] + x_train[:, 1]
    print(y_train)

    # Define the neural network
    model = keras.Sequential(
        [
            keras.Input(shape=(2,)),
            layers.Dense(8, activation="relu"),
            layers.Dense(1),
        ]
    )
    model.summary()

    # Compile the model
    model.compile(loss="mse", optimizer="adam")

    # Train the model
    model.fit(x_train, y_train, batch_size=32, epochs=100, verbose=1)

    # Test the model; print the values
    test_input = tf.constant([[1, 2], [0.3, 0.4]])
    predicted_y = model.predict(test_input)
    print(predicted_y)


main()
