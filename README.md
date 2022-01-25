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

![f1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%20%5Cbg_white%20f_%7B1%7D%5Cbegin%7Bpmatrix%7Dx%20%5C%5C%20y%5Cend%7Bpmatrix%7D%20=%20%5Cbegin%7Bpmatrix%7D%5Cfrac%7B1%7D%7B2%7D%20&%200%20%5C%5C0%20&%20%5Cfrac%7B1%7D%7B2%7D%20%5C%5C%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7Dx%20%5C%5C%20y%5Cend%7Bpmatrix%7D)
![f2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%20%5Cbg_white%20f_%7B2%7D%5Cbegin%7Bpmatrix%7Dx%20%5C%5C%20y%5Cend%7Bpmatrix%7D%20=%20%5Cbegin%7Bpmatrix%7D%5Cfrac%7B1%7D%7B2%7D%20&%200%20%5C%5C0%20&%20%5Cfrac%7B1%7D%7B2%7D%20%5C%5C%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7Dx%20%5C%5C%20y%5Cend%7Bpmatrix%7D%20&plus;%20%5Cbegin%7Bpmatrix%7D%5Cfrac%7B1%7D%7B2%7D%20%5C%5C%20%5Cfrac%7B1%7D%7B2%7D%5Cend%7Bpmatrix%7D)
![f3](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%20%5Cbg_white%20f_%7B3%7D%5Cbegin%7Bpmatrix%7Dx%20%5C%5C%20y%5Cend%7Bpmatrix%7D%20=%20%5Cbegin%7Bpmatrix%7D%5Cfrac%7B1%7D%7B2%7D%20&%200%20%5C%5C0%20&%20%5Cfrac%7B1%7D%7B2%7D%20%5C%5C%5Cend%7Bpmatrix%7D%5Cbegin%7Bpmatrix%7Dx%20%5C%5C%20y%5Cend%7Bpmatrix%7D%20&plus;%20%5Cbegin%7Bpmatrix%7D1%20%5C%5C%200%5Cend%7Bpmatrix%7D)
