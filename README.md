> Computers have been able to add numbers for more than 100 years. But today we're going to add numbers the hard way: by training a neural network to do it. This tutorial will teach you some Python Machine Learning concepts in the context of a very simple problem: adding 1 plus 1.

Based on https://www.freecodecamp.org/news/how-to-add-two-numbers-using-machine-learning/.

---

```shell
make install
```

```shell
make run
```

```python
test_input = tf.constant([[1, 2], [0.3, 0.4]])
predicted_y = model.predict(test_input)
# [[3.012106 ] 
#  [0.6955168]]
```
