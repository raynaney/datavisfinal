# DataVis Final
Project to visualize wildfire spread.

## Installation
1. Install the requirements [TODO: create requirements.txt / environment.yml]
   - pip install pyvista python-decouple

2. Create a `/data` folder and download the `.vts` files from [here](https://wifire-data.sdsc.edu/data/SciVis2022/).
   Follow the online structure, e.g.:
   - data
     - mountain_backcurve40
       - mountain_backcurve40.output.1000.vts
       - [...].vts
     - mountain_backcurve80
       - [...].vts
3. Create a =.env= file \\
   A `.env` file is used to keep track of machine-specific variables. Create a
   `.env` in the root of this project with the following values set:
   ```bash
   PROJECT_DIR=/path/to/root/of/project/ # the root directory of the project
   DATA_DIR=/path/to/root/of/project/data/ # the data directory
   ```

   To access these variables in python code run:
   ```python
   from decouple import config
   config("PROJECT_DIR")
   ```
## The data
Explanation of the data from the IEEE 2022 SciVis Contest:

> The data consists of seven HIGRAD/FIRETEC simulations, each with
> multiple time series (each 70 to 100 times steps) of 3D scalar fields
> on a curvilinear grid from coupled Higrad/Firetec simulations. These
> .vts (VTK structured grid data format, can be opened using Paraview)
> files were generated to study a phenomena known as vorticity-driven
> lateral spread in mountain and canyon topographies. There are six
> mountain and one canyon scenario. Simulations names are first tagged
> with the topographical structure - either mountain or valley. Mountain
> simulations are then tagged with either head curve or back curve to
> indicate whether the fire starts as a headfire or a backing fire and
> that the simulation is a part of a suite of simulations exploring the
> influence of the radius of curvature along the ridgeline. Finally, a
> numerical value is associated with each simulation - 40, 80 or 320. This
> value determines the radius of curvature or roundness of the peak of the
> mountain. A higher value indicates a more rounded ridgeline, resulting
> in a gentle hill top as opposed to a sharp pointy ridge. For questions,
> please contact Divya Banesh, dbanesh@lanl.gov.
