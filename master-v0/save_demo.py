import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


class Net:
    def __init__(self):
        self.sess = tf.Session()
        self.x = tf.placeholder(tf.float32, (None, 4), name="a")
        self.y_ = tf.placeholder(tf.float32, (None, 2), name="label_d")
        self._build_net()
        self.learning_rate = 0.001
        self.loss = tf.losses.mean_squared_error(self.y_, self.predict)
        self.train_op = tf.train.MomentumOptimizer(self.learning_rate, momentum=0.9).minimize(self.loss)
        self.sess.run(tf.global_variables_initializer())

    def _build_net(self):
        with tf.name_scope("FC"):
            fc1 = tf.layers.dense(self.x, 20, activation=tf.nn.relu, name="fc1")
            # fc2 = tf.layers.dense(fc1, 20, activation=tf.nn.relu, name="fc2")
            self.predict = tf.layers.dense(fc1, 2, name="predict")

    def learn(self, x_batch, y_batch):
        _, batch_loss, batch_predict = self.sess.run([self.train_op, self.loss, self.predict],
                                                     feed_dict={self.x: x_batch, self.y_: y_batch})
        return batch_loss, batch_predict


def plt_function(dist3, predict_3):
    dist3_1 = dist3[:, 0]
    dist3_2 = dist3[:, 1]
    predict_dist3_1 = predict_3[:, 0]
    predict_dist3_2 = predict_3[:, 1]
    range_list = np.linspace(1, len(dist3_1), len(dist3_1))

    fig1 = plt.figure('fig1')
    plt.plot(range_list, dist3_2, color="blue", linewidth=1.0, linestyle="-", label="dist3_2")
    plt.plot(range_list, predict_dist3_2, color="red", linewidth=2.0,  label="pred3_2")
    plt.legend(loc="upper left")

    fig2 = plt.figure('fig2')  # 定义一个图像窗口
    plt.plot(range_list, dist3_1, color="blue", linewidth=1.0, linestyle="-", label="dist3_1")
    plt.plot(range_list, predict_dist3_1, color="red", linewidth=2.0, label="pred3_1")
    plt.legend(loc="upper left")

    fig1.show()
    fig2.show()


def main():
    list_a = np.random.random((1000, 2))
    list_b = np.random.random((1000, 2))
    label_d = list_a - list_b
    net = Net()
    epochs = 2
    batch_size = 32
    train_loss = []

    for e in range(epochs):
        print("epoch:", e)
        for i in range(len(list_a)//batch_size):
            indices = np.random.choice(len(list_a), size=batch_size)
            x_batch = np.concatenate([list_a[indices, :], list_b[indices, :]], axis=-1)

            y_batch = label_d[indices, :]
            loss, predict = net.learn(x_batch, y_batch)
            train_loss.append(loss)
            # if (i - len(list_a)//batch_size) >= -1:
            plt_function(y_batch, predict)
        mean_loss = np.mean(train_loss)
        print('mean loss', mean_loss)


if __name__=="__main__":
    main()