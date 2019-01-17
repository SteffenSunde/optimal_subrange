# optimal_subrange

Totally bikeshedding the process of choosing a subset of 
steps outputted from the finite element software [Abaqus](https://www.3ds.com/products-services/simulia/products/abaqus/abaquscae/).

The problem consists of choosing k numbers of a given list, maximising spread. This can be translated into maximising the minimum distance between the points in the output. 

In most cases, the input is not large, and a brute force method is good enough. But an algorithm in polynomial time is possible through [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) (DP).

The problem is solved using a really ugly implementation of bottom-up DP with "parent pointers" [1]. The subproblem can be written as

<a href="https://www.codecogs.com/eqnedit.php?latex=$$X_{i,j}&space;=&space;\max_{\substack{i=0..k&space;\\&space;j=i..n}}\{\min\limits_{k=0..j}(X_{i-1,k},&space;A_i&space;-&space;A_k)\}$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$X_{i,j}&space;=&space;\max_{\substack{i=0..k&space;\\&space;j=i..n}}\{\min\limits_{k=0..j}(X_{i-1,k},&space;A_i&space;-&space;A_k)\}$$" title="$$X_{i,j} = \max_{\substack{i=0..k \\ j=i..n}}\{\min\limits_{k=0..j}(X_{i-1,k}, A_i - A_k)\}$$" /></a>

where $X_{i,j}$ is the solution for choosing $j$ elements from the first $i$ items of the list (ordered), and $A_i$ is the ith number of the input sequence.

## TODO
 - [ ] Write numpy version
 - [ ] Moar testing


## References
 - [1] [MIT excellent lectures on DP by Erik Demaine](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-19-dynamic-programming-i-fibonacci-shortest-paths/)
