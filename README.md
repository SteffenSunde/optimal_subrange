
Totally bikeshedding the process of choosing a subset of 
steps outputted from the finite element software [Abaqus](https://www.3ds.com/products-services/simulia/products/abaqus/abaquscae/).

The problem consists of choosing k numbers of a given list, maximising spread. This can be translated into maximising the minimum distance between the points in the output. 

In most cases, the input is not large, and a brute force method is good enough. But an algorithm in polynomial time is possible through [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) (DP).

The problem is solved using a really ugly implementation of bottom-up DP with "parent pointers" [1]. The subproblem can be written as

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{W}(A,f)&space;=&space;(T,\bar{f})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{W}(A,f)&space;=&space;(T,\bar{f})" title="\mathcal{W}(A,f) = (T,\bar{f})" /></a>

where $X_{i,j}$ is the solution for choosing $j$ elements from the first $i$ items of the list (ordered), and $A_i$ is the ith number of the input sequence.

## TODO
 - [ ] Write numpy version
 - [ ] Moar testing


## References
 - [1] [MIT excellent lectures on DP by Erik Demaine](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-19-dynamic-programming-i-fibonacci-shortest-paths/)
