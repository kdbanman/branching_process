# Branching Process

Branching process simulations as per Chapter 0 _Probability with Martingales_ by David Williams.

Usage examples are available in `examples.py`, which can be run as a demonstration:

```bash
$ python examples.py
```

Which will have output similar to the following, depending on the randomness of the run.

---

Running default process: Poisson with mean 1.0 children per parent per generation,
  for 30 generations,
  starting with a population of 100,
  plotting the population each time.

```
      50 **************************************************
      68 ********************************************************************
      73 *************************************************************************
      72 ************************************************************************
      76 ****************************************************************************
      62 **************************************************************
      62 **************************************************************
      51 ***************************************************
      62 **************************************************************
      60 ************************************************************
      59 ***********************************************************
      50 **************************************************
      50 **************************************************
      51 ***************************************************
      48 ************************************************
      34 **********************************
      33 *********************************
      33 *********************************
      47 ***********************************************
      38 **************************************
      36 ************************************
      38 **************************************
      26 **************************
      32 ********************************
      36 ************************************
      31 *******************************
      29 *****************************
      43 *******************************************
      46 **********************************************
      44 ********************************************
```

Doing the same thing, but for a process with mean 0.96 children per parent.

```
      50 **************************************************
      50 **************************************************
      38 **************************************
      36 ************************************
      24 ************************
      23 ***********************
      25 *************************
      22 **********************
      19 *******************
      14 **************
      19 *******************
      15 ***************
      18 ******************
      19 *******************
      19 *******************
      24 ************************
      26 **************************
      30 ******************************
      27 ***************************
      29 *****************************
      22 **********************
      17 *****************
      19 *******************
       9 *********
       6 ******
       5 *****
       3 ***
       2 **
       2 **
       4 ****
```

Run the default process with an initial population of 5,
  printing the raw array containing the number of children from each parent.
  **Occasionally this will run for a huge number of generations. Exercise: When and why?**

```
[1 1 1 1 1]
[2 2 0 0 1]
[0 1 3 0 1]
[0 2 2 0 1]
[1 1 1 1 0]
[2 0 0 2]
[0 1 1 2]
[1 3 3 0]
[1 2 0 2 1 3 1]
[2 3 0 0 1 0 2 0 1 4]
[2 1 2 1 0 1 0 0 0 1 2 3 1]
[1 1 1 2 1 2 2 2 1 0 1 0 0 0]
[4 1 2 3 2 1 0 0 1 0 0 1 1 3]
[1 0 0 0 0 0 0 1 5 0 1 0 2 0 1 1 3 2 1]
[0 0 2 0 3 0 0 1 0 0 1 0 1 0 0 2 1 2]
[0 2 1 2 0 2 2 1 1 0 0 0 1]
[1 2 1 2 0 2 1 3 0 0 1 5]
[0 0 2 0 2 1 0 0 1 1 0 1 2 0 0 0 1 1]
[0 2 0 3 3 1 2 3 2 1 1 3]
[0 0 0 2 0 1 1 1 0 1 3 0 2 1 1 0 0 0 1 2 0]
[1 0 1 2 1 1 3 0 0 0 0 1 3 0 0 0]
[0 1 0 1 0 0 0 1 0 2 2 0 4]
[0 4 1 1 4 1 3 0 1 0 2]
[2 1 0 0 1 1 1 3 0 0 1 0 3 0 2 0 1]
[1 0 3 1 0 0 3 2 1 1 3 0 2 0 2 3]
[1 3 0 0 0 2 0 2 3 1 0 2 0 2 0 0 0 2 5 1 0 3]
[0 1 2 1 2 0 0 1 1 0 2 0 2 0 2 1 1 2 0 0 0 3 0 0 2 1 3]
[1 2 1 0 0 2 0 1 1 1 2 0 4 2 1 0 1 0 0 2 0 0 1 0 0 1 1]
[1 2 2 1 0 1 1 2 4 1 0 2 3 2 1 1 1 0 0 0 1 0 2 1]
[0 0 1 0 1 0 1 2 0 0 0 1 0 1 4 2 0 0 1 0 0 0 0 1 1 1 1 2 2]
[0 2 2 1 0 1 0 0 0 2 1 1 2 1 0 3 3 2 1 3 2 0]
[0 0 0 1 1 0 1 2 1 0 2 1 0 2 0 1 2 2 1 0 3 2 0 0 1 1 0]
[0 3 4 1 3 2 2 0 2 4 1 2 2 2 2 0 0 1 0 1 2 0 0 0]
[0 2 0 4 0 1 1 0 0 1 3 2 1 2 2 0 0 0 2 0 0 0 0 1 1 1 0 1 1 1 4 0 1 1]
[0 0 0 2 1 1 1 1 0 1 0 1 1 1 0 1 1 1 1 0 0 0 2 2 0 0 1 0 0 0 0 2 0]
[3 3 1 3 1 1 1 0 2 2 0 1 1 3 3 0 3 1 1 0 2]
[2 2 1 2 1 0 1 2 1 0 0 2 1 0 1 0 1 5 1 0 0 1 3 1 2 1 0 2 0 0 2 3]
[0 0 1 0 0 1 0 0 3 2 0 1 0 2 1 1 4 1 0 1 1 4 1 2 1 0 0 0 1 1 1 1 1 1 1 2 1 0]
[0 2 0 1 2 1 0 1 4 0 0 1 0 0 0 2 0 1 0 0 1 2 0 1 0 1 1 1 0 2 1 0 0 1 3 0 1]
[1 1 1 2 2 0 3 1 0 1 0 0 1 0 2 1 1 2 2 3 0 2 0 1 1 0 4 0 0 1]
[1 1 0 0 2 0 1 0 0 0 2 0 2 4 2 0 0 0 1 2 1 1 3 1 2 2 0 0 0 0 3 0 0]
[0 2 0 1 0 0 3 0 1 0 2 1 0 2 1 1 1 1 1 1 0 0 0 2 1 1 0 3 1 1 3]
[0 1 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 1 0 1 2 1 1 0 0 1 3 1 0 0]
[0 1 1 1 1 1 2 1 1 0 0 0 1 1 2 2 0]
[2 1 1 2 2 2 2 2 3 1 1 2 0 1 0]
[2 0 0 3 0 0 4 0 0 1 2 0 1 0 1 1 0 1 0 1 0 0]
[0 0 3 3 0 3 1 2 1 0 0 0 0 0 3 2 2]
[1 0 0 1 2 1 1 3 0 3 0 1 1 2 2 0 1 0 1 2]
[0 1 2 2 2 0 1 3 2 0 1 2 0 2 2 1 0 2 2 0 0 1]
[1 2 1 0 0 2 1 1 2 0 1 1 0 0 2 0 2 2 2 0 0 1 2 0 1 0]
[1 2 0 1 0 1 0 2 0 1 0 0 0 2 0 0 0 1 0 0 0 0 1 1]
[1 0 0 1 0 0 1 0 0 1 2 1 0]
[2 1 0 1 1 2 1]
[2 1 2 0 1 1 1 0]
[0 2 3 1 2 2 1 2]
[0 1 0 0 0 0 1 3 0 2 0 4 0]
[0 0 2 2 0 0 2 1 0 0 3]
[0 0 1 1 1 0 0 0 0 3]
[0 0 0 0 3 2]
[4 3 0 1 0]
[1 1 0 1 0 1 0 1]
[0 0 0 1 0]
[3]
[0 1 1]
[0 0]
```

Doing the same thing, but using the built in sibling printer,
  printing the children that come from each parent as '.' characters,
  where each set of siblings is separated by a '|' character.

```
. | . | . | . | .
.. | . |  | . | ......
 | . | . | .. |  |  | .... | ... | . | .
 | . | .. | .. |  |  | . |  | . |  | . |  | ..
 | . | .. | .. |  | . | .. | .. | .. |
 | .. | ... | . |  |  | . |  |  | .... | .. | ..
.. | . | .. | . |  |  | . |  | . |  | ... |  | . |  |
... |  | . | . |  | .. |  |  |  |  | . |
 | .. | . | .. | ... | . |  | .
.. | .. | . | ... | .. | . |  |  |  |
. |  | .. |  |  |  |  | .. |  |  |
.. | .. |  | . | ....
. |  | ... | . | .. | . |  | . |
 |  | . | . |  |  | . |  | ..
. | .. |  |  | ..
. | . | ... | . |
 | . | ... |  |  | .
 | . |  |  |
..
.. |
. | .
... | .
 | ... |  | .
 |  | . | .
.. | .
 |  | .
....
 | . |  | .
. | .
 |
```

Run a Bernoulli child generating process,
  with 0.5 probability of generating 2 children per parent,
  generating 0 children otherwise,
  plotting the population of each generation.
  **This wil also sometimes runaway in number of generations. Exercise: When and why?**

```
       5 *****
       2 **
       2 **
       4 ****
       4 ****
       6 ******
       8 ********
      12 ************
      14 **************
      14 **************
      16 ****************
      16 ****************
      12 ************
      14 **************
       6 ******
       6 ******
       6 ******
       6 ******
       2 **
       4 ****
       2 **
       2 **
       2 **
       2 **
       0
```

Do the same thing, but with a 0.25 probability of generating 5 children,
  for 50 generations,
  starting with a population of 15,
  plotting the population on a logarithmic scale.

```
1.00E+01 ***
1.00E+01 ***
2.50E+01 ****
3.50E+01 *****
3.00E+01 ****
3.00E+01 ****
2.00E+01 ****
2.50E+01 ****
3.50E+01 *****
5.00E+01 *****
6.00E+01 *****
6.50E+01 ******
9.00E+01 ******
9.00E+01 ******
1.55E+02 *******
2.10E+02 *******
2.20E+02 *******
2.80E+02 ********
3.75E+02 ********
4.50E+02 ********
6.00E+02 *********
7.10E+02 *********
8.20E+02 *********
1.10E+03 **********
1.42E+03 **********
1.62E+03 **********
2.06E+03 ***********
2.70E+03 ***********
3.32E+03 ***********
4.26E+03 ************
```