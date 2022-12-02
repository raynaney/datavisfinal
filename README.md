# datavisfinal

Explanation of the data from the IEEE 2022 SciVis Contest:

The data consists of seven HIGRAD/FIRETEC simulations, each with
multiple time series (each 70 to 100 times steps) of 3D scalar fields
on a curvilinear grid from coupled Higrad/Firetec simulations. These
.vts (VTK structured grid data format, can be opened using Paraview)
files were generated to study a phenomena known as vorticity-driven
lateral spread in mountain and canyon topographies. There are six
mountain and one canyon scenario. Simulations names are first tagged
with the topographical structure - either mountain or valley. Mountain
simulations are then tagged with either head curve or back curve to
indicate whether the fire starts as a headfire or a backing fire and
that the simulation is a part of a suite of simulations exploring the
influence of the radius of curvature along the ridgeline. Finally, a
numerical value is associated with each simulation - 40, 80 or 320. This
value determines the radius of curvature or roundness of the peak of the
mountain. A higher value indicates a more rounded ridgeline, resulting
in a gentle hill top as opposed to a sharp pointy ridge. For questions,
please contact Divya Banesh, dbanesh@lanl.gov.