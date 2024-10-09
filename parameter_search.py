from train_test import training, testing

# Диапазоны для подбора параметров
learning_rate_range = [i * 0.1 for i in range(1, 10)]
learning_epoch_range = [i for i in range(1, 11)]
hidden_nodes_range = [i for i in range(50, 751, 50)]

# Перебор параметров
for l_rate in learning_rate_range:
    for l_epochs in learning_epoch_range:
        for h_nodes in hidden_nodes_range:
            print(f'Обучение с параметрами: learning_rate={l_rate}, epochs={l_epochs}, hidden_nodes={h_nodes}')
            training(l_rate, l_epochs, h_nodes)
            testing(l_rate, l_epochs, h_nodes)
