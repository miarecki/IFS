# Iterated function system (IFS)
... are a method of constructing fractals. Those fractals can be of any number of dimensions, but are commonly computed and drawn in two-dimensional space. For that, we can use a method called "Chaos game".

Method
---------------------

Let (x<sub>0</sub>, y<sub>0</sub>) be an arbitrary starting point (usually fixed to be (0, 0)). Let S be a finite set, which elements are functions T, that are linear (more generally affine) transformations. Let P be a list of corresponding probabilities to each function from S. To get the next point, we apply a function T<sub>i</sub> chosen randomly with a probability P<sub>i</sub>.  


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

They are chosen with an equal probability.  

```python

 sierpinski_triangle.draw(iterations = 100000, save = 'sierp_triangle.png')  
 
```  

Choosing 100000 iterations, we get this picture:  
![sierpinski](images/sierp_triangle.png?raw=true)
