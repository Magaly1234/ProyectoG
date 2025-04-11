import numpy as np
from scipy.spatial.transform import Rotation as R

def calcular_angulos(datos):
    if not datos:
        return {"dorsiflexion": 0, "abduccion": 0, "inversion": 0}

    gx1, gy1, gz1 = datos['giroscopio_x1'], datos['giroscopio_y1'], datos['giroscopio_z1']
    gx2, gy2, gz2 = datos['giroscopio_x2'], datos['giroscopio_y2'], datos['giroscopio_z2']

    rot1 = R.from_euler('xyz', [gx1, gy1, gz1], degrees=True)
    rot2 = R.from_euler('xyz', [gx2, gy2, gz2], degrees=True)

    angulos1 = rot1.as_euler('xyz', degrees=True)
    angulos2 = rot2.as_euler('xyz', degrees=True)

    dorsiflexion = angulos2[0] - angulos1[0]
    abduccion = angulos2[1] - angulos1[1]
    inversion = angulos2[2] - angulos1[2]

    return {"dorsiflexion": dorsiflexion, "abduccion": abduccion, "inversion": inversion}
