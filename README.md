# Convex Hull Analyzer: Brute Force (O(n^3)) vs. Graham Scan (O(nlogn))

This tool provides a theoretical and experimental comparison of two algorithms that compute the smallest convex polygon (Convex Hull) enclosing a set of random points in a 2D surface.

##  Purpose
* To see how the theoretical complexities of Brute Force and Graham Scan translate to real execution times.
* To visualize the stark performance difference between the two algorithms on larger datasets.


## Result
![vision](pic.png)


## Algorithm Logic (Briefly):
* Brute Force: Treats every pair of points as a candidate edge and checks whether all remaining points fall on the same side of that line.
* Graham Scan: Sorts points by polar angle relative to the lowest point and uses a stack to eliminate any that introduce a concave turn.

## Installation & Usage
The project is designed to run as a single Python file.

1.  Install:
    ```bash
    pip install numpy matplotlib
    ```
2.  Run:
    ```bash
    python algoproje.py
    ```



