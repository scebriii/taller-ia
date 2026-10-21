def fcmax_tanaka(edad: float) -> float:
    if edad <= 0:
        raise ValueError("La edad debe ser positiva")
    return 208 - 0.7 * edad


print(fcmax_tanaka(20))
