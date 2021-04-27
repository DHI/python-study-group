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
To run the optimisation using DHI's mosek license: copy mosek.lic to the directory %userprofile%\mosek\. You need to be on DHI's network in order to access the license server.

In the notebook you must enable the lines that refer to 'cp.MOSEK'. Without doing so, the notebook runs the optimisation with
cvxpy's default solver, which is 4-10 times slower than mosek.