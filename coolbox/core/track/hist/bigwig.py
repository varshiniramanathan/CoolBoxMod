from coolbox.utilities import (
    GenomeRange, get_logger
)
import oxbow as ox
from coolbox.core.track.hist.base import HistBase

import pandas as pd
import numpy as np


class BigWig(HistBase):
    """
    BigWig track

    Parameters
    ----------
    file : str
        File path of bigwig file.

    num_bins : int, optional
        Number of bins to plot the hist in current range, default 700.

    """

    DEFAULT_PROPERTIES = {
        "color": "#dfccde",
        "style": HistBase.STYLE_FILL,
        "num_bins": 700,
        "threshold": "inf"
    }

    def __init__(self, file, **kwargs):
        properties = BigWig.DEFAULT_PROPERTIES.copy()
        properties.update({
            'file': file,
            **kwargs
        })
        super().__init__(**properties)
        self.ds = ox.from_bigwig(self.properties['file'])

    def fetch_plot_data(self, gr: GenomeRange, **kwargs):
        intervals = self.fetch_data(gr, **kwargs)
        starts = intervals['start'].values
        ends = intervals['end'].values
        positions = (starts + ends) / 2  # use interval midpoints as real genomic coordinates
        values = intervals['value'].values
        return positions, values

    def fetch_data(self, gr: GenomeRange, **kwargs):
        """
        Parameters
        ----------
        gr : GenomeRange

        Returns
        -------
        intervals : pandas.core.frame.DataFrame
            BigWig interval table.
        """
        gr = self.check_chrom_name(gr, self.ds.chrom_names)

        intervals = self.ds.regions(str(gr)).pd()
        intervals_binned = bin_genomic_data(intervals, self.properties['num_bins'])
        return intervals_binned


def bin_genomic_data(
        df,
        n_bins,
        agg="mean"
):
    """
    Bin a dataframe from the fetch() method with (chrom, start, end, value) into n_bins
    equally-spaced bins spanning the genomic range's start and end.

    This is similar to pybbi's binning procedure, where the non-uniform spacing
    of a bigwig-ish file is taken into account when agg'ing.

    Parameters
    ----------
    df : dataframe as output from oxbow.from_bigwig (should be sorted)
    n_bins : int; number of equally spaced bins to produce.
    agg : {'mean', 'sum'}
        'mean' makes overlap-length-weighted average value in each bin
                  (i.e. what fraction of the bin each source interval
                  covers, times its value).
        'sum'  makes overlap-length-weighted sum: value * overlap_length,
                  summed over all intervals touching the bin.

    Returns
    -------
    pd.df which is by default in the same style as the original intervals object
    """
    if agg not in ("mean", "sum"):
        raise ValueError("agg must be 'mean' or 'sum'")

    chrom = df[chrom_col].iloc[0]

    genome_start = df[start_col].min()
    genome_end = df[end_col].max()

    bin_edges = np.linspace(genome_start, genome_end, n_bins + 1)
    bin_starts = bin_edges[:-1]
    bin_ends = bin_edges[1:]

    starts = df[start_col].to_numpy()
    ends = df[end_col].to_numpy()
    values = df[value_col].to_numpy()

    out_values = np.empty(n_bins)

    for i in range(n_bins):
        b_start, b_end = bin_starts[i], bin_ends[i]

        lo = np.searchsorted(ends, b_start, side="right")
        hi = np.searchsorted(starts, b_end, side="left")

        if lo >= hi:
            out_values[i] = 0.0  # assume empty bins are 0-valued
            continue

        seg_starts = np.maximum(starts[lo:hi], b_start)
        seg_ends = np.minimum(ends[lo:hi], b_end)
        overlap = np.clip(seg_ends - seg_starts, 0, None)
        seg_values = values[lo:hi]

        if agg == "mean":
            total_overlap = overlap.sum()  # size of the interval

            # coverage over the entire bin length
            out_values[i] = (
                (seg_values * overlap).sum() / total_overlap
                if total_overlap > 0
                else 0
            )
        else:  # sum
            out_values[i] = (seg_values * overlap).sum()

    return pd.DataFrame(
        {
            "chrom": chrom,
            "start": bin_starts.round().astype(int),
            "end": bin_ends.round().astype(int),
            "value": out_values,
        }
    )

