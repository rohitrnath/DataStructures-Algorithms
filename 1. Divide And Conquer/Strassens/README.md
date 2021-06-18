# Strassen's Matrix Multiplication

* Two matrix can multiply only when the number of columns of first matrix are equal to the number of rows of second matrix
* The resultant martrix have a dimentsion of number of rows rows in first matrix and number of columns in second matrix.

$$
\begin{bmatrix}
\ A_{11} & \ A_{12} \\
\ A_{21} & \ A_{22}
\end{bmatrix}
*
\begin{bmatrix}
\ B_{11} & \ B_{12} \\
\ B_{21} & \ B_{22}
\end{bmatrix}
=
\begin{bmatrix}
\ C_{11} & \ C_{12} \\
\ C_{21} & \ C_{22}
\end{bmatrix}
$$

## Psudo-code for normal matrix multiplication
* Two for loops require to access all the elements.
* One more for loop require to assign value for each element in the resulting matrix 'C'.
* Time taken for multiplting two matrices in $O(n^2)$.
```c++
for( i=0; i<m; i++)
{
    for( j=0; j<m; j++)
    {
        C[i][j] = 0;
        for( k=0; k<n; k++)
        {
            C[i][j] += A[i][k] * B[k][i]
        }
    }
}
```

## Strassen's Logic

* It's a *Divide And Conquer* Stratergy.
* In this strategy, big problems are divide into small sub problems and solve.






