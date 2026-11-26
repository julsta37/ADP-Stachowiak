from tkinter import messagebox

from src.data_service import get_layer

def show_layer_info():
    layer = get_layer()

    if layer is None:
        return

    info = (
        f"Wymiary rastra: {layer['width']} × {layer['height']} pikseli\n"
        f"Liczba pasm: {layer['count']}\n"
        f"Typ danych: {', '.join(layer['dtype'])}\n"
        f"Układ współrzędnych: {layer['crs']}\n"
        f"Zasięg: {layer['bounds']}\n"
        f"Wartość NoData: {layer['nodata']}"
    )

    messagebox.showinfo(
        "Informacje o warstwie",
        info
    )
