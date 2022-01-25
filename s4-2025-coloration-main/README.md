# Coloration Contest

## Repo content

### Graphs

#### The directory `files` contains some graphs to test, in alphabetic order:
- The first 3 are bipartite: therefore 2 colors...
- The next 4 are planar: therefore at most 4 colors (see the _four color theorem_!)
- The last 3: "mystery" graphs!

#### Graph Specifications:
- no multiple links
- no loops (obviously)

#### Reminder: 
`.gra` files may contain additional informations (given in `G.infos` after `G = graph.load("---.gra")`), such as:
- dimensions: $`n`$ the order, $`p`$ link number, $`k`$ component number, $`c`$ chromatic number
- some properties: for instance `bipartite: True`
- the "engine" used to display
- ...

### The Python file `testcolor.py`:
- The function `run_verif_coloration(f, dirpath)`: allows you to test your coloration function `f` on graphs in the directory `dirpath` (`files` here)
- Each of your coloration function `f` has to return a pair `(nb_colors, color_vector)`:
    - `nb_colors`: the number of used colors 
    - `color_vector` filled with integers from `1` to `nb_colors` (one color per vertex)
- For example, we tested 4 different methods (functions `color_greedy`, `color_1`, `color_2`, `color_3`) on the 10 graphs in the directory `files` (sorted in alphabetic order) . The results (color number found for each graph):
```python
    >>> run_verif_coloration(color_greedy, "files")
    [2, 2, 5, 5, 4, 5, 4, 4, 15, 4]
    >>> run_verif_coloration(color_1, "files")
    [2, 2, 2, 4, 3, 4, 4, 4, 15, 4]
    >>> run_verif_coloration(color_2, "files")
    [2, 5, 2, 4, 4, 4, 4, 4, 15, 4]
    >>> run_verif_coloration(color_3, "files")
    [2, 2, 2, 4, 3, 4, 4, 4, 15, 3]
```
Who can top that?
## Your work
- Write one or several coloration functions: **at least one with the "greedy" method seen in tutorial** (mandatory if you want to be graded)
- [again] Each of your coloration function has to return a pair `(nb_colors, color_vector)`:
    - `nb_colors`: the number of used colors 
    - `color_vector` filled with integers from `1` to `nb_colors` (one color per vertex)
- In your code, all functions not prefixed by `__` will be tested (must be coloration functions...).
### Handout
You can deposit your "contribution": a file `login_coloration.py` (do not forget to replace `login`...) on Moodle
- As usual your `login_coloration.py` does not contain tests, but only function definitions
    - one coloration function at least
    - intermediate functions must begin with `__`
- You can import anything from `algopy` except `timing` (do not forget to delete the potential `@timing.timing`...)
- You can also import any built-in module
- Do not import `testcolor`!
### Deadlines
- Thursday, January the 27th, 4 PM: we will run our "test suite" on the 10 graphs in `files` (you will see if your submission is "correct"...)
- Tuesday, February the 1st, 10 PM: we will run tests with the graphs from `files` and others (bigger, stranger...)
