# Activity 19: Install Third-Party Packages

**Topic 06: Modules & Packages**  ·  Focus: install and verify third-party packages with pip

Install the course packages on your terminal / CMD prompt (or verify them in Colab): numpy, matplotlib, pandas and yfinance — then import them to confirm.

**You'll build:** A working data-analysis toolkit: numpy, pandas, matplotlib and yfinance.

**Tools:** pip, PyPI, Google Colab / terminal

## Steps

1. On your terminal / CMD prompt install the four packages (in Colab, prefix with ! — numpy, pandas and matplotlib are pre-installed there).

   ```python
   pip install numpy
   pip install matplotlib
   pip install pandas
   pip install yfinance
   ```

2. Verify each package imports and print its version.

   ```python
   import numpy, pandas, matplotlib
   import yfinance
   print(numpy.__version__)
   print(pandas.__version__)
   ```

3. Browse https://pypi.org — every third-party Python package lives here.
4. Optional: the Anaconda distribution (anaconda.com) bundles 150+ scientific packages pre-built — NumPy, Pandas, SciPy, Matplotlib, IPython and more.

## Check your result

All four packages import without ModuleNotFoundError and print a version number.
