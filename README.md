# optimal_subrange

Totally bikeshedding the process of choosing a subset of 
steps outputted from the finite element software [Abaqus](https://www.3ds.com/products-services/simulia/products/abaqus/abaquscae/). For nonlinear analyses, difficulties in FE solver convergence may output unevenly dispersed increments. If a selection of increments is to be selected to represent the time history, the selection should 

The problem consists of choosing k numbers of a given list, maximising spread. This can be translated into maximising the minimum distance between the points in the output. 

In most cases, the input is not large, and a brute force method is good enough. But an algorithm in polynomial time is possible through [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) (DP).

The problem is solved using a really ugly implementation of bottom-up DP with "parent pointers" [1]. The subproblem can be written as

<img src="https://render.githubusercontent.com/render/math?math=X_{i,j} = \max\limits_{i=0..k \\ j=i..n}\{\min\limits_{k=0..j}(X_{i-1,k}, A_i - A_k)\}">

where <img src="https://render.githubusercontent.com/render/math?math=$X_{i,j}"> is the solution for choosing k elements from the first i items of the list (ordered), and <img src="https://render.githubusercontent.com/render/math?math=$A_i$"> is the ith number of the input sequence.

Warning: This 

## Example

```python
import optimal_subrange.choose_subset as cs
frames = [0.0, 0.23, 0.61, 1.0]

subrange = cs.choose_subset(frames, 3)  # Returns [0.0, 0.61, 1.0]
```


## TODO
 - [ ] Write numpy version
 - [ ] Moar testing
 - [ ] Implement (quicker?) solution using binary search
 - [ ] Handle negative numbers


## References
 - [1] [MIT's excellent lectures on DP by Erik Demaine](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-19-dynamic-programming-i-fibonacci-shortest-paths/)
