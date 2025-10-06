# Attention is all you need

This is a brief article that explains Attention (famously used in the GPT architecture used by chatGPT). This is based on the [Attention is all you need Paper](https://arxiv.org/abs/1706.03762) written in 2017, also from the [3Blue1Brown Attention video](https://www.youtube.com/watch?v=eMlx5fFNoYc&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=7), along with [Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy) video [Let's build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY).


## Attention is a communication mechanism

Attention is most famously in the GPT architecture, but in essence it is a **Communication Mechanism** between nodes of a *Directed Graph*.

If you're unfamiliar with what a [directed graph](https://en.wikipedia.org/wiki/Directed_graph) is, it's a data structure consisting of nodes connected by edges that have a direction. See below diagram for illustration.

![directed_graph](../diagrams/exported/directed_graph.png)


So Attention basically provides a way for nodes in this directed graph to communicate. You may ask why?

Let's consider the classic example where you have a sentence that is composed of words, for example *The sky is blue*. As humans we already know that *blue* here is referring to the *sky*. Imagine now that you represented this sentence as a directed graph, having a node for every word, then the relationship between the words *sky* and blue *blue* can be represented by passing information between the nodes of the directed graph.

In addition, attention has no notion of space (or where each of the nodes is located relative to the others). It is mainly way for each of the nodes to communicate information between each other. In the context of LLMs, a sentence will be broken down into tokens where tokens need to communicate with each other in order to pass information relating to context (an adjective needs to communicate with the noun it is describing for example). This communication is directional since only previous words can impact coming words. Here is an illustration of the directed graph that representing a sentence:

![sentence_directed_graph](../diagrams/exported/sentence_directed_graph.png)


## Attention Formulation

The formulation of attention from the paper can be described as:

$$
Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V
$$

Ok let's break this down in very simple terms.


![attention](../diagrams/exported/attention.png)

## Self vs. Cross Attention

Self attention means that words of the same sentence are internally passing information from each other. There is no external data source (like video or voice) where information passing is needed.

On the contrary, cross attention is where you have information passing from a datasource to a different data source. The classic example is translating a sentence from one language to another, here you'd want information from the sentence with language A to flow to the sentence with language B.


