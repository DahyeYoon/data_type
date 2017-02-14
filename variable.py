import tensorflow as tf

var1 = tf.Variable([5])
var2 = tf.Variable([3])
var3 = tf.Variable([2])

var4 = var1*var2+var3
sess = tf.Session()
# Unlike constant, Variable must be initialized (그래야 값이 들어감)
init=tf.initialize_all_variables()
sess.run(init)
result =sess.run(var4)

print(result)