# SciVis wildfire visualization of VLS
This paper presents a visualization and analysis of vorticity-driven lateral spread (VLS) in wildfire scenarios. The purpose of the study is to understand and evaluate the underlying mechanisms of VLS in wildfires, and to determine how visualizations of VLS simulations can inform decision-making in the field. We analyze the influence of VLS on wildfires in simulated environments with varying topological characteristics and study the effect of VLS on the spread of wildfires. The visualizations and analysis tools developed in this work are intended to help firefighters make more informed decisions in the field.

## Installation
1. Install ParaView.
2. Create a `/data` folder and download the `.vts` files from [here](https://oceans11.lanl.gov/firetec/).
   Follow the online structure, e.g.:
   - data
     - mountain_backcurve40
       - output.1000.vts
       - output.2000.vts
       - [...]
     - mountain_backcurve80
       - output.1000.vts
       - output.2000.vts
       - [...]
     - [...]
3. Install python-decouple and create a `.env` file.
   - `pip install python-decouple`
   - A `.env` file is used to keep track of machine-specific variables. Create a
     `.env` in the root of this project with the following values set:
     ```bash
     DATA_DIR=/path/to/root/of/project/data/
     ```
   - To access these variables in python code run:
     ```python
     from decouple import config
     config("DATA_DIR")
     ```
## Running
1. Locate the `pvpython` executable
   - Navigate to ParaView in Applications, right click and show contents.
   - Locate the executable and copy the path, e.g. `/Applications/ParaView-<VERSION>.app/Contents/bin/pvpython`.
2. Run `/Applications/ParaView-<VERSION>.app/Contents/bin/pvpython py_anim.py` to generate the overview animation frames.
3. Run `/Applications/ParaView-<VERSION>.app/Contents/bin/pvpython py_anim_closeup.py` to generate the close-up animation frames.
4. Run `convert *.png animation.gif` from each of the output folders (found in the data directory) to create the animation.

Note: memory usage is high for the generations. If memory issues occur, consider generating the animations as follows:
1. Set `single_run_mode=True`{:.python} in `py_anim.py` and `py_anim_closeup.py` (at the bottom of the file).
2. Run `chmod +x run_anim.sh`{:.bash} and `chmod +x run_anim_closeup.sh`{:.bash} to make the shell scripts executable.
3. Double check the `pvpython` path in `run_anim.sh` and `run_anim_closeup.sh`, it should point to your `pvpython` executable.
4. Run `./run_anim.sh` and `./run_anim_closeup.sh` to generate the overview and closeup visualization frames.
5. Run `convert *.png animation.gif` from each of the output folders (found in the data directory) to create the animation.

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
