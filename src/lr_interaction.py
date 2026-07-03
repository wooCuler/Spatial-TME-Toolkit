"""Ligand-receptor interaction analysis utilities.

Wraps squidpy's permutation-based ligand-receptor interaction test
(`squidpy.gr.ligrec`) and provides result summarization helpers.
"""

from __future__ import annotations

import pandas as pd
from anndata import AnnData


def run_ligrec(
    adata: AnnData,
    cluster_key: str = "cell_type",
    n_perms: int = 1000,
) -> dict:
    """Run squidpy's ligand-receptor interaction analysis (CellPhoneDB-style).

    Args:
        adata: Annotated AnnData object with cell-type labels.
        cluster_key: Key in `.obs` holding cell-type/cluster labels used
            to group cells for interaction testing.
        n_perms: Number of permutations for the significance test.

    Returns:
        Dictionary of ligrec results as returned by `squidpy.gr.ligrec`
        (containing 'means' and 'pvalues' DataFrames).
    """
    raise NotImplementedError


def summarize_lr_results(
    ligrec_result: dict,
    pval_threshold: float = 0.05,
) -> pd.DataFrame:
    """Summarize significant ligand-receptor pairs from ligrec output.

    Args:
        ligrec_result: Output dictionary from `run_ligrec`.
        pval_threshold: P-value threshold for significance filtering.

    Returns:
        DataFrame of significant ligand-receptor pairs per cluster pair.
    """
    raise NotImplementedError
