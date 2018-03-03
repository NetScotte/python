import numpy as np
import theano.tensor as T
import theano
import pickle
import matplotlib.pyplot as plt


def compute_accuracy(y_target, y_predict):
    correct_prediction = np.equal(y_predict, y_target)
    accuracy = np.sum(correct_prediction) / len(correct_prediction)
    return accuracy

rng = np.random
N = 400
feats = 784

D = (rng.randn(N, feats), rng.randint(size=N, low=0, high=2))
x = T.dmatrix('x')
y = T.dvector('y')
W = theano.shared(rng.randn(feats), name='W')
b = theano.shared(0.1, name='b')
p_1 = T.nnet.sigmoid(T.dot(x, W) + b)
prediction = p_1 > 0.5
xe = -y*T.log(p_1) - (1-y)*T.log(1 - p_1)
cost = xe.mean() + 0.01*(W**2).sum()
gW, gb = T.grad(cost, [W,b])

learning_rate = 0.1
train = theano.function(inputs=[x, y], \
                        outputs=[prediction, xe.mean()],\
                        updates=[(W, W-learning_rate*gW),(b, b-learning_rate*gb)])
predict = theano.function(inputs=[x], outputs=prediction)


for i in range(500):
    pred, err=train(D[0], D[1])



#     if i % 50 ==0:
#         print('cost',err)
#         print('accuracy',compute_accuracy(D[1],pred))
#
# print('target value for D')
# print(D[1])
# print('prediction on D:')
# print(pred)




#save W, b
#with open('gwgb','wb') as f:
#    model = [W.get_value(), b.get_value()]
#     pickle.dump(model, f)
#     print(model[0][:10])


# load W, b
# with open('gwgb','rb') as f:
#     model = pickle.load(f)
#     W.set_value(model[0])
#     b.set_value(model[1])





