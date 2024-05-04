import random

from src.t2i import t2i_by_hand
from src.vibe import vibe, vibe_by_hand
from utils.env import env
from utils.utils import format_str, read_json, sleep_for_cool
from utils.jsondata import json_for_vibe


def character(): #指定角色词
    character = ""
    data = read_json("./plugins/specify_prompt_vibe/prompt/poimiku.json")

    character += random.choice(data["character"]) + ", "

    return format_str(character)

# 中间固定prompt
fixed_prompt = "[artist:ningen_mame],{{{ciloranko}}},[artist:sho_(sho_lwlw)],[[artist:rhasta]],[artist:wlop],[artist:ke-ta],year 2023,white background, simple background, upper body, {{cropped shoulders}}, looking at viewer,  solo,hair ornament, hairclip, {{cat costume, animal costume}}, "

def append_prompt(): #指定末尾词
    append_prompt = ""
    data = read_json("./plugins/specify_prompt_vibe/prompt/poimiku.json")

    append_prompt += random.choice(data["append"]) + ", "

    return format_str(append_prompt)    

def t2i():
    positive = character() + fixed_prompt + append_prompt()
    # data = read_json("./files/favorite.json")
    # negative = format_str(random.choice(data["negative_prompt"]["belief"]))
    negative = "nsfw,lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract], weibo watermark,{{{{{chibi,animal,doll}}}}}{{{+_+}}}"
    resolution = (
        random.choice(["832x1216"]) #"832x1216", "1024x1024", "1216x832", "896x1152"
        if env.img_size == -1
        else "{}x{}".format(env.img_size[0], env.img_size[1])
    )
    scale = 5 #env.scale
    sampler = env.sampler
    noise_schedule = "k_euler" #k_euler k_euler_ancestral
    steps = 28 #env.steps
    sm = False #env.sm
    sm_dyn = False #env.sm_dyn
    seed = random.randint(1000000000, 9999999999) if env.seed == -1 else env.seed
    input_imgs = "./plugins/specify_prompt_vibe/vibes"
    img = vibe_by_hand(positive, negative, resolution, scale, sampler, noise_schedule, steps, sm, sm_dyn, seed, input_imgs)
    sleep_for_cool(env.t2i_cool_time - 6, env.t2i_cool_time + 6)
    return img