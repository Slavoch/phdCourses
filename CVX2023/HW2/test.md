error1 and error2 are significantly different because $U_1$ and $U_2$ are different matrices with small scale factor.
As far as we approximate $Y_1$ with $U_1V_1^T$ s.t. $U_1 =U_2$ the scale factor of $U_1V_1^T$ is containce in $V_1$ and $U_1$ ramaince ralativly small in terms of norm.
So then we compare $U_1 =U_2$ the distance error is small because of small scale factor of $U_1$ and by the same logic $U_2$.

So if we force $U$ be orthogonal we could resolve that issue.

$$
\begin{align*}
\min \quad & \frac{1}{2} ||Y_1 - U_1V_1^T||_F^2 + \frac{1}{2}||Y_2 - U_2V_2^T||_F^2\\
s.t \quad & U_1^TU_1 = I\\
&U_2^TU_2 = I\\
&U_1^TU_2 = I\\

\end{align*}
$$