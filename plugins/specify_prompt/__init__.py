from pathlib import Path

import gradio as gr

from plugins.specify_prompt.utils import t2i
from utils.utils import open_folder


def plugin_template(name="模板插件", description="描述", func=None):
    with gr.Tab(name):
        with gr.Row():
            with gr.Column(scale=8):
                gr.Markdown(f"> {description}")
            folder = gr.Textbox(Path("./output/t2i"), visible=False)
            open_folder_ = gr.Button("打开保存目录", scale=1)
            open_folder_.click(open_folder, inputs=folder)
        with gr.Row():
            generate_button = gr.Button("无限生成")
            stop_button = gr.Button("停止生成")
        otp_img = gr.Image()
        cancel_event = otp_img.change(
            fn=func,
            inputs=None,
            outputs=otp_img,
            show_progress="hidden",
        )
        generate_button.click(
            fn=func,
            inputs=None,
            outputs=otp_img,
        )
        stop_button.click(None, None, None, cancels=[cancel_event])



def plugin():
    plugin_template("poimiku", "指定角色组+固定串+指定串组", t2i)
