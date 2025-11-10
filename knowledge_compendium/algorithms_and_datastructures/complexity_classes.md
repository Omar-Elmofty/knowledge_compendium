# Complexity Classes


A decision problem is a problem whose answer is binary (i.e., yes or no)

• Is some integer prime?

• Does some graph have a clique of size ?

• Can a specific Boolean formula be satisfied by an interpretation?

The theory of complexity for decision problems is a foundational field in computer science that involves the notion of Turing machines

Formally, define a complexity class to be the set of all problems that can be solved by a Turing machine using resources, or the union of multiple such sets

The resources of interest are computation time and memory (space)

The complexity classes of interest are defined in terms of decision problems because of their importance (both historical and technical) in theoretical computer science.

## P

P is the set of all decision problems that can be solved by a deterministic Turing machine with
worst-case (i.e., Big-O) polynomial time complexity.

Problems in P can typically be solved efficiently; they are often called tractable problems.

These are all the problems that could be solved in polynomial time:

$$
O(n^k)
$$

Where $k$ is a constant.


Examples of problems in P include:

• Determining if an integer is prime

• Decision version of linear programming (i.e., the optimization of a linear objective function,
subject to linear equality and linear inequality constraints).

## NP
The set of decision problems whose positive instances (i.e., cases with the answer “yes”) can be verified in polynomial time by a deterministic Turing machine

Trivially, P is included in NP (because finding a solution constitutes a proof)

NP is central in complexity theory because whether all problems in NP can in fact be solved in
polynomial time as well is unknown (P = NP?)

At present, many NP problems are “hard”, or intractable

## NP-Hard vs NP-Complete

NP-Hard is the set of all problems that are as hard as all other problems in NP or **harder**.


NP-Complete is the intersection of NP-Hard and NP. Intuitively, these are NP problems that are “at least as hard” as every other problem in NP.

![complexity classes](../images/complexity_classes.png)
