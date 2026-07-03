# Spatial-TME-Toolkit

공개 Xenium/Visium 데이터 기반 Niche·Neighborhood 분석 재현

## 프로젝트 목적

공개된 종양 미세환경(Tumor Microenvironment, TME) 공간전사체 데이터를 활용하여,
세포 조성 기반 니치(niche) 정의와 공간적 이웃(neighborhood) 상호작용 분석
파이프라인을 재현 가능한 형태로 구현한다. 단일세포 해상도(Xenium)와
스팟 기반(Visium) 두 플랫폼에 대해 동일한 분석 논리를 적용해 비교 가능한
포트폴리오를 구성하는 것을 목표로 한다.

## 데이터 출처 (자리표시자)

- Xenium: `TBD — 10x Genomics 공개 Xenium 종양 데이터셋 (링크 예정)`
- Visium: `TBD — 10x Genomics 공개 Visium 종양 데이터셋 (링크 예정)`

## 분석 파이프라인 요약

```
QC (qc.py)
  → Cell-Type Annotation (annotation.py)
    → Ligand-Receptor Interaction (lr_interaction.py)
      → Niche Definition (niche.py)
        → Neighborhood Enrichment / Co-occurrence (neighborhood.py)
```

1. **QC**: 세포/스팟 단위 QC 지표 계산, 저품질 세포/스팟 필터링, 라이브러리 사이즈 정규화
2. **Annotation**: Leiden 클러스터링 후 마커 유전자 기반 셀타입 라벨링
3. **LR Interaction**: squidpy `ligrec`을 통한 셀타입 간 유의미한 ligand-receptor 쌍 탐색
4. **Niche**: 국소 세포 조성(composition) 기반 클러스터링으로 공간적 니치 정의
5. **Neighborhood**: squidpy `nhood_enrichment`, `co_occurrence`를 통한 니치/셀타입 간
   공간적 근접성 및 공존 패턴 분석

## English Summary

*(TBD)* This repository reproduces a niche/neighborhood analysis pipeline on
public tumor spatial transcriptomics datasets (Xenium single-cell resolution
and Visium spot-based), covering QC, cell-type annotation, ligand-receptor
interaction analysis, composition-based niche definition, and spatial
neighborhood enrichment/co-occurrence analysis.

## 방법론 한계 (Limitations)

- **니치 정의의 임의성**: 니치 개수(`n_niches`), 이웃 반경/이웃 수 등 하이퍼파라미터
  선택에 따라 니치 경계와 해석이 달라질 수 있음.
- **플랫폼 간 이질성**: Visium은 스팟당 다세포가 혼합되어 있어 단일세포 해상도인
  Xenium과 동일한 기준으로 셀타입 조성을 비교하기 어려움 (deconvolution 필요).
- **공개 데이터의 배치 효과 및 메타데이터 한계**: 서로 다른 출처의 공개 데이터를
  사용할 경우 배치 효과, 임상 정보 부족 등으로 결과 일반화에 제약이 있음.
- **LR 분석의 통계적 한계**: permutation 기반 유의성 검정은 공간적 근접성을
  직접 고려하지 않으며, 발현량 기반 추정이므로 실제 물리적 상호작용을 보장하지 않음.
- **마커 기반 어노테이션의 주관성**: 마커 유전자 세트 선택에 따라 셀타입 분류
  결과가 달라질 수 있으며, 참조 데이터셋 기반 자동 어노테이션 대비 재현성이 낮음.
