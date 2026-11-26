import matplotlib.pyplot as plt
import numpy as np

from src.data_service import get_layer


def show_layer():
    layer = get_layer()

    if layer is None:
        return

    data = np.asarray(layer["data"])
    if data.ndim != 3 or data.shape[0] == 0:
        return

    nodata = layer.get("nodata")

    def stretch(band):
        band = band.astype(float)
        valid = np.isfinite(band)
        if nodata is not None:
            valid &= band != nodata
        if not np.any(valid):
            return np.zeros(band.shape, dtype=float)

        low, high = np.percentile(band[valid], (2, 98))
        if high <= low:
            high = low + 1
        result = np.zeros(band.shape, dtype=float)
        result[valid] = np.clip((band[valid] - low) / (high - low), 0, 1)
        return result

    if data.shape[0] >= 3:
        # Dla danych wielopasmowych pokaż trzy pierwsze pasma jako RGB.
        image = np.dstack([stretch(data[index]) for index in range(3)])
        cmap = None
    else:
        image = stretch(data[0])
        cmap = "gray"

    plt.figure("Warstwa rastrowa")
    plt.imshow(image, cmap=cmap, origin="upper")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
