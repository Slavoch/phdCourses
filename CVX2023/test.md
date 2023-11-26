## (a)
Solve the following optimization problem to find an orthogonal matrix U and a feature matrix, $X = [x_1, . . . , x_K]$, of size $R \times K$
$$
\begin{align*}
\min \quad  &||Y-UX||^2_F\\
\text{s.t.}\quad & U^TU = I_R\\
& X \geq 0 \quad X^T 1_r=1_k
\end{align*}\\
\begin{align*}\\
\min_U ||Y-UX||^2_F &= \min_U ||Y||^2_F +||UX||^2_F - 2\langle Y|UX\rangle = \\
& = \min_U  ||X||^2_F - 2trace(Y^TUX) =  \max_U trace(UXY^T)\\
XY^T &= A \Lambda B^T \\
\max_U trace(UXY^T) & = \max_U trace(UA \Lambda B^T) = \max_U trace(B^TUA \Lambda)\\
 & = \max_U \sum Q_{ij} * \sigma_{ij}=\max_U \sum Q_{ii} * \sigma_{ii} \\
\end{align*}\\
\text{Where $Q = B^TUA $ is orthogonal matrix with largest elements on diagonal =>}\\
\text{$Q$ is $I$}\\
\begin{align*}\\
B^TUA &= I\\
U^* &= BA^T
\end{align*}\\
\min_X ||Y-UX||^2_F\quad  X \geq 0 \quad X^T 1_r=1_k \\
\begin{align*}\\
\mathcal{L} & = \frac{1}{2}||UX  - Y||^2_F +trace(\Gamma X) + \lambda^T (X^T 1_r - 1_k)\\
\frac{\partial\mathcal{L}}{\partial x} &=U^T(UX-Y) + 1_r\lambda^T +\Gamma^T = 0\\
&\text{By complementary slackness if $\Gamma_{ij} = 0 => X_{ij} > 0$}\\
\frac{\partial\mathcal{L}}{\partial x} &=U^T(UX-Y) + 1_r\lambda^T = 0\\
& X = U^TY - 1_r\lambda^T\\
& X^T1_r = (Y^TU - \lambda1_r^T)1_r = Y^TU1_r - \lambda R = 1_k\\
& \lambda = (Y^TU1_r-1_k )(1/R)\\
& X = U^TY- 1_r\lambda^T = U^TY- 1_r(1_r^TU^TY-1_k^T )(1/R)=\\
& \quad =(I_r- \frac{1_r1_r^T}{R})U^TY-\frac{1_r1_k^T}{R}\\
& X^* =
\begin{matrix}
(I_r- \frac{1_r1_r^T}{R})U^TY-\frac{1_r1_k^T}{R} & \text{ if $X_{ij} > 0$}\\
0& \text{ if $X_{ij} = 0$}
\end{matrix}\\

\end{align*}\\
$$

