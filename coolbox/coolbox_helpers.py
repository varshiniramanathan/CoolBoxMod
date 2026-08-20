import os
import numpy as np
from matplotlib import pyplot as plt
import cooler as clr
from coolbox.api import *
from coolbox.utilities import GenomeRange


def is_nested(x):
    if not isinstance(x, list):
        return ValueError("BigWig list should be either a list, or a nested list of lists")

    is_list = [isinstance(item, list) for item in x]

    if all(not i for i in is_list):
        return False  # not nested

    elif all(is_list):
        return True  # nested

    else:
        return ValueError("BigWig list should be either a list, or a nested list of lists")


def get_single_max(bw, region):
    # the [1] index is for compability with May 2026 release of coolbox which returns a tuple instead of a list
    return np.round(np.amax(bw.fetch_plot_data(GenomeRange(region))[1]))


def auto_scale_bigwig(bigwig_single, region, y_max=None, y_min=0):
    """
    Autoscales y axis of single bigwig based off values in `region`.
    """
    if y_max is None:
        if type(region) == list:
            y_max_list = [get_single_max(bigwig_single, single_region) for single_region in region]
            y_max = max(y_max_list)
        else:
            y_max = get_single_max(bigwig_single, region)

    return bigwig_single + MaxValue(y_max) + MinValue(y_min)

def auto_scale_bigwigs(bigwig_list, region, y_max=None, y_min=0):
    """
    Autoscales y axis of bigwigs in bigwig list based off values in `region`.
    """

    # gets max of entire list to scale a set of tracks together
    def get_max_y_value(bigwig_list, region):
        max_y_values = []
        for bigwig in bigwig_list:
            max_y_values.append(get_single_max(bigwig, region))
        y_max = round(max(max_y_values) * 1.05)
        return y_max

    if y_max is None:
        if type(region) == list:
            y_max_list = [get_max_y_value(bigwig_list, single_region) for single_region in region]
            y_max = max(y_max_list)
        else:
            y_max = get_max_y_value(bigwig_list, region)

    return [bigwig + MaxValue(y_max) + MinValue(y_min) for bigwig in bigwig_list]


def make_bigwig_list(bigwigs, region, condition_order, bw_bins=1600, track_height=2, autoscale=True,
                     y_max=None):
    """
    Helper function for `make_region_plot` that converts file paths to bigwig plotting objects.
    """
    assert len(bigwigs) % len(condition_order) == 0
    bigwig_list = [BigWig(bigwig, num_bins=bw_bins) + Title(title) \
                   + TrackHeight(track_height) for bigwig, title in zip(bigwigs, condition_order)]
    if autoscale:
        bigwig_list = auto_scale_bigwigs(bigwig_list, region, y_max=y_max)
    return bigwig_list


def cat_prefix_to_list(prefix, file_list):
    """
    Helper function that concatenates a prefix to every element
    in a list.
    """
    return [os.path.join(prefix, file) for file in file_list]

def read_cooler(cooler_path, resolution=250):
    """
    Simple function wrapper to read cooler file at a particular resolution.
    """
    if clr.fileops.is_cooler(cooler_path):
        return clr.Cooler(cooler_path)
    elif clr.fileops.is_multires_file(cooler_path):
        return clr.Cooler(cooler_path + "::resolutions/" + str(int(resolution)))


