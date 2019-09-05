from PIL import Image
import os


def compress_image(src_path, dst_path, ws, hs):
    # 如果是文件就处理
    if os.path.isfile(src_path):
        src_image = Image.open(src_path)
        src_image = src_image.convert("RGBA")
        w, h = src_image.size
        print(w, h)
        print(src_image.mode)
        dst_image = src_image.resize((ws, hs), Image.BILINEAR)
        dst_image.save(dst_path)
        print(dst_path + " compressed succeeded")


def compress_image_ratio(src_path, dst_path, hs):
    # 如果是文件就处理
    if os.path.isfile(src_path):
        src_image = Image.open(src_path)
        src_image = src_image.convert("RGBA")
        w, h = src_image.size
        ws = round(hs * (w / h))
        print(w, h)
        print(ws, hs)
        dst_image = src_image.resize((ws, hs), Image.BILINEAR)
        dst_image.save(dst_path)
        print(dst_path + " compressed succeeded")


def find_images(dir):
    images = []
    for fn in os.listdir(dir):
        if fn.endswith(".jpg") or fn.endswith(".png"):
            images.append(os.path.join(dir, fn))
    return images


def prepare_dir(dst):
    resolution = ['m', 'h', 'xh', 'xxh', 'xxxh']
    resolution_dir = []
    for re in resolution:
        dir = os.path.join(dst, "drawable-" + re + "dpi")
        resolution_dir.append(dir)
        if not os.path.exists(dir):
            os.makedirs(dir)
    # for re in resolution:
    #     dir = os.path.join(dst, "mipmap-" + re + "dpi")
    #     resolution_dir.append(dir)
    #     if not os.path.exists(dir):
    #         os.makedirs(dir)
    return resolution_dir


work_dir = os.path.join("E:", os.sep, "studying", "android-drawable")
dst_dirs = prepare_dir(work_dir)
src_images = find_images(work_dir)

for src in src_images:
    for i in range(len(dst_dirs)):
        if i == 0:
            compress_image_ratio(src, os.path.join(dst_dirs[i], os.path.split(src)[1]), 48)
        if i == 1:
            compress_image_ratio(src, os.path.join(dst_dirs[i], os.path.split(src)[1]), 72)
        if i == 2:
            compress_image_ratio(src, os.path.join(dst_dirs[i], os.path.split(src)[1]), 96)
        if i == 3:
            compress_image_ratio(src, os.path.join(dst_dirs[i], os.path.split(src)[1]), 144)
        if i == 4:
            compress_image_ratio(src, os.path.join(dst_dirs[i], os.path.split(src)[1]), 192)
