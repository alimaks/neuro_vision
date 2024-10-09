from neural_network import NeuralNetwork
import numpy

path = 'results/weights/'  # Путь для сохранения весов

train_data_file = 'data/mnist_train.csv'  # Путь к тренировочным данным
test_data_file = 'data/mnist_test.csv'  # Путь к тестовым данным

# Неизменные параметры сети
input_nodes = 784
output_nodes = 10


def training(learning_rate, learning_epochs, hidden_nodes):

    nn = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    with open(train_data_file, 'r') as data_file:
        data_list = data_file.readlines()

    for i in range(learning_epochs):
        for record in data_list:
            all_data = record.split(',')
            inputs = (numpy.asarray(all_data[1:], dtype=float) / 255.0 * 0.99) + 0.01
            targets = numpy.zeros(output_nodes) + 0.01
            targets[int(all_data[0])] = 0.99
            nn.train(inputs, targets)

    nn.save(path)


def testing(learning_rate, learning_epochs, hidden_nodes):

    nn = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    nn.load(path)

    with open(test_data_file, 'r') as data_file:
        data_list = data_file.readlines()

    scorecard = []

    for record in data_list:
        all_data = record.split(',')
        correct_label = int(all_data[0])
        inputs = (numpy.asarray(all_data[1:]) / 255.0 * 0.99) + 0.01
        outputs = nn.query(inputs)
        label = numpy.argmax(outputs)

        scorecard.append(1 if correct_label == label else 0)

    accuracy = sum(scorecard) / len(scorecard)

    res_str = '{},{},{},{}'.format(learning_rate, learning_epochs, hidden_nodes, accuracy)
    with open('results/acc_results.txt', 'a') as f:
        f.write(res_str + '\n')
