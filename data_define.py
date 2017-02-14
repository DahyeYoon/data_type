import tensorflow as tf

ph = tf.placeholder(tf.float32, shape=[3,3])
var = tf.Variable([1,2,3,4,5], dtype=tf.float32)
const = tf.constant([10,20,30,40,50], dtype=tf.float32)
# these variables cannot be calculated  ==> because tf just makes graph
# session 에 싣기 전까지는 그래프만 그린 것. session에 싣고 run 을 해야 역행연산으로 input을 찾아, 연산할 수 있음
# print (ph)
# print (var)
# print (const)

# Open Session
sess = tf.Session()
# Run session
result =sess.run(const)
print(result)