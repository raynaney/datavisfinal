import pyvista as pv
import sys
import os


def main(argv):
    argv = sys.argv
    if len(argv) < 2:
        sys.stderr.write("Usage: %s <volume.vtk>\n" % argv[0])
        return 1

    filename = argv[1]

    if not os.path.exists(filename):
        sys.stderr.write("file '%s' not found\n" % filename)
        return 1

    # mesh = pv.read(filename)
    mesh = pv.StructuredGrid(filename)
    breakpoint()
    cpos = mesh.plot()


if __name__ == "__main__":
    main(sys.argv)
