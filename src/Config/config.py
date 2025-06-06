
#语音配置
class VoiceConfig:
    voice: str          #声音
    rate: int           # 语速
    volume: float       # 音量
    pitch: int          # 音高 (0-100)
    interruptible: bool # 是否可被更高优先级打断
    save_to_file: bool  # 是否保存语音到文件
    output_dir: str     # 语音文件输出目录

    def __init__(self):
        self.voice="zh-CN-XiaoxiaoNeural"
        self.rate=0
        self.volume=100
        self.pitch=50
        self.interruptible=True
        self.save_to_file=False
        self.output_dir="output"


    def setVoice(self, voice):
        self.voice=voice
    def setRate(self, rate):
        self.rate=rate
    def setVolume(self, volume):
        self.volume=volume
    def setPitch(self, pitch):
        self.pitch=pitch
    def setInterruptible(self, interruptible):
        self.interruptible=interruptible
    def setSaveToFile(self, save_to_file):
        self.save_to_file=save_to_file
    def setOutputDir(self, output_dir):
        self.output_dir=output_dir
    def getVoice(self):
        return self.voice
    def getRate(self):
        return self.rate
    def getVolume(self):
        return self.volume
    def getPitch(self):
        return self.pitch
    def getInterruptible(self):
        return self.interruptible
    def getSaveToFile(self):
        return self.save_to_file
    def getOutputDir(self):
        return self.output_dir


class Config:
    vc: VoiceConfig

    def loadConfig(self):
        self.vc=VoiceConfig()



