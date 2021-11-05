# DASK

## DASK introduction

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


## DASK overview

Dask provides multi-core and distributed parallel execution on larger-than-memory datasets.

We can think of Dask at a high and a low level

*  **High level collections:**  Dask provides high-level Array, Bag, and DataFrame
   collections that mimic NumPy, lists, and Pandas but can operate in parallel on
   datasets that don't fit into memory.  Dask's high-level collections are
   alternatives to NumPy and Pandas for large datasets.
*  **Low Level schedulers:** Dask provides dynamic task schedulers that
   execute task graphs in parallel.  These execution engines power the
   high-level collections mentioned above but can also power custom,
   user-defined workloads.  These schedulers are low-latency (around 1ms) and
   work hard to run computations in a small memory footprint.  Dask's
   schedulers are an alternative to direct use of `threading` or
   `multiprocessing` libraries in complex cases or other task scheduling
   systems like `Luigi` or `IPython parallel`.

Different users operate at different levels but it is useful to understand
both.

The Dask [use cases](https://stories.dask.org/en/latest/) provides a number of sample workflows where Dask should be a good fit.
