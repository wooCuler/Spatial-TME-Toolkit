"""Spatial neighborhood enrichment and co-occurrence analysis.

Wraps squidpy's spatial graph construction, neighborhood enrichment
test (`squidpy.gr.nhood_enrichment`), and co-occurrence analysis
(`squidpy.gr.co_occurrence`).
"""

from __future__ import annotations

from anndata import AnnData


def build_spatial_neighbors(
    adata: AnnData,
    coord_type: str = "generic",
    n_neighs: int = 6,
) -> AnnData:
    """Build the spatial neighbor graph used for neighborhood analyses.

    Args:
        adata: AnnData object with spatial coordinates in `.obsm['spatial']`.
        coord_type: Coordinate type passed to `squidpy.gr.spatial_neighbors`
            (e.g. 'generic' for Xenium, 'grid' for Visium).
        n_neighs: Number of spatial neighbors per cell/spot.

    Returns:
        AnnData with spatial connectivity graph added to `.obsp`.
    """
    raise NotImplementedError


def run_nhood_enrichment(
    adata: AnnData,
    cluster_key: str = "cell_type",
    n_perms: int = 1000,
) -> dict:
    """Run squidpy's neighborhood enrichment permutation test.

    Args:
        adata: AnnData object with spatial neighbor graph built.
        cluster_key: Key in `.obs` holding cell-type/niche labels.
        n_perms: Number of permutations for the significance test.

    Returns:
        Dictionary of neighborhood enrichment z-scores as returned by
        `squidpy.gr.nhood_enrichment`.
    """
    raise NotImplementedError


def run_co_occurrence(
    adata: AnnData,
    cluster_key: str = "cell_type",
) -> dict:
    """Run squidpy's spatial co-occurrence analysis across distance intervals.

    Args:
        adata: AnnData object with spatial coordinates available.
        cluster_key: Key in `.obs` holding cell-type/niche labels.

    Returns:
        Dictionary of co-occurrence scores as returned by
        `squidpy.gr.co_occurrence`.
    """
    raise NotImplementedError
