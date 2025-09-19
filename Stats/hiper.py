import math

size_poblacion = 20   # tamaño de la población
exitos_en_pob = 7    # número de éxitos en la población
extracciones = 5    # número de extracciones
exitos_deseados = 3    # número de éxitos a evaluar

def hypergeom_pdf(size_poblacion, exitos_en_pob, extracciones, k):
    if k < 0 or k > extracciones or k > exitos_en_pob or extracciones - k > size_poblacion - exitos_en_pob:
        return 0.0
    return (math.comb(exitos_en_pob, k) * math.comb(size_poblacion - exitos_en_pob, extracciones - k)) / math.comb(size_poblacion, extracciones)

def hypergeom_cdf(size_poblacion, exitos_en_pob, extracciones, exitos_deseados):
    total = 0.0
    k_min = max(0, extracciones - (size_poblacion - exitos_en_pob))
    k_max = min(exitos_deseados, exitos_en_pob, extracciones)
    for k in range(k_min, k_max + 1):
        total += hypergeom_pdf(size_poblacion, exitos_en_pob, extracciones, k)
    return total

print("pdf: ", hypergeom_pdf(size_poblacion, exitos_en_pob, extracciones, exitos_deseados))
print("cdf: ", hypergeom_cdf(size_poblacion, exitos_en_pob, extracciones, exitos_deseados))

