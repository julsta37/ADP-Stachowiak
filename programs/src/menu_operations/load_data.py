import rasterio
from tkinter import filedialog, messagebox

from src.data_service import set_layer


def load_data_and_remember_outcome():
    layer = load_data()
    set_layer(layer)


def load_data():
    path = filedialog.askopenfilename(
        title="Wybierz warstwę rastrową",
        filetypes=[
            ("Pliki rastrowe", "*.tif *.tiff *.img *.jp2 *.vrt"),
            ("Wszystkie pliki", "*.*"),
        ],
    )

    if not path:
        return None

    try:
        # Odczytujemy wszystkie pasma do pamięci, żeby zamknąć plik zaraz po
        # wczytaniu i nie uzależniać dalszej pracy od otwartego uchwytu.
        with rasterio.open(path) as dataset:
            layer = {
                "data": dataset.read(),
                "crs": dataset.crs,
                "transform": dataset.transform,
                "bounds": dataset.bounds,
                "nodata": dataset.nodata,
                "width": dataset.width,
                "height": dataset.height,
                "count": dataset.count,
                "dtype": dataset.dtypes,
            }
    except Exception:
        messagebox.showwarning(
            "Błąd wczytywania",
            "Nie udało się wczytać wybranego pliku.\n"
            "Upewnij się, że jest to prawidłowy plik rastrowy.",
        )
        return None

    return layer
