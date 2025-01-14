import networkx as nx
import matplotlib.pyplot as plt

dfa_letters = ['a', 'b']
nfa_states = ['q0', 'q1', 'q2']
nfa_transitions = {
    ('q0', 'a'): ['q0', 'q1'],
    ('q0', 'b'): ['q0'],
    ('q1', 'a'): ['q2'],
    ('q1', 'b'): ['q0'],
    ('q2', 'a'): ['q0'],
    ('q2', 'b'): ['q1']
}

q = [('q0',)]
dfa_transitions = {}

G_nfa = nx.DiGraph()
G_dfa = nx.DiGraph()

# NFA transitions visualization
for (state, symbol), next_states in nfa_transitions.items():
    for next_state in next_states:
        G_nfa.add_edge(state, next_state, label=symbol)

# DFA transitions visualization (generated after NFA to DFA conversion)
for in_state in q:
    for symbol in dfa_letters:
        f_dest = [] 

        if len(in_state) == 1 and (in_state[0], symbol) in nfa_transitions:
            dfa_transitions[(in_state, symbol)] = nfa_transitions[(in_state[0], symbol)]
            if tuple(dfa_transitions[(in_state, symbol)]) not in q:
                q.append(tuple(dfa_transitions[(in_state, symbol)]))
        else:
            dest = []
            for n_state in in_state:
                if (n_state, symbol) in nfa_transitions:
                    for state in nfa_transitions[(n_state, symbol)]:
                        if state not in dest:
                            dest.append(state)
            if dest:
                for d in dest:
                    for value in d:
                        if value not in f_dest:
                            f_dest.append(value)
                dfa_transitions[(in_state, symbol)] = f_dest
                if tuple(f_dest) not in q:
                    q.append(tuple(f_dest))
                    
        # Add DFA transitions to graph
        G_dfa.add_edge(str(in_state), str(f_dest), label=symbol)

# Draw the NFA state diagram
plt.figure(figsize=(8, 6))
pos_nfa = nx.spring_layout(G_nfa)
nx.draw(G_nfa, pos_nfa, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold')
edge_labels_nfa = nx.get_edge_attributes(G_nfa, 'label')
nx.draw_networkx_edge_labels(G_nfa, pos_nfa, edge_labels=edge_labels_nfa)
plt.title("NFA Transition Diagram")
plt.show()

# Draw the DFA state diagram
plt.figure(figsize=(8, 6))
pos_dfa = nx.spring_layout(G_dfa)
nx.draw(G_dfa, pos_dfa, with_labels=True, node_size=3000, node_color='lightgreen', font_size=12, font_weight='bold')
edge_labels_dfa = nx.get_edge_attributes(G_dfa, 'label')
nx.draw_networkx_edge_labels(G_dfa, pos_dfa, edge_labels=edge_labels_dfa)
plt.title("DFA Transition Diagram")
plt.show()

print("DFA Transitions:")
for key, value in dfa_transitions.items():
    print(f"From state {key[0]} on symbol '{key[1]}' -> {value}")