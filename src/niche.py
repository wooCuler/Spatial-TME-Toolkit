"""Niche definition based on local cell-type composition.

Covers computing neighborhood cell-type composition per cell/spot
and clustering that composition into spatial niches.
"""

from __future__ import annotations

import pandas as pd
from anndata import AnnData


def compute_cell_type_composition(
    adata: AnnData,
    cluster_key: str = "cell_type",
    spatial_key: str = "spatial",
    radius: float | None = None,
    n_neighbors: int = 20,
) -> pd.DataFrame:
    """Compute local cell-type composition within each cell/spot's neighborhood.

    Args:
        adata: Annotated AnnData object with cell-type labels and coordinates.
        cluster_key: Key in `.obs` holding cell-type/cluster labels.
        spatial_key: Key in `.obsm` holding spatial coordinates.
        radius: Radius (in coordinate units) defining the local neighborhood.
            If None, `n_neighbors` is used instead.
        n_neighbors: Number of nearest neighbors defining the local
            neighborhood when `radius` is not provided.

    Returns:
        DataFrame (cells/spots x cell types) of local composition fractions.
    """
    raise NotImplementedError


def define_niches(
    composition_df: pd.DataFrame,
    n_niches: int = 10,
    random_state: int = 0,
) -> pd.Series:
    """Cluster cell-type composition vectors into spatial niches.

    Args:
        composition_df: Output of `compute_cell_type_composition`.
        n_niches: Number of niche clusters to define (e.g. via K-means).
        random_state: Random seed for reproducibility.

    Returns:
        Series mapping each cell/spot index to a niche label.
    """
    raise NotImplementedError


def assign_niche_labels(adata: AnnData, niche_labels: pd.Series) -> AnnData:
    """Attach niche labels to an AnnData object.

    Args:
        adata: AnnData object to annotate.
        niche_labels: Output of `define_niches`, indexed like `adata.obs`.

    Returns:
        AnnData with niche labels added to `.obs['niche']`.
    """
    raise NotImplementedError
