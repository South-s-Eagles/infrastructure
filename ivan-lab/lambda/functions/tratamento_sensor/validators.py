def validate_sensor_data(data):
    errors = []
    print(type(data))
    # Validando batimento cardíaco (de 40 a 180 BPM)
    if not (0 <= float(data["batimento"]) <= 180):
        errors.append(f"Batimento fora do intervalo: {data['batimento']} BPM")

    # Validando cortisol (de 2.5 a 25 µg/dL)
    if not (0 <= float(data["cortisol"]) <= 75):
        errors.append(f"Cortisol fora do intervalo: {data['cortisol']} µg/dL")

    # Validando eletroencefalograma (de 0.5 a 40 Hz)
    if not (0.5 <= float(data["eletroencefalograma"]) <= 80):
        errors.append(f"Eletroencefalograma fora do intervalo: {data['eletroencefalograma']} Hz")

    # Validando glicose (de 70 a 140 mg/dL)
    if not (70 <= float(data["glicose"]) <= 140):
        errors.append(f"Glicose fora do intervalo: {data['glicose']} mg/dL")

    if not (33.0 <= float(data["temperatura"]) <= 40.5):
        errors.append(f"Temperatura fora do intervalo: {data['temperatura']} °C")

    # Validando latitude e longitude
    if not (-90 <= float(data["latitude"]) <= 90):
        errors.append(f"Latitude inválida: {data['latitude']}")
    if not (-180 <= float(data["longitude"]) <= 180):
        errors.append(f"Longitude inválida: {data['longitude']}")

    return errors