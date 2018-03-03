import theano
import numpy
import theano.tensor as T
import matplotlib.pyplot as plt


class Layer(object):
    def __init__(self, inputs, in_size, out_size, activation_function=None):
        self.W = theano.shared(numpy.random.normal(0, 1, (in_size, out_size)))
        self.b = theano.shared(numpy.zeros(out_size) + 0.1)
        self.Wx_plus_b = T.dot(inputs,self.W) + self.b
        self.activation_function = activation_function
        if activation_function is None:
            self.out_puts = self.Wx_plus_b
        else:
            self.out_puts = self.activation_function(self.Wx_plus_b)

x_data = numpy.linspace(-1, 1, 300)[:, numpy.newaxis]
noise = numpy.random.normal(0, 0.05, x_data.shape)
y_data = numpy.square(x_data) - 0.5 + noise

x = T.dmatrix('x')
y = T.dmatrix('y')
l1 = Layer(x, 1, 10, T.nnet.relu)
l2 = Layer(l1.out_puts, 10, 1, None)
cost = T.mean(T.square(l2.out_puts - y))

gW1, gb1, gW2, gb2 = T.grad(cost, [l1.W, l1.b, l2.W, l2.b])
learning_rate = 0.05
train = theano.function(inputs=[x, y], outputs=cost, updates=[(l1.W, l1.W - learning_rate*gW1), \
                                                                 (l1.b, l1.b - learning_rate*gb1), \
                                                                 (l2.W, l2.W - learning_rate*gW2), \
                                                                 (l2.b, l2.b - learning_rate*gb2)])

predict = theano.function(inputs=[x],outputs=l2.out_puts)

flg = plt.figure()
ax = flg.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()
plt.axis([-1.5,1.5,-0.6,0.6])           # 指定坐标轴的显示范围横坐标-1.5到1.5，纵坐标为-0.6到0.6
plt.show()

for i in range(1000):
    err = train(x_data, y_data)
    print(err)
    if i%50==0:
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = predict(x_data)
        lines = ax.plot(x_data, prediction_value,'r', lineWidth=5)
        plt.pause(0.1)