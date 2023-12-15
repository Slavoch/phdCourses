
$$
\begin{align*}
\min_w \max_{e_k} &\sum^K_{k=1}(y_k - (x_k + e_k)^Tw)^2\\

s.t. & ||e_k||^2_2\leq \delta^2, k =1...K
\end{align*}
$$
Simplify the above problem to an unconstrained optimization problem. Solve the simplified
problem and report the classification accuracy for 10-fold cross-validation.

$$

\begin{align*}
\mathcal{L} &= \sum^K_{k=1}(y_k - (x_k + e_k)^Tw)^2 + \alpha(||e_k||^2_2 - \delta^2)\\

\frac{\partial\mathcal{L}}{\partial e_k}&=2w(y_k - w^T(x_k + e_k)) + 2 \alpha e_k = 0\\

& => w(scalar) +\alpha e_k=0\\
& => e_k  \text{ is parallel to w}\\
& => e_k =\lambda w
\end{align*}
$$
As far as convex function reach its maxima on the boundary (except constant functions) $||e_k||^2_2 = \delta^2$
=> $e_k = \lambda \frac{w}{||w||_2}\delta$ for $\lambda \in\{1,-1\}$

to maximize this function $(y_k - (x_k + e_k)^Tw)^2 = (b - e_k^Tw)^2 = (b - \lambda \delta|w|_2)^2$ it is clear that second term should have the sign as $(-b)$ => $\lambda = \frac{-b}{|b|}$

$$
(b - \lambda \delta|w|_2)^2 =(b + \frac{b}{|b|} \delta|w|_2)^2 = b^2 +2|b|\delta||w||_2 + ||w||_2^2 = \\
=(|b|+\delta||w||_2)^2 = (|y_k - x_k^Tw|+\delta||w||_2)^2\\

$$

Back to init problem

$$
\min_w \max_{e_k} \sum^K_{k=1}(y_k - (x_k + e_k)^Tw) =\min_w \sum^K_{k=1}(|y_k - x_k^Tw|+\delta||w||_2)^2
$$
rewrite to equivalent problem (because all terms are positive)
$$
\min_w \sum^K_{k=1}(|y_k - x_k^Tw|+\delta||w||_2)= \min_w (||y - Xw||_1+\delta K ||w||_2)
$$

I tryed to do something but it did not become better:
$$
\frac{\partial f}{\partial w} = X^T sign(y - Xw^*) +\delta \frac{w}{||w||_2} = 0\\
 \delta \frac{w}{||w||_2} = - X^T sign(y - Xw^*) = - X^T S\\
|\delta \frac{w}{||w||_2}|_2=\delta => |X^T S|_2 = \delta
$$
So i came with the following:
$$
\delta \frac{w^*}{||w^*||_2} = - X^T sign(y - Xw^*)\\
|X^T sign(y - Xw^*)|_2 = \delta
$$
Did not come to closed form solution