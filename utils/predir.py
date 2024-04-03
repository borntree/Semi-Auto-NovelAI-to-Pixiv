import os
import shutil

need_dir_list = ["./output", "./output/t2i", "./output/choose_for_i2i", "./output/i2i/", "./output/pixiv", "./output/choose_for_upscale" ,"./output/upscale", "./output/mosaic", "./output/choose_to_mosaic", "./output/inpaint", "./output/inpaint/img", "./output/inpaint/mask", "./files/else_upscale_engine"]

if not os.path.exists(".env"):
    shutil.copyfile(".env.example", ".env")
for dir in need_dir_list:
    if not os.path.exists(dir):
        os.mkdir(dir)