# Iterated function system (IFS)
... are a method of constructing fractals. Those fractals can be of any number of dimensions, but are commonly computed and drawn in two-dimensional space. For that, we can use a method called "Chaos game".

Method
---------------------

Let (x0, y0) be an arbitrary starting point. Let S be a finite set, which elements are functions, that are linear (more generally affinite) transformations. To get the next point, we apply one of the those functions chosen randomly from a list of coresponding probabilities.
In this project I am going to fix a starting point to be (0, 0)

Example
---------------------

We create and use Ifs class:

```python

 fractal = Ifs(list_of_transformations, list_of_probabilities)
      
```

```python

 sierpinski_triangle = Ifs([lambda x, y: (.5 * x, .5 * y),
                            lambda x, y: (.5 * x + .5, .5 * y + .5),
                            lambda x, y: (.5 * x + 1, .5 * y)],
                            [1,1,1])
```

Each transformation can be represented as:

![f1](https://latex.codecogs.com/png.image?\dpi{110}%20\bg_white%20f_{1}\begin{pmatrix}x%20\\%20y\end{pmatrix}%20=%20\begin{pmatrix}\frac{1}{2}%20&%200%20\\0%20&%20\frac{1}{2}%20\\\end{pmatrix}\begin{pmatrix}x%20\\%20y\end{pmatrix})
