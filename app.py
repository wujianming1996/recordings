import gradio as gr
from datetime import datetime
import numpy as np
from scipy.io.wavfile import write



def reverse_audio(audio):
    sr, data = audio

    # 录制音频，直到停止按钮被按下，并将其保存到以当前时间戳命名的文件
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    try:
        filename = f"/app/recordings/recorded_audio_{current_time}.wav"
        write(filename, sr, data.astype(np.int16))
    except:
        filename = f"recordings/recorded_audio_{current_time}.wav"
        write(filename, sr, data.astype(np.int16))

    
    # 返回反转后的音频

    return (sr, np.flipud(data))

input_audio = gr.Audio(
    sources=["microphone"],
    waveform_options=gr.WaveformOptions(
        waveform_color="#01C6FF",
        waveform_progress_color="#0066B4",
        skip_length=2,
        show_controls=False,
    ),
)

if __name__ == "__main__":
    # 创建一个 Gradio 接口
    gr.Interface(fn=reverse_audio, inputs=input_audio, outputs="audio", title="录音器").launch(server_name="0.0.0.0")









