$$
\begin{align*}
\min_W \max_{v_k,u_k}& \quad \frac{1}{K} \sum_{k=1}^K(y_k - (x_k^m + v_k)^TW(x_k^n+u_k))^2\\
s.t. &\quad ||u_k||^2_2\leq\delta^2,\quad ||v_k||^2_2\leq\delta^2, \quad k =1,...,K.
\end{align*}
$$
where W is a weight matrix.
Derive update rules to estimate W and report classification accuracy for 10-fold cross-validation

let's denote $x_k^m$ as $x_k$ and $x_k^n$ as $z_k$.

solve the problem with respect to $v_k$.
$$\max_{v_k}(y_k - (x_k + v_k)^TW(z_k+u_k))^2 = \max_{v_k}
(y_k - (x_k + v_k)^Tw_R)^2$$
There is exactly the same problem as in the first task, so
$$v_k^* = \lambda \frac{w_R}{||w_R||_2}\delta = -sign(y_k-x_k^Tw_R)\delta\frac{w_R}{||w_R||_2}$$

The same for $u_k$
$$\max_{u_k}(y_k - (x_k + v_k)^TW(z_k+u_k))^2 = \max_{u_k}
(y_k - w_L^T(z_k+u_k))^2 =\\ \max_{u_k}
(y_k - (z_k+u_k)^Tw_L)^2$$

$$u_k^*=-sign(y_k-z_k^Tw_L)\delta\frac{w_L}{||w_L||_2}$$

For W
$$
\min_W \max_{v_k,u_k} \quad \frac{1}{K} \sum_{k=1}^K(y_k - (x_k + v_k)^TW(z_k+u_k))^2 =\\ \min_W \quad \frac{1}{K} \sum_{k=1}^K(y_k - (x_k + v_k^*)^TW(z_k+u_k^*))^2
$$
denote X as $[x_1 + v_1^*,...,x_K+v_K^*]$ and Z as $[z_1 + u_1^*,...,z_K+u_K^*]$
$\sum_{k=1}^K(y_k - (x_k + v_k^*)^TW(z_k+u_k^*))^2 = ||y -diag(X^TWZ)||_2^2$

I did not find whether how to diff the diag function or more simpler matrix form. So:

$$W = \argmin_W ||y -diag(X^TWZ)||_2^2$$

result:

1) 
$$
    w_L =W^{tT}(x_k + v_k^t)\\
    u_k^{t+1}=-sign(y_k-z_k^Tw_L)\delta\frac{w_L}{||w_L||_2}
$$
2) 
$$
    w_R =W^t(z_k+u_k)\\
    v_k^{t+1} = -sign(y_k-x_k^Tw_R)\delta\frac{w_R}{||w_R||_2}
$$
3) 
$$
    X = [x_1 + v_1^{t+1},...,x_K+v_K^{t+1}] \quad Z = [z_1 + u_1^{t+1},...,z_K+u_K^{t+1}]\\
    W^{t+1} = \argmin_W ||y -diag(X^TWZ)||_2^2
$$