"""Clustering and marker-based cell-type annotation utilities.

Covers Leiden clustering on the normalized expression graph and
downstream marker-gene-based annotation of clusters to cell types.
"""

from __future__ import annotations

from anndata import AnnData


def run_leiden_clustering(
    adata: AnnData,
    resolution: float = 1.0,
    n_pcs: int = 50,
    n_neighbors: int = 15,
) -> AnnData:
    """Run PCA, neighbor graph construction, and Leiden clustering.

    Args:
        adata: Normalized AnnData object.
        resolution: Leiden resolution parameter controlling cluster granularity.
        n_pcs: Number of principal components used to build the neighbor graph.
        n_neighbors: Number of neighbors used to build the kNN graph.

    Returns:
        AnnData with cluster labels added to `.obs['leiden']`.
    """
    raise NotImplementedError


def score_marker_genes(
    adata: AnnData,
    marker_dict: dict[str, list[str]],
) -> AnnData:
    """Score cells/spots for each cell-type marker gene set.

    Args:
        adata: AnnData object with normalized expression.
        marker_dict: Mapping from cell-type name to list of marker gene names.

    Returns:
        AnnData with per-cell-type marker scores added to `.obs`.
    """
    raise NotImplementedError


def annotate_cell_types(
    adata: AnnData,
    marker_dict: dict[str, list[str]],
    cluster_key: str = "leiden",
) -> AnnData:
    """Assign cell-type labels to clusters based on marker gene scores.

    Args:
        adata: AnnData object with cluster labels and marker scores available.
        marker_dict: Mapping from cell-type name to list of marker gene names.
        cluster_key: Key in `.obs` holding cluster assignments.

    Returns:
        AnnData with cell-type labels added to `.obs['cell_type']`.
    """
    raise NotImplementedError
