# Linear Quadratic Control


Assuming that:
1. System is linear and deterministic
2. The setpoint is at the origin
3. The system model is as following:

$$
x^+ = Ax + Bu
$$

$$
y=Cx
$$

4. Assuming also that $C =I$, i.e. the system is fully observable.
5. We will be ignoring constraints on the input.


## Finite Horizon LQ control

> **Note**:   
> The constraints are the main feature that
> distinguishes MPC from the standard linear quadratic (LQ) control.


Let's now define the objective function $V$ that will measure the deviation from the origin (setpoint):

$$
V(x(0), u) = \frac{1}{2} \Sigma_{k=0}^{N-1} [x(k)^TQx(k)+u(k)^TRu(k)] + \frac{1}{2}x(N)^TP_fx(N)
$$

Subject to:

$$
x(k+1) = Ax(k)+Bu(k)
$$

The above objective has the following properties:
1. It is a function on the initial state $x(0)$ and the input sequence $u$, note that any intermediate state $x(k)$ can be derived by rolling out the inputs from $x(0)$ to timestep k
2. The tuning parameters are $Q$ and $R$, we also allow the final penalty state to be $P_f$ for generality (may desire a different behavior at the end). Choosing the values of $Q$ and $R$ is not always obvious and may require some extensive tuning. Increasing $Q$ in comparison to $R$ will make the system want to converge quickly to the setpoint at the expense of high inputs and vice versa.


We can then formulate the following optimal LQ control problem:

$$
min_u V(x(0), u)
$$

The Q, Pf , and R matrices often are chosen to be diagonal, but we do
not assume that here. We assume, however, that Q, Pf , and R are real
and symmetric; Q and Pf are positive semide®nite; and R is positive
de®nite. These assumptions guarantee that the solution to the optimal
control problem exists and is unique.


## Infinite Horizon LQ control (Linear Quadratic Regulator)



