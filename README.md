# Truth-Tree-Project
This project aims to act as a truth tree creator for L1 sentences (which fall under propositional logic), and inform the user of the logical result of the tableaux proof.

## Explanation
Truth trees, or tableaux proofs, are used as a visualisation of the possible structures which satisfy a sentence or set of sentences. If we look at the sentence `p ^ q` we can break this down into the two sentences `p` and `q`. This is because both of these setences have to also be true if the first is true. A disjunction, on the other hand, branches. For example, for `p v q` to be true, either `p` or `q` must be true. A similar principle can be applied to all sentences. Once done repeatedly, you create a tree which represents that set of sentences.

![Example Truth Tree](https://www.logicmatters.net/wp-content/uploads/2010/04/tableau01.gif)

The above tree, in my program, should look like this when input:

     `|- p^r, ¬(p^q), ¬(¬(rvq)), p, r`

         |   - ¬(p), rvq   x

             |  |- ¬(q), rvq

                `|  |  - r

                `|  |   - q   x`

Concerning proof using a truth tree, either all paths are closed or they aren't. By this I mean that if all paths are closed we know that there must be a contradiction in the set. However, if all paths are open, this does not mean that it is a tautology, only that it is satisfiable. Due to this, to prove whether a sentence is a tautology, we must negate it and then prove its negation is a contradiction.


## Usage
It should be run using main.py, and it only requires python3. Running the program should result in a menu giving options from 1 to 5.
The first option will run a set of example tests that demonstrate what the code does.
The second will create a tree from a set of sentences to see whether it is satisfiable.
The third will do the same as teh previous, except it informs you if it is a contradiction.
For the fourth option, so as to distiguish whether the sentence input is a tautology, we must test whether its negation is a contradiction.
This menu will keep on appearing until number five is selected, which quits the program.

When inputting sentences, I have required more than the syntax of propositional logic usually demands. Firstly, I have prevented the user from inputting unnecessary brackets, which includes brackets that wrap around the entire sentence as well as double brackets. On top of this, the user must make all implicit brackets explicit. 

For example, the implicit brackets for `p v q v r` are `p v ( q v r )`, meaning only the second sentence would be excepeted by the program. Another example would be that `p ^ ¬p` has to be written as `p ^ ( ¬ ( p ) )`. Brackets are important as they dictate the scope of a connective.

Also, I don't allow anything more than single letter variables, and everything must be separated by a space. So, `pvq` would be rejected as it would be read as a multi letter variable, rather than as `p v q`.



