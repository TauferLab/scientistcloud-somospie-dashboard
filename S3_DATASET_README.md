# ScientistCloud SOMOSPIE Terrain Parameters Dataset

This dataset contains high-resolution terrain parameter GeoTIFF products generated for U.S. states as part of the SOMOSPIE/GEOtiled workflow. The files are organized by spatial resolution, state, and terrain parameter. They can be downloaded directly as GeoTIFF files or converted to OpenVisus IDX for interactive exploration through the ScientistCloud SOMOSPIE dashboard notebook.

## Dataset Summary

| Item | Description |
| --- | --- |
| Dataset family | SOMOSPIE terrain parameter products |
| Spatial resolutions | `10m` and `30m` |
| Spatial organization | Per U.S. state |
| File format | GeoTIFF (`.tif`) and selected vector/grid archives (`.zip`) |
| Primary use | Terrain analysis, hydrology preprocessing, visualization, and IDX conversion |
| NoData value | Commonly `-999999` in raster products |
| Recommended repository | <https://github.com/TauferLab/scientistcloud-somospie-dashboard> |

The public ScientistCloud dataset identifiers are:

| Resolution | ScientistCloud Dataset ID |
| --- | --- |
| `10m` | `7d796ffa-2489-40b1-b3f4-fa6c0de7b1fe` |
| `30m` | `2814af5e-0ca7-49fe-ae9b-f5f2e8c2f538` |

## Generation Workflow

These datasets were generated using GEOtiled:

- GEOtiled repository: <https://github.com/TauferLab/GEOtiled>
- Paper: **GEOtiled-SG: A Scalable Framework for High-Resolution Terrain Parameter Computation**
- DOI: <https://doi.org/10.1109/eScience65000.2025.00019>

GEOtiled computes terrain parameters from digital elevation data using a scalable tiling workflow. The resulting products are published here as state-level raster outputs at multiple resolutions.

## Bucket Layout

The dataset is organized with this logical layout:

```text
utk/conus/
  10m/
    <STATE>/
      elevation.tif
      hillshade.tif
      aspect.tif
      slope.tif
      plan_curvature.tif
      profile_curvature.tif
      ...
  30m/
    <STATE>/
      elevation.tif
      hillshade.tif
      aspect.tif
      slope.tif
      plan_curvature.tif
      profile_curvature.tif
      ...
```

`<STATE>` is the two-letter state abbreviation, for example `TN`, `CA`, `AL`, or `GA`.

## Common Terrain Parameters

Available files may vary slightly by resolution or state, but the state folders commonly include:

| File | Description |
| --- | --- |
| `elevation.tif` | Elevation surface |
| `hillshade.tif` | Hillshade / shaded relief |
| `aspect.tif` | Terrain aspect in degrees |
| `slope.tif` | Terrain slope in degrees |
| `plan_curvature.tif` | Plan curvature |
| `profile_curvature.tif` | Profile curvature |
| `convergence_index.tif` | Convergence index |
| `flow_direction.tif` | Flow direction |
| `flow_connectivity.tif` | Flow connectivity |
| `flow_width.tif` | Flow width |
| `channel_network_grid.tif` | Channel network raster grid |
| `drainage_basins_grid.tif` | Drainage basin raster grid |
| `channel_network.zip` | Channel network archive |
| `drainage_basins.zip` | Drainage basin archive |

For quick dashboard exploration, start with:

- `hillshade`
- `slope`
- `elevation`
- `aspect`
- `plan_curvature`

## Converting To IDX And Visualizing

Use the standalone dashboard notebook repository:

<https://github.com/TauferLab/scientistcloud-somospie-dashboard>

The notebook:

1. Downloads selected GeoTIFF files from ScientistCloud, or reads them from local storage.
2. Uses GDAL to inspect metadata and read raster data.
3. Converts selected terrain parameters into a multi-field OpenVisus IDX dataset.
4. Validates the IDX with a low-resolution preview.
5. Launches an interactive OpenVisus dashboard for visualization.

### Recommended Setup

```bash
git clone https://github.com/TauferLab/scientistcloud-somospie-dashboard.git
cd scientistcloud-somospie-dashboard

conda create -n scientistcloud-idx python=3.10 gdal=3.8.4 pip
conda activate scientistcloud-idx
pip install -r requirements.txt

python -m pip install ipykernel jupyterlab
python -m ipykernel install --user --name scientistcloud-idx --display-name "ScientistCloud IDX"
jupyter lab
```

Open:

```text
Transform_ScientistCloud_to_IDX.ipynb
```

Select the `ScientistCloud IDX` kernel.

### Notebook Configuration

Edit the notebook configuration cell:

```python
RESOLUTION = "30m"
STATE = "TN"
FIELDS = ["elevation", "hillshade", "aspect", "slope", "plan_curvature"]
SOURCE_MODE = "local_or_download"
```

Supported values:

- `RESOLUTION`: `10m` or `30m`
- `STATE`: two-letter state abbreviation
- `FIELDS`: list of terrain parameters without `.tif`
- `SOURCE_MODE`:
  - `local_or_download`: reuse local files when present, otherwise download.
  - `download`: download selected files.
  - `local`: require files to already exist locally.

Generated files are stored by default under:

```text
data/tif/<resolution>/<state>/
data/idx/
logs/dashboard.log
```

## Dashboard Notes

After launching the notebook dashboard, open:

```text
http://localhost:8989/dashboard
```

Use `localhost`, not `0.0.0.0`, in the browser.

If the map appears only as a state silhouette, the color range is likely including the NoData value `-999999`. Change the dashboard `Range` control from dynamic to manual/user and start with:

| Field | Min | Max |
| --- | ---: | ---: |
| `elevation` | `0` | `2000` |
| `hillshade` | `0` | `255` |
| `aspect` | `0` | `360` |
| `slope` | `0` | `70` |
| `plan_curvature` | `-0.05` | `0.05` |

## Citation

If you use this dataset or workflow, please cite:

```
Laboy, Gabriel, Ian Lumsden, Paula Olaya, Jack Marquez, Kin Wai NG, Rodrigo Vargas, and Michela Taufer. "GEOtiled-SG: A Scalable Framework for High-Resolution Terrain Parameter Computation." In 2025 IEEE International Conference on eScience (eScience), pp. 84-92. IEEE, 2025.
```

### BibTex
```
@INPROCEEDINGS{11181531,
  author={Laboy, Gabriel and Lumsden, Ian and Olaya, Paula and Marquez, Jack and N G, Kin Wai and Vargas, Rodrigo and Taufer, Michela},
  booktitle={2025 IEEE International Conference on eScience (eScience)}, 
  title={GEOtiled-SG: A Scalable Framework for High-Resolution Terrain Parameter Computation}, 
  year={2025},
  volume={},
  number={},
  pages={84-92},
  doi={10.1109/eScience65000.2025.00019}}
```

## Contact And Issues

Email: mtaufer@utk.edu

For notebook, conversion, or dashboard issues, use the GitHub repository:

<https://github.com/TauferLab/scientistcloud-somospie-dashboard/issues>

