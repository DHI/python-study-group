# Dependencies
- matplotlib
- numpy
- scipy
- pandas
- cvxpy 
- control

A common reason for cvxpy to fail installation is that it needs a c-compiler to build the installation package of some of its 
dependencies. The error message points you towards visual studio build tools, from whis a compiler can be installed. 

# mosek license
Get a one-month trial license of mosek at https://www.mosek.com/try/. If you are a DHI'er, you can ask AKF for access to internal license

In the notebook you must enable the lines that refer to 'cp.MOSEK'. Without doing so, the notebook runs the optimisation with
cvxpy's default solver, which is 4-10 times slower than mosek.