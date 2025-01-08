# coding=utf-8

import sys

import dashscope
from dashscope.audio.tts import SpeechSynthesizer

dashscope.api_key = 'sk-7ed7b7188ce34b1e9acaf36b464191b6'

# 尝试使用 'sambert-zhina-v1' 模型
result = SpeechSynthesizer.call(model='sambert-zhina-v1',
                                text='今天天气怎么样',
                                sample_rate=48000,
                                format='wav')

if result.get_audio_data() is not None:
    with open('output.wav', 'wb') as f:
        f.write(result.get_audio_data())
    print('SUCCESS: get audio data: %d bytes in output.wav' %
          (sys.getsizeof(result.get_audio_data())))
else:
    print('ERROR: response is %s' % (result.get_response()))