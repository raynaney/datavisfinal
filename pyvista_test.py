import pyvista as pv
import sys
import os
from pathlib import Path
from decouple import config


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: %s <volume.vtk>\n" % argv[0])
        return 1

    filename = argv[1]

    if not os.path.exists(filename):
        sys.stderr.write("file '%s' not found\n" % filename)
        return 1

    # mesh = pv.read(filename)
    mesh = pv.StructuredGrid(filename)
    cpos = mesh.plot()


if __name__ == "__main__":
    # main(sys.argv)
    manual_argv = [
        "pyvista_test.py",
        Path(config("DATA_DIR"))
        / "mountain_backcurve40/mountain_backcurve40.output.1000.vts",
    ]
    main(manual_argv)
