# ScientistCloud GDAL-to-IDX Dashboard

This standalone notebook downloads terrain-parameter GeoTIFF files from the public ScientistCloud CONUS datasets, reads them with GDAL, converts selected fields to an OpenVisus IDX dataset, validates the result, and launches the OpenVisus dashboard.

Default example:

- Resolution: `30m`
- State: `TN`
- Fields: `elevation`, `hillshade`, `aspect`, `slope`, `plan_curvature`

## Setup

Python 3.10 is recommended. Install GDAL with Conda, then install the Python requirements with pip:

```bash
conda create -n scientistcloud-idx python=3.10 gdal=3.8.4 pip
conda activate scientistcloud-idx
pip install -r requirements.txt
```

If you must use pip-only installation, install a GDAL wheel compatible with your system before running the notebook. GDAL installed only through pip can be fragile because it depends on native GDAL libraries.

If you installed the requirements before `param==2.0.2` was pinned, refresh the environment with:

```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

To use the environment in Jupyter:

```bash
python -m pip install ipykernel jupyterlab
python -m ipykernel install --user --name scientistcloud-idx --display-name "ScientistCloud IDX"
jupyter lab
```

Open `Transform_ScientistCloud_to_IDX.ipynb` and select the `ScientistCloud IDX` kernel.

## Running The Notebook

The notebook stores files locally under:

- TIFF downloads: `data/tif/<resolution>/<state>/`
- IDX output: `data/idx/`
- Dashboard log: `logs/dashboard.log`

Run the cells in order. The dashboard cell is intentionally short:

```python
%%capture dashboard_output
launch_dashboard()
```

After the dashboard starts, open:

```text
http://localhost:8989/dashboard
```

Use `localhost`, not `0.0.0.0`, in your browser.

## Configuration

Edit the configuration cell near the top of the notebook:

```python
RESOLUTION = "30m"
STATE = "TN"
FIELDS = ["elevation", "hillshade", "aspect", "slope", "plan_curvature"]
SOURCE_MODE = "local_or_download"
```

Supported resolutions are:

- `30m`
- `10m`

The `10m` files can be many gigabytes per field. Make sure you have enough disk space before switching to `10m` or adding more fields.

`SOURCE_MODE` options:

- `local_or_download`: reuse local TIFFs when present, otherwise download them.
- `download`: download configured TIFFs even if local files already exist.
- `local`: require TIFFs to already exist locally.

## Recommended Dashboard Ranges

If the dashboard only shows the silhouette of the state, the color range is probably including the NoData value `-999999`. Change `Range` from `dynamic` to a manual/user range and use these starting values:

| Field | Min | Max |
| --- | ---: | ---: |
| `elevation` | `0` | `2000` |
| `hillshade` | `0` | `255` |
| `aspect` | `0` | `360` |
| `slope` | `0` | `70` |
| `plan_curvature` | `-0.05` | `0.05` |

For terrain interpretation, `hillshade` and `slope` usually show spatial structure most clearly at first glance. For `elevation`, keep `Mapper` as `linear` and use a palette such as `Viridis256`, `Turbo256`, or `Inferno256`.

## Troubleshooting

If the dashboard cell exits immediately, run the diagnostic cell:

```python
dashboard_output.show()
```

Also check:

```text
logs/dashboard.log
```

If you see NumPy/GDAL compatibility errors, confirm that the environment uses `numpy<2`:

```bash
python -c "import numpy; print(numpy.__version__)"
```

If `openvisuspy` or `OpenVisus` cannot be imported, rerun:

```bash
pip install -r requirements.txt
```
