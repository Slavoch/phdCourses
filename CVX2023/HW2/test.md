$$
\begin{align*}
y_k(tr(W^TX_k) + b) - 1 & \geq 0\\
y_k(tr(W^TX_k) + b) - 1  -p_k^2 & = 0\\
\end{align*}
$$

denote $g_k =y_k(tr(W^TX_k) + b) - 1$ and rewrite problem

$$
\begin{align*}
\min_{W,b} \quad & \frac{1}{2}||W||_F^2\\
st. \quad & g_k -|p_k| = 0
\end{align*}
$$

$$
\begin{align*}
\mathcal{L} = \frac{1}{2}||W||_F^2 + \frac{\alpha}{2}||g - abs(p) + u||^2_2
\end{align*}
$$

ADMM:
$$
\begin{align*}
W^{k+1} &= \argmin_W\mathcal{L}(W,b^k,u^k,p^k)\\
    b^{k+1} &= \argmin_b\mathcal{L}(W^{k+1},b,u^k,p^k)\\
p^{k+1} &= \argmin_b\mathcal{L}(W^{k+1},b^{k+1},u^k,p)\\
u^{k+1} &= u^k + g^k-abs(p^{k+1})\\
\end{align*}
$$

Missing elements:
Consider $tr(W^TX) = \sum W_{ij}X_{ij}$ to consider only existing elements I substituted $X_{ij} = 0$ where pixel is missing. We should minimize only such $W_{ij}$ that partisipated in prediction so I substituted $||W||^2_F$ with $||W \circ \Omega_{mean}||^2_F$ where $ \Omega_{mean} = \sum \Omega_k/K$
