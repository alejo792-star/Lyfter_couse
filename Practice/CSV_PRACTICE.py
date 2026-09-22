import csv
def read_series(ruta):
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        series = []
        for serie in lector:
            series.append(serie)
        return series
        

def filter_series(series, min_score, plataform):
    recomendation_series =[]
    for serie in series:
        if (float(serie["Score"]) >= min_score and plataform.lower() == serie["Platform"].lower()):
                recomendation_series.append(serie)
    return recomendation_series

def save_series(ruta, series):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        fieldnames = ["Name", "Platform", "Score"]
        writer = csv.DictWriter(archivo,fieldnames)
        writer.writeheader()
        writer.writerows(series)

def pedir_puntuacion():
    while True:
        try:
            puntuacion = float(input("Puntuación mínima: "))
            return puntuacion
        except ValueError:
            print("Debes escribir un número, por ejemplo 9.0.")


def main():
    series = read_series("series.csv")
    min_score = pedir_puntuacion()
    platform = input ("give a platformn")
    recomendadas = filter_series(series,min_score,platform)
    save_series("series_recomendadas.csv", recomendadas)
    print(f"Se guardaron {len(recomendadas)} series recomendadas.")


if __name__ == "__main__":
    main()


