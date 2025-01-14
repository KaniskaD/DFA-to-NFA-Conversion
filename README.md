# DFA-to-NFA-Conversion
This Python script performs the conversion of a Non-deterministic Finite Automaton (NFA) to a Deterministic Finite Automaton (DFA) and visualizes both automata using graphs. It uses the networkx library for graph creation and matplotlib for visualization.
The conversion process involves taking an NFA, which allows multiple possible transitions for the same input symbol from a given state, and transforming it into a DFA. In a DFA, each state has exactly one transition for each symbol in the alphabet, making the automaton deterministic.

Libraries Used:
  NetworkX
  Matplotlib
