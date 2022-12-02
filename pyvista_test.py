import pyvista as pv
import vtk
import sys
import os

v = vtk.vtkVersion()
version = v.GetVTKSourceVersion()

def main(argv):
    argv = sys.argv
    if len(argv) < 2:
        sys.stderr.write("Usage: %s <volume.vtk>\n" % argv[0])
        return 1

    filename = argv[1]

    if not os.path.exists(filename):
        sys.stderr.write("file '%s' not found\n" % filename)
        return 1

    mesh = pv.StructuredGrid(filename) #read in file
    #mesh.set_active_scalars("O2") #get O2 scalar
    #smin, smax = mesh.GetScalarRange() #get scalar range
    """
    # Create colour transfer table: mapping scalar value to colour
    opacity_function = vtk.vtkPiecewiseFunction() #a function that creates a ramp
    opacity_function.AddPoint(smin, 0.0) #add control points on that color ramp
    opacity_function.AddPoint(smax, 0.2) #the maximum value is 20% opaque

    # Create colour transfer table: mapping scalar value to colour
    colour_function = vtk.vtkColorTransferFunction() #interpolates color values
    colour_function.AddRGBPoint(smin, 0.0, 0.0, 0.0) #can do RGB space with minimum mapping
    colour_function.AddRGBPoint(smax, 1.0, 1.0, 1.0) #maximum scalar value mapped

    volume_property = vtk.vtkVolumeProperty() #connects the volume transfer function to color mapping
    volume_property.SetColor(colour_function)
    volume_property.SetScalarOpacity(opacity_function)
    volume_property.ShadeOn() ;# adds shading, but will introduce artefacts (and CPU/GPU load)
    volume_property.SetInterpolationTypeToLinear()
    volume_mapper = vtk.vtkSmartVolumeMapper()
    breakpoint()
    volume_mapper.SetInputData(mesh) #error: The SetInput method of this mapper requires either a vtkImageData or a vtkRectilinearGrid as input
    """

    model = mesh

    # contours for O2
    contours = model.contour(15, scalars='O2')
    contours.array_names

    contours['O2'] /= contours['O2'].max() #not sure what this line is actually doing

    p = pv.Plotter(shape=(1, 2))

    p.add_text('Opacity by Array')
    p.add_mesh(
        contours.copy(),
        use_transparency=True,
        scalars='O2',
        opacity='O2', #this is not quite right either
        cmap='bwr',
    )

    # contours for fire fuel
    contours = mesh.contour(scalars = 'rhof_1')
    p.add_mesh(mesh.outline(), color="k")
    p.add_mesh(contours, opacity=0.25, clim=[0, 200])

    """
    p.subplot(0, 1)
    p.add_text('No Opacity')
    p.add_mesh(contours, scalars='O2', cmap='bwr')
    """
    p.show()


if __name__ == "__main__":
    main(sys.argv)
