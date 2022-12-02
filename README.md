# datavisfinal







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
   MODEL_DIR=/path/to/model/dir/ # the directory where the models (e.g. Stable Diffusion) are saved
   IMG_DIR=/path/to/imgs/dir/ # the directory where generated images go
   ```

   To access these variables in python code run:
   ```python
   from decouple import config
   config("PROJECT_DIR")
   ```
