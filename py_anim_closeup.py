# state file generated using paraview version 5.10.1
import time
import sys
from pathlib import Path

# uncomment the following three lines to ensure this script works in future versions
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


def render_and_save_file(inp_filename, outp_filename):
    startTime = time.time()

    # ----------------------------------------------------------------
    # setup views used in the visualization
    # ----------------------------------------------------------------

    # Create a new 'Render View'
    renderView1 = CreateView("RenderView")
    # renderView1.ViewSize = [2150, 1152]
    renderView1.ViewSize = [1500, 797]
    renderView1.AxesGrid = "GridAxes3DActor"
    renderView1.CenterOfRotation = [101.0, -1.0, 449.6810739338398]
    renderView1.StereoType = "Crystal Eyes"

    if "mountain_backcurve" in inp_filename:
        renderView1.CameraPosition = [
            481.2030035446619,
            927.2905968996618,
            485.77167882412664,
        ]
        renderView1.CameraFocalPoint = [
            444.75791588915905,
            795.0201492245914,
            418.6610540588739,
        ]
        renderView1.CameraViewUp = [
            -0.14601496231957947,
            -0.41532743083523355,
            0.8978768044529362,
        ]
    else:
        renderView1.CameraPosition = [
            -580.4335841053316,
            -819.0502137866939,
            539.826021898917,
        ]
        renderView1.CameraFocalPoint = [
            -470.9416262188834,
            -653.3075819157582,
            437.1343965108021,
        ]
        renderView1.CameraViewUp = [
            0.27373019969873047,
            0.36938901005035524,
            0.8880447832327556,
        ]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 899.6336487402332

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name="Layout #1")
    layout1.AssignView(0, renderView1)
    # layout1.SetSize(2150, 1152)
    layout1.SetSize(1500, 797)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView1)
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------

    # create a new 'XML Structured Grid Reader'
    output = XMLStructuredGridReader(
        registrationName="output.*", FileName=[inp_filename]
    )
    output.PointArrayStatus = [
        "u",
        "v",
        "w",
        "theta",
        "O2",
        "rhowatervapor",
        "rhof_1",
        "convht_1",
        "frhosiesrad_1",
    ]
    output.TimeArray = "None"

    # create a new 'Contour'
    fireinducedheattransfer = Contour(
        registrationName="fire induced heat transfer", Input=output
    )
    fireinducedheattransfer.ContourBy = ["POINTS", "frhosiesrad_1"]
    fireinducedheattransfer.Isosurfaces = [
        -449420.0,
        -388433.4888888889,
        -327446.97777777776,
        -266460.4666666667,
        -205473.95555555556,
        -144487.44444444444,
        -83500.93333333335,
        -22514.4222222222,
        38472.08888888889,
        99458.59999999998,
    ]
    fireinducedheattransfer.PointMergeMethod = "Uniform Binning"

    # create a new 'Contour'
    bulkDensityDryFuel = Contour(
        registrationName="Bulk Density Dry Fuel", Input=output
    )
    bulkDensityDryFuel.ContourBy = ["POINTS", "rhof_1"]
    bulkDensityDryFuel.Isosurfaces = [
        0.0,
        0.020689655994546825,
        0.04137931198909365,
        0.06206896798364048,
        0.0827586239781873,
        0.10344827997273412,
        0.12413793596728095,
        0.14482759196182776,
        0.1655172479563746,
        0.18620690395092143,
        0.20689655994546824,
        0.22758621594001507,
        0.2482758719345619,
        0.2689655279291087,
        0.2896551839236555,
        0.3103448399182024,
        0.3310344959127492,
        0.351724151907296,
        0.37241380790184286,
        0.39310346389638967,
        0.4137931198909365,
        0.43448277588548334,
        0.45517243188003015,
        0.47586208787457696,
        0.4965517438691238,
        0.5172413998636706,
        0.5379310558582174,
        0.5586207118527643,
        0.579310367847311,
        0.6000000238418579,
    ]
    bulkDensityDryFuel.PointMergeMethod = "Uniform Binning"

    # create a new 'Calculator'
    calculator1 = Calculator(registrationName="Calculator1", Input=output)
    calculator1.ResultArrayName = "wind"
    calculator1.Function = "u*iHat+v*jHat+w*kHat"

    # create a new 'Stream Tracer'
    streamTracer1 = StreamTracer(
        registrationName="StreamTracer1", Input=calculator1, SeedType="Line"
    )
    streamTracer1.Vectors = ["POINTS", "wind"]
    streamTracer1.IntegrationDirection = "FORWARD"
    streamTracer1.IntegratorType = "Runge-Kutta 4"
    streamTracer1.MaximumStreamlineLength = 1198.0

    # init the 'Line' selected for 'SeedType'
    streamTracer1.SeedType.Point1 = [-475.0, -529.0, 105.0]
    streamTracer1.SeedType.Point2 = [-475.0, 468.584, 105.0]
    streamTracer1.SeedType.Resolution = 100

    # create a new 'Contour'
    o2FullRange = Contour(registrationName="O2 (Full Range)", Input=output)
    o2FullRange.ContourBy = ["POINTS", "O2"]
    o2FullRange.Isosurfaces = [
        0.0,
        0.007932573556900024,
        0.01586514711380005,
        0.023797720670700073,
        0.0317302942276001,
        0.03966286778450012,
        0.047595441341400146,
        0.05552801489830017,
        0.0634605884552002,
        0.07139316201210022,
        0.07932573556900024,
        0.08725830912590027,
        0.09519088268280029,
        0.10312345623970032,
        0.11105602979660034,
        0.11898860335350037,
        0.1269211769104004,
        0.13485375046730042,
        0.14278632402420044,
        0.15071889758110046,
        0.1586514711380005,
        0.1665840446949005,
        0.17451661825180054,
        0.18244919180870056,
        0.19038176536560059,
        0.1983143389225006,
        0.20624691247940063,
        0.21417948603630066,
        0.22211205959320068,
        0.2300446331501007,
    ]
    o2FullRange.PointMergeMethod = "Uniform Binning"

    # create a new 'Contour'
    thetaWarmFire = Contour(registrationName="Theta Warm Fire", Input=output)
    thetaWarmFire.ContourBy = ["POINTS", "theta"]
    thetaWarmFire.Isosurfaces = [
        500.0,
        533.3333333333334,
        566.6666666666666,
        600.0,
        633.3333333333334,
        666.6666666666667,
        700.0,
        733.3333333333334,
        766.6666666666667,
        800.0,
    ]
    thetaWarmFire.PointMergeMethod = "Uniform Binning"

    # create a new 'Contour'
    warmSmoke = Contour(registrationName="Warm Smoke", Input=output)
    warmSmoke.ContourBy = ["POINTS", "theta"]
    warmSmoke.Isosurfaces = [
        303.0,
        303.77777777777777,
        304.55555555555554,
        305.3333333333333,
        306.1111111111111,
        306.8888888888889,
        307.6666666666667,
        308.44444444444446,
        309.22222222222223,
        310.0,
    ]
    warmSmoke.PointMergeMethod = "Uniform Binning"

    # create a new 'Contour'
    hotFire = Contour(registrationName="Hot Fire", Input=output)
    hotFire.ContourBy = ["POINTS", "theta"]
    hotFire.Isosurfaces = [
        800.0,
        841.1111111111111,
        882.2222222222222,
        923.3333333333334,
        964.4444444444445,
        1005.5555555555555,
        1046.6666666666667,
        1087.7777777777778,
        1128.888888888889,
        1170.0,
    ]
    hotFire.PointMergeMethod = "Uniform Binning"

    # create a new 'Contour'
    fire = Contour(registrationName="Fire", Input=output)
    fire.ContourBy = ["POINTS", "theta"]
    fire.Isosurfaces = [
        400.0,
        411.1111111111111,
        422.22222222222223,
        433.3333333333333,
        444.44444444444446,
        455.55555555555554,
        466.66666666666663,
        477.77777777777777,
        488.8888888888889,
        500.0,
    ]
    fire.PointMergeMethod = "Uniform Binning"

    # create a new 'Contour'
    convectiveHeatTransfer = Contour(
        registrationName="Convective Heat Transfer", Input=output
    )
    convectiveHeatTransfer.ContourBy = ["POINTS", "convht_1"]
    convectiveHeatTransfer.Isosurfaces = [
        -271779.0,
        -222961.22222222222,
        -174143.44444444444,
        -125325.66666666666,
        -76507.88888888888,
        -27690.111111111095,
        21127.666666666686,
        69945.4444444445,
        118763.22222222225,
        167581.0,
    ]
    convectiveHeatTransfer.PointMergeMethod = "Uniform Binning"

    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------

    # show data from streamTracer1
    streamTracer1Display = Show(
        streamTracer1, renderView1, "GeometryRepresentation"
    )

    # get color transfer function/color map for 'wind'
    windLUT = GetColorTransferFunction("wind")
    windLUT.AutomaticRescaleRangeMode = "Never"
    windLUT.RGBPoints = [
        3.0,
        0.231373,
        0.298039,
        0.752941,
        15.5,
        0.865003,
        0.865003,
        0.865003,
        28.0,
        0.705882,
        0.0156863,
        0.14902,
    ]
    windLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    streamTracer1Display.Representation = "Surface"
    streamTracer1Display.ColorArrayName = ["POINTS", "wind"]
    streamTracer1Display.LookupTable = windLUT
    streamTracer1Display.Opacity = 0.35
    streamTracer1Display.SelectTCoordArray = "None"
    streamTracer1Display.SelectNormalArray = "None"
    streamTracer1Display.SelectTangentArray = "None"
    streamTracer1Display.OSPRayScaleArray = "u"
    streamTracer1Display.OSPRayScaleFunction = "PiecewiseFunction"
    streamTracer1Display.SelectOrientationVectors = "Normals"
    streamTracer1Display.ScaleFactor = 111.83714599609375
    streamTracer1Display.SelectScaleArray = "u"
    streamTracer1Display.GlyphType = "Arrow"
    streamTracer1Display.GlyphTableIndexArray = "u"
    streamTracer1Display.GaussianRadius = 5.591857299804688
    streamTracer1Display.SetScaleArray = ["POINTS", "u"]
    streamTracer1Display.ScaleTransferFunction = "PiecewiseFunction"
    streamTracer1Display.OpacityArray = ["POINTS", "u"]
    streamTracer1Display.OpacityTransferFunction = "PiecewiseFunction"
    streamTracer1Display.DataAxesGrid = "GridAxesRepresentation"
    streamTracer1Display.PolarAxes = "PolarAxesRepresentation"

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    streamTracer1Display.ScaleTransferFunction.Points = [
        -0.6325899958610535,
        0.0,
        0.5,
        0.0,
        24.168136596679688,
        1.0,
        0.5,
        0.0,
    ]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    streamTracer1Display.OpacityTransferFunction.Points = [
        -0.6325899958610535,
        0.0,
        0.5,
        0.0,
        24.168136596679688,
        1.0,
        0.5,
        0.0,
    ]

    # show data from bulkDensityDryFuel
    bulkDensityDryFuelDisplay = Show(
        bulkDensityDryFuel, renderView1, "GeometryRepresentation"
    )

    # get color transfer function/color map for 'rhof_1'
    rhof_1LUT = GetColorTransferFunction("rhof_1")
    rhof_1LUT.AutomaticRescaleRangeMode = "Never"
    rhof_1LUT.RGBPoints = [
        0.0,
        0.4,
        0.0,
        0.0,
        0.0,
        0.4,
        0.047058823529411764,
        0.0,
        0.011764706939748104,
        0.25098039215686274,
        0.027450980392156862,
        0.0,
        0.02588235438121232,
        0.25098039215686274,
        0.24313725490196078,
        0.0,
        0.22941178689931851,
        0.17254901960784313,
        0.2196078431372549,
        0.0,
        0.2811764805024859,
        0.18823529411764706,
        0.21568627450980393,
        0.0,
        0.35529413983182406,
        0.19215686274509805,
        0.25098039215686274,
        0.00392156862745098,
        0.43529412085490093,
        0.10588235294117647,
        0.20784313725490197,
        0.0,
        0.5000000475630119,
        0.0,
        0.23529411764705882,
        0.0,
        0.5482353302386906,
        0.0,
        0.17254901960784313,
        0.0,
        0.6000000238418579,
        0.06666666666666667,
        0.23921568627450981,
        0.0,
    ]
    rhof_1LUT.ColorSpace = "RGB"
    rhof_1LUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    bulkDensityDryFuelDisplay.Representation = "Surface"
    bulkDensityDryFuelDisplay.ColorArrayName = ["POINTS", "rhof_1"]
    bulkDensityDryFuelDisplay.LookupTable = rhof_1LUT
    bulkDensityDryFuelDisplay.Opacity = 0.15
    bulkDensityDryFuelDisplay.SelectTCoordArray = "None"
    bulkDensityDryFuelDisplay.SelectNormalArray = "Normals"
    bulkDensityDryFuelDisplay.SelectTangentArray = "None"
    bulkDensityDryFuelDisplay.OSPRayScaleArray = "rhof_1"
    bulkDensityDryFuelDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    bulkDensityDryFuelDisplay.SelectOrientationVectors = "None"
    bulkDensityDryFuelDisplay.ScaleFactor = 119.80000000000001
    bulkDensityDryFuelDisplay.SelectScaleArray = "rhof_1"
    bulkDensityDryFuelDisplay.GlyphType = "Arrow"
    bulkDensityDryFuelDisplay.GlyphTableIndexArray = "rhof_1"
    bulkDensityDryFuelDisplay.GaussianRadius = 5.99
    bulkDensityDryFuelDisplay.SetScaleArray = ["POINTS", "rhof_1"]
    bulkDensityDryFuelDisplay.ScaleTransferFunction = "PiecewiseFunction"
    bulkDensityDryFuelDisplay.OpacityArray = ["POINTS", "rhof_1"]
    bulkDensityDryFuelDisplay.OpacityTransferFunction = "PiecewiseFunction"
    bulkDensityDryFuelDisplay.DataAxesGrid = "GridAxesRepresentation"
    bulkDensityDryFuelDisplay.PolarAxes = "PolarAxesRepresentation"

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    bulkDensityDryFuelDisplay.ScaleTransferFunction.Points = [
        0.04285714402794838,
        0.0,
        0.5,
        0.0,
        0.6000000238418579,
        1.0,
        0.5,
        0.0,
    ]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    bulkDensityDryFuelDisplay.OpacityTransferFunction.Points = [
        0.04285714402794838,
        0.0,
        0.5,
        0.0,
        0.6000000238418579,
        1.0,
        0.5,
        0.0,
    ]

    # show data from o2FullRange
    o2FullRangeDisplay = Show(
        o2FullRange, renderView1, "GeometryRepresentation"
    )

    # get color transfer function/color map for 'O2'
    o2LUT = GetColorTransferFunction("O2")
    o2LUT.RGBPoints = [
        0.22777777910232544,
        0.27450980392156865,
        0.7450980392156863,
        1.0,
        0.2300751507282257,
        0.0,
        0.2901960784313726,
        0.7529411764705882,
    ]
    o2LUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    o2FullRangeDisplay.Representation = "Surface"
    o2FullRangeDisplay.ColorArrayName = ["POINTS", "O2"]
    o2FullRangeDisplay.LookupTable = o2LUT
    o2FullRangeDisplay.Opacity = 0.1
    o2FullRangeDisplay.SelectTCoordArray = "None"
    o2FullRangeDisplay.SelectNormalArray = "Normals"
    o2FullRangeDisplay.SelectTangentArray = "None"
    o2FullRangeDisplay.OSPRayScaleArray = "O2"
    o2FullRangeDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    o2FullRangeDisplay.SelectOrientationVectors = "None"
    o2FullRangeDisplay.ScaleFactor = 119.80000000000001
    o2FullRangeDisplay.SelectScaleArray = "O2"
    o2FullRangeDisplay.GlyphType = "Arrow"
    o2FullRangeDisplay.GlyphTableIndexArray = "O2"
    o2FullRangeDisplay.GaussianRadius = 5.99
    o2FullRangeDisplay.SetScaleArray = ["POINTS", "O2"]
    o2FullRangeDisplay.ScaleTransferFunction = "PiecewiseFunction"
    o2FullRangeDisplay.OpacityArray = ["POINTS", "O2"]
    o2FullRangeDisplay.OpacityTransferFunction = "PiecewiseFunction"
    o2FullRangeDisplay.DataAxesGrid = "GridAxesRepresentation"
    o2FullRangeDisplay.PolarAxes = "PolarAxesRepresentation"

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    o2FullRangeDisplay.ScaleTransferFunction.Points = [
        0.22777777910232544,
        0.0,
        0.5,
        0.0,
        0.23000000417232513,
        1.0,
        0.5,
        0.0,
    ]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    o2FullRangeDisplay.OpacityTransferFunction.Points = [
        0.22777777910232544,
        0.0,
        0.5,
        0.0,
        0.23000000417232513,
        1.0,
        0.5,
        0.0,
    ]

    # show data from thetaWarmFire
    thetaWarmFireDisplay = Show(
        thetaWarmFire, renderView1, "GeometryRepresentation"
    )

    # trace defaults for the display properties.
    thetaWarmFireDisplay.Representation = "Surface"
    thetaWarmFireDisplay.AmbientColor = [
        0.7529411764705882,
        0.2,
        0.01568627450980392,
    ]
    thetaWarmFireDisplay.ColorArrayName = [None, ""]
    thetaWarmFireDisplay.DiffuseColor = [
        0.7529411764705882,
        0.2,
        0.01568627450980392,
    ]
    thetaWarmFireDisplay.Opacity = 0.8
    thetaWarmFireDisplay.SelectTCoordArray = "None"
    thetaWarmFireDisplay.SelectNormalArray = "None"
    thetaWarmFireDisplay.SelectTangentArray = "None"
    thetaWarmFireDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    thetaWarmFireDisplay.SelectOrientationVectors = "None"
    thetaWarmFireDisplay.ScaleFactor = -2.0000000000000002e298
    thetaWarmFireDisplay.SelectScaleArray = "None"
    thetaWarmFireDisplay.GlyphType = "Arrow"
    thetaWarmFireDisplay.GlyphTableIndexArray = "None"
    thetaWarmFireDisplay.GaussianRadius = -1e297
    thetaWarmFireDisplay.SetScaleArray = [None, ""]
    thetaWarmFireDisplay.ScaleTransferFunction = "PiecewiseFunction"
    thetaWarmFireDisplay.OpacityArray = [None, ""]
    thetaWarmFireDisplay.OpacityTransferFunction = "PiecewiseFunction"
    thetaWarmFireDisplay.DataAxesGrid = "GridAxesRepresentation"
    thetaWarmFireDisplay.PolarAxes = "PolarAxesRepresentation"

    # show data from fire
    fireDisplay = Show(fire, renderView1, "GeometryRepresentation")

    # trace defaults for the display properties.
    fireDisplay.Representation = "Surface"
    fireDisplay.AmbientColor = [1.0, 0.3333333333333333, 0.0]
    fireDisplay.ColorArrayName = [None, ""]
    fireDisplay.DiffuseColor = [1.0, 0.3333333333333333, 0.0]
    fireDisplay.Opacity = 0.09
    fireDisplay.SelectTCoordArray = "None"
    fireDisplay.SelectNormalArray = "None"
    fireDisplay.SelectTangentArray = "None"
    fireDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    fireDisplay.SelectOrientationVectors = "None"
    fireDisplay.ScaleFactor = -2.0000000000000002e298
    fireDisplay.SelectScaleArray = "None"
    fireDisplay.GlyphType = "Arrow"
    fireDisplay.GlyphTableIndexArray = "None"
    fireDisplay.GaussianRadius = -1e297
    fireDisplay.SetScaleArray = [None, ""]
    fireDisplay.ScaleTransferFunction = "PiecewiseFunction"
    fireDisplay.OpacityArray = [None, ""]
    fireDisplay.OpacityTransferFunction = "PiecewiseFunction"
    fireDisplay.DataAxesGrid = "GridAxesRepresentation"
    fireDisplay.PolarAxes = "PolarAxesRepresentation"

    # show data from hotFire
    hotFireDisplay = Show(hotFire, renderView1, "GeometryRepresentation")

    # trace defaults for the display properties.
    hotFireDisplay.Representation = "Surface"
    hotFireDisplay.AmbientColor = [
        0.7058823529411765,
        0.2235294117647059,
        0.00392156862745098,
    ]
    hotFireDisplay.ColorArrayName = [None, ""]
    hotFireDisplay.DiffuseColor = [
        0.7058823529411765,
        0.2235294117647059,
        0.00392156862745098,
    ]
    hotFireDisplay.SelectTCoordArray = "None"
    hotFireDisplay.SelectNormalArray = "None"
    hotFireDisplay.SelectTangentArray = "None"
    hotFireDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    hotFireDisplay.SelectOrientationVectors = "None"
    hotFireDisplay.ScaleFactor = -2.0000000000000002e298
    hotFireDisplay.SelectScaleArray = "None"
    hotFireDisplay.GlyphType = "Arrow"
    hotFireDisplay.GlyphTableIndexArray = "None"
    hotFireDisplay.GaussianRadius = -1e297
    hotFireDisplay.SetScaleArray = [None, ""]
    hotFireDisplay.ScaleTransferFunction = "PiecewiseFunction"
    hotFireDisplay.OpacityArray = [None, ""]
    hotFireDisplay.OpacityTransferFunction = "PiecewiseFunction"
    hotFireDisplay.DataAxesGrid = "GridAxesRepresentation"
    hotFireDisplay.PolarAxes = "PolarAxesRepresentation"

    # show data from warmSmoke
    warmSmokeDisplay = Show(warmSmoke, renderView1, "GeometryRepresentation")

    # trace defaults for the display properties.
    warmSmokeDisplay.Representation = "Surface"
    warmSmokeDisplay.AmbientColor = [
        0.35294117647058826,
        0.35294117647058826,
        0.35294117647058826,
    ]
    warmSmokeDisplay.ColorArrayName = [None, ""]
    warmSmokeDisplay.DiffuseColor = [
        0.35294117647058826,
        0.35294117647058826,
        0.35294117647058826,
    ]
    warmSmokeDisplay.Opacity = 0.01
    warmSmokeDisplay.SelectTCoordArray = "None"
    warmSmokeDisplay.SelectNormalArray = "None"
    warmSmokeDisplay.SelectTangentArray = "None"
    warmSmokeDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    warmSmokeDisplay.SelectOrientationVectors = "None"
    warmSmokeDisplay.ScaleFactor = -2.0000000000000002e298
    warmSmokeDisplay.SelectScaleArray = "None"
    warmSmokeDisplay.GlyphType = "Arrow"
    warmSmokeDisplay.GlyphTableIndexArray = "None"
    warmSmokeDisplay.GaussianRadius = -1e297
    warmSmokeDisplay.SetScaleArray = [None, ""]
    warmSmokeDisplay.ScaleTransferFunction = "PiecewiseFunction"
    warmSmokeDisplay.OpacityArray = [None, ""]
    warmSmokeDisplay.OpacityTransferFunction = "PiecewiseFunction"
    warmSmokeDisplay.DataAxesGrid = "GridAxesRepresentation"
    warmSmokeDisplay.PolarAxes = "PolarAxesRepresentation"

    # show data from convectiveHeatTransfer
    convectiveHeatTransferDisplay = Show(
        convectiveHeatTransfer, renderView1, "GeometryRepresentation"
    )

    # get color transfer function/color map for 'convht_1'
    convht_1LUT = GetColorTransferFunction("convht_1")
    convht_1LUT.RGBPoints = [
        -44.430938720703125,
        0.3764705882352941,
        0.23137254901960785,
        0.0,
        -12.401758193969727,
        0.28627450980392155,
        0.0,
        0.0,
        19.627422332763672,
        0.0,
        0.0,
        0.0,
    ]
    convht_1LUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    convectiveHeatTransferDisplay.Representation = "Surface"
    convectiveHeatTransferDisplay.ColorArrayName = ["POINTS", "convht_1"]
    convectiveHeatTransferDisplay.LookupTable = convht_1LUT
    convectiveHeatTransferDisplay.SelectTCoordArray = "None"
    convectiveHeatTransferDisplay.SelectNormalArray = "Normals"
    convectiveHeatTransferDisplay.SelectTangentArray = "None"
    convectiveHeatTransferDisplay.OSPRayScaleArray = "convht_1"
    convectiveHeatTransferDisplay.OSPRayScaleFunction = "PiecewiseFunction"
    convectiveHeatTransferDisplay.SelectOrientationVectors = "None"
    convectiveHeatTransferDisplay.ScaleFactor = 99.80000000000001
    convectiveHeatTransferDisplay.SelectScaleArray = "convht_1"
    convectiveHeatTransferDisplay.GlyphType = "Arrow"
    convectiveHeatTransferDisplay.GlyphTableIndexArray = "convht_1"
    convectiveHeatTransferDisplay.GaussianRadius = 4.99
    convectiveHeatTransferDisplay.SetScaleArray = ["POINTS", "convht_1"]
    convectiveHeatTransferDisplay.ScaleTransferFunction = "PiecewiseFunction"
    convectiveHeatTransferDisplay.OpacityArray = ["POINTS", "convht_1"]
    convectiveHeatTransferDisplay.OpacityTransferFunction = "PiecewiseFunction"
    convectiveHeatTransferDisplay.DataAxesGrid = "GridAxesRepresentation"
    convectiveHeatTransferDisplay.PolarAxes = "PolarAxesRepresentation"

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    convectiveHeatTransferDisplay.ScaleTransferFunction.Points = [
        7.462446212768555,
        0.0,
        0.5,
        0.0,
        7.463422775268555,
        1.0,
        0.5,
        0.0,
    ]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    convectiveHeatTransferDisplay.OpacityTransferFunction.Points = [
        7.462446212768555,
        0.0,
        0.5,
        0.0,
        7.463422775268555,
        1.0,
        0.5,
        0.0,
    ]

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for rhof_1LUT in view renderView1
    rhof_1LUTColorBar = GetScalarBar(rhof_1LUT, renderView1)
    rhof_1LUTColorBar.Title = "rhof_1"
    rhof_1LUTColorBar.ComponentTitle = ""

    # set color bar visibility
    rhof_1LUTColorBar.Visibility = 1

    # get color legend/bar for windLUT in view renderView1
    windLUTColorBar = GetScalarBar(windLUT, renderView1)
    windLUTColorBar.WindowLocation = "Lower Left Corner"
    windLUTColorBar.Position = [0.0018604651162790699, 0.016493055555555556]
    windLUTColorBar.Title = "wind"
    windLUTColorBar.ComponentTitle = "Magnitude"

    # set color bar visibility
    windLUTColorBar.Visibility = 1

    # get color legend/bar for convht_1LUT in view renderView1
    convht_1LUTColorBar = GetScalarBar(convht_1LUT, renderView1)
    convht_1LUTColorBar.WindowLocation = "Upper Right Corner"
    convht_1LUTColorBar.Title = "convht_1"
    convht_1LUTColorBar.ComponentTitle = ""

    # set color bar visibility
    convht_1LUTColorBar.Visibility = 1

    # get color legend/bar for o2LUT in view renderView1
    o2LUTColorBar = GetScalarBar(o2LUT, renderView1)
    o2LUTColorBar.WindowLocation = "Upper Left Corner"
    o2LUTColorBar.Title = "O2"
    o2LUTColorBar.ComponentTitle = ""

    # set color bar visibility
    o2LUTColorBar.Visibility = 1

    # show color legend
    streamTracer1Display.SetScalarBarVisibility(renderView1, True)

    # show color legend
    bulkDensityDryFuelDisplay.SetScalarBarVisibility(renderView1, True)

    # show color legend
    o2FullRangeDisplay.SetScalarBarVisibility(renderView1, True)

    # show color legend
    convectiveHeatTransferDisplay.SetScalarBarVisibility(renderView1, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # get opacity transfer function/opacity map for 'rhof_1'
    rhof_1PWF = GetOpacityTransferFunction("rhof_1")
    rhof_1PWF.Points = [0.0, 0.0, 0.5, 0.0, 0.6000000238418579, 1.0, 0.5, 0.0]
    rhof_1PWF.ScalarRangeInitialized = 1

    # get opacity transfer function/opacity map for 'O2'
    o2PWF = GetOpacityTransferFunction("O2")
    o2PWF.Points = [
        0.22777777910232544,
        0.0,
        0.5,
        0.0,
        0.2300751507282257,
        1.0,
        0.5,
        0.0,
    ]
    o2PWF.ScalarRangeInitialized = 1

    # get opacity transfer function/opacity map for 'wind'
    windPWF = GetOpacityTransferFunction("wind")
    windPWF.Points = [3.0, 0.0, 0.5, 0.0, 28.0, 1.0, 0.5, 0.0]
    windPWF.ScalarRangeInitialized = 1

    # get opacity transfer function/opacity map for 'convht_1'
    convht_1PWF = GetOpacityTransferFunction("convht_1")
    convht_1PWF.Points = [
        -44.430938720703125,
        0.0,
        0.5,
        0.0,
        19.627422332763672,
        1.0,
        0.5,
        0.0,
    ]
    convht_1PWF.ScalarRangeInitialized = 1

    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(warmSmoke)
    # ----------------------------------------------------------------

    layout = GetLayout()
    SaveScreenshot(outp_filename, layout)

    endTime = time.time()
    executionTime = endTime - startTime
    print(f"\t render time: {executionTime}s")


if __name__ == "__main__":
    overwrite = False
    single_run_mode = True

    drive_dir = Path(
        "/Users/lucweytingh/Documents/msc_ai/svvr/datavisfinal/data.nosync/"
    )
    simulation_names = [
        "mountain_headcurve40",
        "mountain_headcurve80",
        "mountain_headcurve320",
    ]

    ts = range(5000, 91001, 1000)
    # ts = range(70000, 70001, 1000)

    for simulation in simulation_names:
        src_dir = drive_dir / simulation
        out_dir = drive_dir / f"{simulation}_closeup_out"
        out_dir.mkdir(exist_ok=True)

        for i, t in enumerate(ts, 1):
            in_fname = src_dir / f"output.{t}.vts"
            out_fname = out_dir / f"t{t}.png"
            if not in_fname.is_file():
                if not single_run_mode:
                    print(
                        f"Src file '{in_fname.relative_to(drive_dir)}' does not exist"
                    )
            elif out_fname.is_file() and overwrite is False:
                if not single_run_mode:
                    print(f"Already generated step {i}/{len(ts)} (t={t})")
            else:
                print(f"Generating step {i}/{len(ts)} (t={t})")
                try:
                    render_and_save_file(str(in_fname), str(out_fname))
                except:
                    print(f"{out_fname.relative_to(drive_dir)} may be damaged")
                    continue
                if single_run_mode:
                    sys.exit(0)
        if single_run_mode:
            sys.exit(1)
