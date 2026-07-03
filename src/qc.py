"""Quality control utilities for spatial transcriptomics data.

Covers per-cell/per-spot QC metric computation, low-quality
cell/spot filtering, and count normalization prior to downstream
clustering and annotation steps.
"""

from __future__ import annotations

from anndata import AnnData


def compute_qc_metrics(adata: AnnData, mito_prefix: str = "MT-") -> AnnData:
    """Compute per-cell/per-spot QC metrics (total counts, n_genes, mito fraction).

    Args:
        adata: Input AnnData object (raw counts expected in `.X`).
        mito_prefix: Gene name prefix used to flag mitochondrial genes.

    Returns:
        AnnData with QC metrics added to `.obs` (e.g. total_counts,
        n_genes_by_counts, pct_counts_mt).
    """
    raise NotImplementedError


def filter_cells(
    adata: AnnData,
    min_counts: int = 10,
    min_genes: int = 3,
    max_pct_mito: float | None = None,
) -> AnnData:
    """Filter out low-quality cells/spots based on QC thresholds.

    Args:
        adata: Input AnnData object, ideally after `compute_qc_metrics`.
        min_counts: Minimum total counts required to keep a cell/spot.
        min_genes: Minimum number of detected genes required.
        max_pct_mito: Optional upper bound on mitochondrial read percentage.

    Returns:
        Filtered AnnData object.
    """
    raise NotImplementedError


def normalize_counts(
    adata: AnnData,
    target_sum: float | None = None,
    log1p: bool = True,
) -> AnnData:
    """Normalize counts by library size and optionally log-transform.

    Args:
        adata: Filtered AnnData object with raw counts in `.X`.
        target_sum: Target total count per cell/spot for normalization.
            If None, uses the median of total counts across cells.
        log1p: Whether to apply log1p transformation after normalization.

    Returns:
        AnnData with normalized (and optionally log-transformed) `.X`.
    """
    raise NotImplementedError
