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


def set_contours(mesh):
    global contours_o2
    global contours_rhof
    global wind_arrows

    # mesh.set_active_scalars("O2")
    contours_o2 = mesh.contour(3, scalars="O2")
    contours_rhof = mesh.contour(scalars="rhof_1")

    # Add arrows
    wind_arrows = mesh.glyph(tolerance=0.05, factor=2.0)


def update_contours(mesh_n):
    global contours_o2
    global contours_rhof
    global wind_arrows

    contours_o2.point_data["O2"] = mesh_n.contour(3, scalars="O2").point_data[
        "O2"
    ]
    contours_rhof.point_data["rhof_1"] = mesh_n.contour(
        scalars="rhof_1"
    ).point_data["rhof_1"]
    wind_arrows.point_data["u"] = mesh_n.glyph(
        tolerance=0.05, factor=2.0
    ).point_data["u"]


def plot_through_time(filenames):
    global plotter
    global mesh

    plotter = pvqt.BackgroundPlotter()
    mesh = pv.StructuredGrid(filenames[0])
    mesh.set_active_scalars("u")

    # plotter.add_mesh(mesh.outline())
    # plotter.add_mesh(mesh.contour(3, scalars="O2"))
    # set_contours(mesh)
    # plotter.add_mesh(mesh.contour(3, scalars="O2"))

    # plotter.add_mesh(
    #     contours_o2,
    #     use_transparency=True,
    #     scalars="O2",
    #     opacity="O2",  # this is not quite right either
    #     cmap="bwr",
    # )
    # plotter.add_mesh(contours_rhof, opacity=0.25, clim=[0, 200])
    # plotter.add_mesh(wind_arrows, color="yellow")
    plotter.add_mesh(mesh)

    plotter.show()

    thread = Thread(target=update_plot, args=(filenames[1:],))
    thread.start()
    breakpoint()


def update_plot(filenames):
    for file_t in filenames:
        time.sleep(1)
        mesh_n = pv.StructuredGrid(file_t)

        # Update points
        mesh.point_data["O2"] = mesh_n.point_data["O2"]


if __name__ == "__main__":
    args = get_args()
    tseries_dirpath = Path(config("DATA_DIR")) / args.data_folder
    tseries_fpaths = sorted(list(tseries_dirpath.glob("*.vts")))
    print("Plotting:")
    print("\n".join([str(x.name) for x in tseries_fpaths]))

    plot_through_time(tseries_fpaths)
