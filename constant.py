import tensorflow as tf

a = tf.constant([5])
b=tf.constant([10])
c= tf.constant([2])
d = a*b+c

sess = tf.Session()
result = sess.run(d)
print(result)

# BOOL
# var = tf.constant([10,20,30,40,50] , dtype=bool)