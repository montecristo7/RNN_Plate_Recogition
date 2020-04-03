from models.resnet import CNN_radar_resnet
from models.simple import CNN_radar_simple
from models.simpleS import CNN_radar_simpleS
from models.simpleSS import CNN_radar_simpleSS
from models.resnetS import CNN_radar_resnetS
from models.simpleL import CNN_radar_simpleL
from models.complexFunc import *
from models.Csimple import *
from models.resnetSS import CNN_radar_resnetSS
from models.CsimpleS import *
from models.CsimpleSS import *
from models.CsimpleSSS import *
from models.resnetL import *

def create_model(model_name, in_channels, out_channels):
    if model_name=='resnet':
        model = CNN_radar_resnet(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'simple':
        model = CNN_radar_simple(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'resnetS':
        model = CNN_radar_resnetS(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'simpleS':
        model = CNN_radar_simpleS(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'simpleSS':
        model = CNN_radar_simpleSS(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'simpleL':
        model = CNN_radar_simpleL(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'Csimple':
        model = ComplexNet_Simple(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'resnetSS':
        model = CNN_radar_resnetSS(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'CsimpleS':
        model = ComplexNet_SimpleS(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'CsimpleSS':
        model = ComplexNet_SimpleSS(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'CsimpleSSS':
        model = ComplexNet_SimpleSSS(in_channels=in_channels, out_channels=out_channels)
    elif model_name == 'resnetL':
        model = CNN_radar_resnetL(in_channels=in_channels, out_channels=out_channels)
    return model