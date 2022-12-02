import pyvista as pv
import pyvistaqt as pvqt
import argparse
import vtk
import sys
import os
import time
from threading import Thread
from decouple import config
from pathlib import Path

v = vtk.vtkVersion()
version = v.GetVTKSourceVersion()


def get_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data_folder",
        "-df",
        default="mountain_backcurve40",
        type=str,
        choices=[
            "mountain_backcurve40",
            "mountain_backcurve80",
            "mountain_backcurve320",
            "mountain_headcurve40",
            "mountain_headcurve80",
            "mountain_headcurve320",
        ],
        help="the name of the time series folder with the vts files.",
    )

    return parser


def get_args():
    return get_parser().parse_args()


def plot_through_time(filenames):
    global mesh
    global plotter

    mesh = pv.StructuredGrid(filenames[0])
    mesh.set_active_scalars("O2")

    plotter = pvqt.BackgroundPlotter()
    plotter.add_mesh(mesh)
    plotter.show()

    thread = Thread(target=update_plot, args=(filenames[1:],))
    thread.start()


def update_plot(filenames):
    for file_t in filenames:
        mesh_n = pv.StructuredGrid(file_t)
        mesh.point_data["O2"] = mesh_n.point_data["O2"]
        time.sleep(1)


if __name__ == "__main__":
    args = get_args()
    tseries_dirpath = Path(config("DATA_DIR")) / args.data_folder
    tseries_fpaths = sorted(list(tseries_dirpath.glob("*.vts")))
    print("Plotting:")
    print("\n".join([str(x.name) for x in tseries_fpaths]))

    plot_through_time(tseries_fpaths)
