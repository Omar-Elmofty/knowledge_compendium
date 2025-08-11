# Control Barrier Functions

This section of the notes discusses the theory behind Control Barrier functions, and how they could be used to design a safe controller. A safe controller in this context is a controller that guarentees that the command sequence stays within a safe region that ensures that the overall system is safe.

Credit for some of the learnings in this section goes to Jason Choi and his [Introduction to Control Lyapunov Functions and Control Barrier Functions](https://www.youtube.com/watch?v=_Tkn_Hzo4AA) video.

In this section we will discuss the theory behind the following, with examples:
1. Lyapunov Stability Theorm
2. Nagumo's Invariance Principle
3. Control Lyapunov Functions
4. Control Barrier Functions
5. The CLF-CBF-QP controller
6. Example for a diff drive vehicle
