# Generative Pre-trained Transformer (GPT)

Resources:
[Attention is all you need](https://arxiv.org/abs/1706.03762): The original paper about Attention ..etc.
[3blue1brown series about DL](https://www.youtube.com/watch?v=LPZh9BOjkQs&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=5)
[Andrej Karpathy DL lectures](https://karpathy.ai/zero-to-hero.html)


What is the GPT in the most famous chatGPT:


The transformer architecture used in GPT is
a significant advancement over previous approaches to NLP,
such as RNN and CNN. I

Steps for training a GPT:

1. Pretraining: Training on a very large data set
2. Reinforcement learing with human feedback (RLHF): Use feedback to tune performance


Previously RNNs where very popular , but they were sequential and were hard to parallelize and improve.
GPTs. However, GPTs use a large portion of text into the transformer, which can then be parallelized.


## How does a chatbot works

1. First the text is split into tokens, these are words or parts of a word that have meaning associated with it. If tokens are coming from images or sound, then they could be chunks of that image, or bits of that sound.
2. Each one of the tokens is associated with a vector that's in a high dimensional space, it represents the meaning of that word.
3. Tokens from the sentence are passed through an attention block.
4. After the attention block you go through a multilayer perception feed-forward block.
5. Repeat steps 3 & 4


- The model has a pre-defined vocabulary.


First the input as text is passed to the embedding matrix $W_E$ which is a mapping from every word to a vector in the embedding space. Usually the direction of the embedding vector entails its meaning of the word. Also, difference vectors between similar words like (man - woman) and (king - queen) will be very similar. Hence, for example you could determine the word queen in the embedding space by taking $queen = king - (man - woman)$


Softmax with temperature: You add T to the softmax formulation in order to impact how softmax behaves. T will make softmax give more weight to lesser values, or not.



Tiny shakespere dataset for training transformers https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt


Andrej Kaparathy nanoGPT, good repo for learning how to train a gpt https://github.com/karpathy/nanoGPT

