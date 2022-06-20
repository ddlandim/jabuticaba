import numpy as np

def get_long_tail(long):
    if long is None or long <= -1:
        return np.nan
    else:
        return np.log(1+long)


def get_total_pixels(pixels):
    if (pixels is None) | (type(pixels) != str):
        return None
    elif ('x' not in pixels) | (len(pixels.split('x'))<= 1):
        return None
    return float(pixels.split('x')[0])*float(pixels.split('x')[1])


ceil = lambda x: 1 if x >= 1 else x

def default_fn():
    pass

functions_dict = {
    "get_long_tail" : get_long_tail,
    "get_total_pixels" : get_total_pixels,
    "ceil" : ceil,
    "default" : default_fn
}

functions_cl_name = {
    "get_long_tail" : "log_",
    "get_total_pixels" : "total_pixels",
    "ceil" : "ceil_",
    "default" : ""
}