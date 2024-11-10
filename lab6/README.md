# MDP
# Objective.
To implement algorithms for finding the optimal policy in the Markov decision process (MDP) using Policy Iteration and MDP learning with unknown transition probabilities.
# Theory.
An MDP is described by the pentagon (S,A,P,γ,R)(S, A, P, \gamma, R)(S,A,P,γ,R), where SSS are states, AAA are actions, PPP are transition probabilities, γ\gammaγ is a discount factor, and RRR is a reward function. Policy Iteration allows you to find the optimal policy by iteratively updating the values of states and actions.

# Implementation.
-	Policy Iteration: random initialisation of the policy; calculation of state values for the current policy; greedy policy update.
-	MDP Learning: estimation of transient probabilities and rewards based on frequencies; use of Policy Iteration to update the policy.

# Results.
The optimal policy, state values for it, and estimated transition probabilities and rewards for unknown parameters are obtained.

![image](https://github.com/user-attachments/assets/b752c072-48a0-4826-9b66-d36a5018637c)


# Conclusion.
The algorithms correctly implement Policy Iteration and MDP training, achieving optimal results for a given model.
