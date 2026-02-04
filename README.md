"# NFA-Epsilon-Removal." 
🧪 Lab Report
Eliminating ε-Transitions from a Non-Deterministic Finite Automaton (NFA)
Student Name: …………………
Module: Automata Theory / Formal Languages
Lab: Eliminating ε-Transitions from an NFA
Language Used: Python
Academic Year: 2025–2026
1. Introduction

In automata theory, a Non-Deterministic Finite Automaton (NFA) is a finite automaton that may contain multiple transitions for the same input symbol and may also include ε (epsilon) transitions.

An ε-transition is a transition that does not consume any input symbol. These transitions are useful during the construction of automata from regular expressions, but they must be eliminated before performing determinization (NFA → DFA).

The purpose of this lab is to design and implement a program that removes ε-transitions from an NFA and produces an equivalent NFA without ε-transitions.

2. Objective of the Lab

The main objectives of this work are:

To read and represent an NFA that contains ε-transitions

To compute the ε-closure of each state

To eliminate ε-transitions using the theoretical algorithm

To compute the new transition function

To determine the new set of final states

To display the resulting NFA without ε-transitions

3. Theoretical Background
3.1 Non-Deterministic Finite Automaton (NFA)

An NFA is defined as a 5-tuple:

N = (Q, Σ, δ, q0, F)

Where:

Q is a finite set of states

Σ is the input alphabet

δ is the transition function

q0 is the initial state

F is the set of final states

An NFA may contain transitions labeled with ε.

#3.2 ε-Closure

For a given state 𝑞 the ε-closure(q) is defined as:

The set of all states reachable from q using only ε-transitions, including q itself.

Formally:

𝜀-closure(𝑞)={𝑝∈𝑄∣𝑞→𝜀∗𝑝}
	​
#3.3 Elimination of ε-Transitions

To eliminate ε-transitions from an NFA, the following steps are applied:

1)-Compute ε-closure for each state

2)-For every state s and input symbol 𝑎, compute new transitions:

𝛿′(𝑠,𝑎)=⋃(𝑞∈𝜀-closure(𝑠))𝜀-closure(𝛿(𝑞,𝑎)
	​
3)-Update final states:

A state becomes final if its ε-closure contains at least one original final state

4. Program Design and Implementation (Python)

The program was implemented in Python, as allowed by the instructor.

4.1 Task 1 – Reading the NFA

The program reads:

Number of states

Alphabet symbols (excluding ε)

Transitions (symbol transitions and ε-transitions)

Start state

Final states

The NFA is stored using Python data structures such as lists, sets, and dictionaries.

4.2 Task 2 – Computing ε-Closures

For each state, a Depth-First Search (DFS) is used to compute its ε-closure.

Each ε-closure contains:

The state itself

All states reachable through ε-transitions

4.3 Task 3 – Computing New Transitions

For every state and every input symbol:

The program explores all states in its ε-closure

It follows symbol transitions

Then computes the ε-closure of the reached states

This ensures that all ε-paths are correctly eliminated.

4.4 Task 4 – Computing New Final States

A state is marked as final in the new NFA if:

At least one state in its ε-closure is a final state in the original NFA

4.5 Task 5 – Displaying the New Automaton

The program displays:

ε-closures of all states

The new transition function (without ε)

The new set of final states

5. Example Execution
5.1 Input NFA

States: {0, 1, 2}

Alphabet: {a, b}

Transitions:

0 ε 1

1 a 1

1 b 2

Start state: 0

Final state: {2}

5.2 ε-Closures
E-closure(0) = {0, 1}
E-closure(1) = {1}
E-closure(2) = {2}

5.3 New NFA Without ε-Transitions
δ(0, a) = {1}
δ(0, b) = {2}
δ(1, a) = {1}
δ(1, b) = {2}

5.4 New Final States
{2}

6. Results and Discussion

All ε-transitions were successfully eliminated

The resulting NFA recognizes the same language as the original NFA

The algorithm strictly follows the theoretical model taught in class

The resulting automaton is ready for determinization

7. Conclusion

In this lab, we successfully implemented a Python program to eliminate ε-transitions from a Non-Deterministic Finite Automaton.

The program:

Computes ε-closures

Rebuilds the transition function

Determines the new set of final states

This work demonstrates a correct application of automata theory concepts and prepares the automaton for further transformations such as DFA conversion.
