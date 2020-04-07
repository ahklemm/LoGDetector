from fiji.plugin.trackmate import Settings
from fiji.plugin.trackmate.detection import LogDetectorFactory
import fiji.plugin.trackmate.features.FeatureFilter as FeatureFilter
from ij import IJ, WindowManager, ImagePlus
from fiji.plugin.trackmate import Model

imp = WindowManager.getCurrentImage()
#mp = IJ.openImage('https://fiji.sc/samples/FakeTracks.tif')
#imp.show()
settings = Settings()
settings.setFrom(imp)
       
# Configure detector - We use the Strings for the keys
settings.detectorFactory = LogDetectorFactory()
settings.detectorSettings = { 
    'DO_SUBPIXEL_LOCALIZATION' : True,
    'RADIUS' : 2.5,
    'TARGET_CHANNEL' : 1,
    'THRESHOLD' : 0.,
    'DO_MEDIAN_FILTERING' : False,
}  
    
# Configure spot filters - Classical filter on quality
#filter1 = FeatureFilter('QUALITY', 30, True)
#settings.addSpotFilter(filter1)

model = new Model()
trackmate = new TrackMate(model, settings)