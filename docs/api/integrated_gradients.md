# Integrated Gradients

Integrated Gradients is a visualization technique resulting of a theoretical search for an 
explanatory method that satisfies two axioms, Sensitivity and Implementation Invariance
(Sundararajan et al[^1]). 

> We consider the straightline path (in $R^n$) from the baseline $\bar{x}$ to the input $x$, and compute the 
> gradients at all points along the path. Integrated gradients are obtained by cumulating these 
> gradients.
>
> -- <cite>[Axiomatic Attribution for Deep Networks (2017)](https://arxiv.org/abs/1703.01365)</cite>[^1]

Rather than calculating only the gradient relative to the image, the method consists of averaging
the gradient values along the path from a baseline state to the current value. The baseline state 
is often set to zero, representing the complete absence of features.

More precisely, with $\bar{x}$ the baseline state, $x$ the image, $c$ the class of interest and
$S_c$ the unormalized class score (layer before softmax). The Integrated Gradient is defined as

$$IG(x) = (x - \bar{x}) \cdot \int_0^1{ \frac { \partial{S_c(\tilde{x})} } { \partial{\tilde{x}} } 
            \Big|_{ \tilde{x} = \bar{x} + \alpha(x - \bar{x}) } d\alpha }$$

Note that computing the Integral of Integrated Gradient is often (not always[^2]) intractable in 
practice, but it could be approximated by regularly calculating points along the straightline path.

!!! tip
    In order to approximate from a finite number of steps, the implementation here use the
    Trapezoidal rule[^3] and not a left-Riemann summation, which allows for more accurate results 
    and improved performance. (see the paper below for a comparison of the methods[^2]).

## Examples

```python
from xplique.methods import IntegratedGradients

# load images, labels and model
# ...

method = IntegratedGradients(model, steps=50, baseline_value=0.0)
explanations = method.explain(images, labels)
```

Using Integrated gradients method on the layer before softmax (as recommended).
```python
from xplique.methods import IntegratedGradients

"""
load images, labels and model
...

#Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, None, 512)     401920     
_________________________________________________________________
dense_2 (Dense)              (None, None, 10)      5130      
_________________________________________________________________
activation_1 (Activation)    (None, None, 10)      0         
=================================================================
Total params: 407,050
Trainable params: 407,050
Non-trainable params: 0
"""

# model target layer is dense_2, before activation
# leaving baseline_value as default (0.0)
method = IntegratedGradients(model, output_layer_index=-2, steps=50)
explanations = method.explain(images, labels)
```

{{xplique.methods.integrated_gradients.IntegratedGradients}}

[^1]: [Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365)
[^2]: [Computing Linear Restrictions of Neural Networks](https://arxiv.org/abs/1908.06214)
[^3]: [Trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)