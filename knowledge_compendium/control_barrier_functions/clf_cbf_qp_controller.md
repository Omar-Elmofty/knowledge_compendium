# CLF CBF QP Controller


### Control Affine System
Before we jump into Control Lyapunov Functions (CLFs), we first must establish what a Control Affine system is:

$$
\dot{x} = f(x) + g(x)u
$$

This is is basically it is a system $\dot{x} = f(x, u)$ with the control input $u$, but the the $u$ factoring in linearly in the system. 

Many dynamical systems can be expressed as a control affine system, and expressing the system as a control affine system makes the formulation of the problem much simpler.
