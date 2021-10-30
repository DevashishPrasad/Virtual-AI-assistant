import json
import torch
import numpy as np
import sys
import sounddevice as sd

from flowtron import Flowtron
from data import Data

from SimpleFace import audio2mouth

sys.path.insert(0, 'flowtron/tacotron2')
sys.path.insert(0, 'flowtron/tacotron2/waveglow')

from glow import WaveGlow

import scipy.io.wavfile
import os
abspath = os.path.abspath(__file__)
i = abspath.rfind('flowtron')+9
abspath = abspath[:i]
class FlowAPI():

    def __init__(self): 

        flowtron_pretrained_model = abspath+'flowtron_libritts.pt'
        waveglow_pretrained_model = abspath+'waveglow_256channels_universal_v5.pt'
        
        torch.manual_seed(1234)
        torch.cuda.manual_seed(1234)
        torch.backends.cudnn.enabled = True
        torch.backends.cudnn.benchmark = False

        # read self.config
        config = json.load(open(abspath+'config.json'))
        data_config = config["data_config"]
        model_config = config["model_config"]
        model_config['n_speakers'] = 123 # there are 123 speakers
        data_config['training_files'] = abspath+'filelists/libritts_train_clean_100_audiopath_text_sid_shorterthan10s_atleast5min_train_filelist.txt'
        data_config['validation_files'] = data_config['training_files']
        print("\n\n\n\n",data_config['training_files'],"\n\n\n\n\n")
        # load waveglow
        self.waveglow = torch.load(waveglow_pretrained_model)['model'].cuda().eval()
        self.waveglow.cuda()
        for k in self.waveglow.convinv:
            k.float()
        _ = self.waveglow.eval()

        # load flowtron
        self.model = Flowtron(**model_config).cuda()
        state_dict = torch.load(flowtron_pretrained_model, map_location='cpu')['state_dict']
        self.model.load_state_dict(state_dict)
        _ = self.model.eval()

        ignore_keys = ['training_files', 'validation_files']
        self.trainset = Data(data_config['training_files'], **dict((k, v) for k, v in data_config.items() if k not in ignore_keys))

    def synthesize(self, speaker_id, text, sigma=0.5, n_frames=1500):
      speaker_vecs = self.trainset.get_speaker_id(speaker_id).cuda()
      text = self.trainset.get_text(text).cuda()
      speaker_vecs = speaker_vecs[None]
      text = text[None]

      with torch.no_grad():
        residual = torch.cuda.FloatTensor(1, 80, n_frames).normal_() * sigma
        mels, attentions = self.model.infer(residual, speaker_vecs, text)

      audio = self.waveglow.infer(mels, sigma=0.8).float()
      audio = audio.cpu().numpy()[0]

      audio2mouth(22050, audio)

# print("\n\n\n","SUCCESSS","\n\n\n\n\n")
# # fp = FlowAPI()
# # # available speaker ids: 1069, 1088, 1116, 118, 1246, 125, 1263, 1502, 1578, 1841, 1867, 196, 1963, 1970, 200, 2092, 2136, 2182, 2196, 2289, 2416, 2436, 250, 254, 2836, 2843, 2911, 2952, 3240, 3242, 3259, 3436, 3486, 3526, 3664, 374, 3857, 3879, 3982, 3983, 40, 4018, 405, 4051, 4088, 4160, 4195, 4267, 4297, 4362, 4397, 4406, 446, 460, 4640, 4680, 4788, 5022, 5104, 5322, 5339, 5393, 5652, 5678, 5703, 5750, 5808, 587, 6019, 6064, 6078, 6081, 6147, 6181, 6209, 6272, 6367, 6385, 6415, 6437, 6454, 6476, 6529, 669, 6818, 6836, 6848, 696, 7059, 7067, 7078, 7178, 7190, 7226, 7278, 730, 7302, 7367, 7402, 7447, 7505, 7511, 7794, 78, 7800, 8051, 8088, 8098, 8108, 8123, 8238, 83, 831, 8312, 8324, 8419, 8468, 8609, 8629, 87, 8770, 8838, 887
# # SPEAKER_ID = 196  # 196 is a male voice & 1246 is a female voice
# # fp.synthesize(speaker_id=1246,text="Today is my interview.")