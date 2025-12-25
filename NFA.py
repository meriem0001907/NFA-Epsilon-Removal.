MAX_STATES = 20

# --------------------------------------------------
# Task 1: Read NFA
def read_nfa():
    n_states = int(input("Enter number of states: "))
    n_symbols = int(input("Enter number of symbols: "))

    symbols = input("Enter symbols (without epsilon, space separated): ").split()

    transitions = {i: {s: set() for s in symbols} for i in range(n_states)}
    eps = {i: set() for i in range(n_states)}

    print("Enter transitions (state symbol state), use e for epsilon (-1 to stop):")
    while True:
        data = input().split()
        if data[0] == '-1':
            break

        from_state = int(data[0])
        sym = data[1]
        to_state = int(data[2])

        if sym == 'e':
            eps[from_state].add(to_state)
        else:
            transitions[from_state][sym].add(to_state)

    start_state = int(input("Enter start state: "))

    final_states = set(map(int, input("Enter final states (space separated): ").split()))

    return n_states, symbols, transitions, eps, start_state, final_states


# --------------------------------------------------
# Task 2: Compute epsilon-closure
def epsilon_closure(state, eps):
    stack = [state]
    closure = {state}

    while stack:
        current = stack.pop()
        for nxt in eps[current]:
            if nxt not in closure:
                closure.add(nxt)
                stack.append(nxt)

    return closure


def compute_all_eclosures(n_states, eps):
    return {i: epsilon_closure(i, eps) for i in range(n_states)}


# --------------------------------------------------
# Task 3 & 4: New transitions and new final states
def remove_epsilon(n_states, symbols, transitions, eps, final_states):
    eclosures = compute_all_eclosures(n_states, eps)

    new_transitions = {i: {s: set() for s in symbols} for i in range(n_states)}
    new_final_states = set()

    for state in range(n_states):
        # Determine new final states
        if eclosures[state] & final_states:
            new_final_states.add(state)

        # Compute new transitions
        for sym in symbols:
            reachable = set()
            for q in eclosures[state]:
                for t in transitions[q][sym]:
                    reachable |= eclosures[t]
            new_transitions[state][sym] = reachable

    return new_transitions, new_final_states, eclosures


# --------------------------------------------------
# Task 5: Display new automaton
def display_nfa(symbols, transitions, final_states, eclosures):
    print("\nE-closures:")
    for state, clo in eclosures.items():
        print(f"E-closure({state}) = {clo}")

    print("\nNew NFA (without epsilon transitions):")
    for state in transitions:
        for sym in symbols:
            print(f"δ({state}, {sym}) = {transitions[state][sym]}")

    print("\nNew final states:", final_states)


# --------------------------------------------------
# Task 6: Display flattened transitions of new NFA
def display_flat_transitions(transitions, symbols):
    print("\nTransitions (flattened) without epsilon:")
    for state in transitions:
        for sym in symbols:
            for to_state in transitions[state][sym]:
                print(f"{state} {sym} {to_state}")


# --------------------------------------------------
def main():
    n_states, symbols, transitions, eps, start_state, final_states = read_nfa()
    new_trans, new_finals, eclosures = remove_epsilon(
        n_states, symbols, transitions, eps, final_states
    )
    display_nfa(symbols, new_trans, new_finals, eclosures)

    # Display flattened transitions at the end
    display_flat_transitions(new_trans, symbols)


# --------------------------------------------------
if __name__ == "__main__":
    main()
