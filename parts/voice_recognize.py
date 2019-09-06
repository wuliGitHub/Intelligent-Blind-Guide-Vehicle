#_*_ coding:UTF-8 _*_
# @author: zdl 
# 对本地录音文件进行语音识别，将识别结果保存至txt文本中，对txt文本进行语音合成生成mp3文件


# 导入AipSpeech  AipSpeech是语音识别的Python SDK客户端
from aip import AipSpeech



''' 你的APPID AK SK  参数在申请的百度云语音服务的控制台查看'''
APP_ID = '16704715'
API_KEY = 'Axgmx7PhEADcl4wwGfnNjDEi'
SECRET_KEY = 'dF3k0it96jyTmq6wt0mbbjPrGANKDHjo'

# 新建一个AipSpeech
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
  
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件并合成
def identify_synthesize(fileName):
    result = client.asr(get_file_content(fileName), 
			    'wav', 16000, 
			    {'dev_pid': 1536,})
    if 'result' in result:
        print (result['result'][0])
        RES=result['result'][0]
    else :
        print ("识别失败")
        RES='识别失败‘'
    with open('result.txt','w') as f:
        f.write(RES)

if __name__ == '__main__':

    identify_synthesize('yahboom.wav')
	
