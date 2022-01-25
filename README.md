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

![f1](<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;f_{1}\begin{pmatrix}x&space;\\&space;y\end{pmatrix}&space;=&space;\begin{pmatrix}\frac{1}{2}&space;&&space;0&space;\\0&space;&&space;\frac{1}{2}&space;\\\end{pmatrix}\begin{pmatrix}x&space;\\&space;y\end{pmatrix}" title="\bg_white f_{1}\begin{pmatrix}x \\ y\end{pmatrix} = \begin{pmatrix}\frac{1}{2} & 0 \\0 & \frac{1}{2} \\\end{pmatrix}\begin{pmatrix}x \\ y\end{pmatrix}" />)
