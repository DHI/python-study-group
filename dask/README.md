# DASK

## DASK overview

\[ snip from [docs.dask.org](https://docs.dask.org/) \]

Dask is a flexible library for parallel computing in Python.

Dask is composed of two parts:

1. Dynamic task scheduling optimized for computation. This is similar to Airflow, Luigi, Celery, or Make, but optimized for interactive computational workloads.

2. “Big Data” collections like parallel arrays, dataframes, and lists that extend common interfaces like NumPy, Pandas, or Python iterators to larger-than-memory or distributed environments. These parallel collections run on top of dynamic task schedulers.

Dask emphasizes the following virtues:

* **Familiar**: Provides parallelized NumPy array and Pandas DataFrame objects
* **Flexible**: Provides a task scheduling interface for more custom workloads and integration with other projects.
* **Native**: Enables distributed computing in pure Python with access to the PyData stack.
* **Fast**: Operates with low overhead, low latency, and minimal serialization necessary for fast numerical algorithms
* **Scales up**: Runs resiliently on clusters with 1000s of cores
* **Scales down**: Trivial to set up and run on a laptop in a single process
* **Responsive**: Designed with interactive computing in mind, it provides rapid feedback and diagnostics to aid humans

![](https://docs.dask.org/en/latest/_images/dask-overview.svg)

## Resources

* [dask.org](https://dask.org/)
* SciPy 2020 [DASK video tutorial](https://www.youtube.com/watch?v=EybGGLbLipI&ab_channel=Enthought) (3:48 hours)
* [DASK tutorial repo](https://github.com/dask/dask-tutorial) (used in above video)
* Video: [DASK Dashboard walkthrough](https://www.youtube.com/watch?v=N_GqzcuGLCY&t=191s&ab_channel=MatthewRocklin)
* Datacamp course: [parallel-programming-with-dask-in-python](https://app.datacamp.com/learn/courses/parallel-programming-with-dask-in-python)


## 
