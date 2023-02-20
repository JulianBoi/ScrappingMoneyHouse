from numpy import array


def multi_single_tab(array_multiple):
    # définir le tableau multidimensionnel
    multi_array = array(array_multiple)

    # utiliser la fonction flatten pour fusionner en un seul tableau
    flat_array = multi_array.flatten()

    return flat_array