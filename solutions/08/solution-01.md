## Solution - Notebook 07 - Exercise 01

The coefficients needed for bilinear filtering can be estimated using the following system of linear equations

$$
\left[
\begin{array}{cccc}
1 & x_1 & y_1 & x_1 y_1 \\
1 & x_1 & y_2 & x_1 y_2 \\
1 & x_2 & y_1 & x_2 y_1 \\
1 & x_2 & y_2 & x_2 y_2 
\end{array}
\right]
\left(
\begin{array}{c}
a_0 \\
a_1 \\
a_2 \\
a_3 
\end{array}
\right)
=
\left(
\begin{array}{c}
f(Q_{11})\\
f(Q_{12}) \\
f(Q_{21}) \\
f(Q_{22}) 
\end{array}
\right)
$$