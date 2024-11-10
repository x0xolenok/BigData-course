import numpy as np


S = ['s1', 's2', 's3']
A = ['a1', 'a2']
gamma = 0.9
P = {
    's1': {'a1': {'s1': 0.5, 's2': 0.5}, 'a2': {'s2': 1.0}},
    's2': {'a1': {'s1': 0.7, 's3': 0.3}, 'a2': {'s3': 1.0}},
    's3': {'a1': {'s3': 1.0}, 'a2': {'s1': 0.6, 's3': 0.4}}
}
R = {'s1': 5, 's2': 10, 's3': 0}

# Алгоритм 5: Policy Iteration Algorithm
def policy_iteration(S, A, P, R, gamma):

    policy = {s: np.random.choice(A) for s in S}
    V = {s: 0 for s in S}

    while True:

        for s in S:
            action = policy[s]
            V[s] = R[s] + gamma * sum(P[s][action].get(s_next, 0) * V[s_next] for s_next in S)


        policy_stable = True
        for s in S:
            old_action = policy[s]
            policy[s] = max(A, key=lambda a: sum(P[s][a].get(s_next, 0) * V[s_next] for s_next in S))
            if old_action != policy[s]:
                policy_stable = False


        if policy_stable:
            break

    return policy, V

# Алгоритм 6: MDP Learning with Unknown Ps,a
def learn_mdp(S, A, gamma, trials=1000):
    policy = {s: np.random.choice(A) for s in S}
    P_est = {s: {a: {s_next: 1 / len(S) for s_next in S} for a in A} for s in S}
    R_est = {s: 0 for s in S}
    counts = {s: {a: {s_next: 0 for s_next in S} for a in A} for s in S}

    for _ in range(trials):
        for s in S:
            action = policy[s]
            s_next = np.random.choice(S, p=list(P_est[s][action].values()))
            counts[s][action][s_next] += 1
            R_est[s] = R[s]  # Оновлення оцінки винагороди (або через інші дані)
            P_est[s][action] = {s_next: counts[s][action][s_next] / sum(counts[s][action].values())
                                for s_next in S}


        policy, _ = policy_iteration(S, A, P_est, R_est, gamma)

    return policy, P_est, R_est


optimal_policy, V_optimal = policy_iteration(S, A, P, R, gamma)
learned_policy, P_estimated, R_estimated = learn_mdp(S, A, gamma)

print("Optimal policy:", optimal_policy)
print("State values under the optimal policy:", V_optimal)
print("Estimated policy:", learned_policy)
print("Estimated transition probabilities:")
for s, actions in P_estimated.items():
    for a, transitions in actions.items():
        print(f"  {s} -> {a}: {transitions}")
print("Estimated reward function:", R_estimated)
