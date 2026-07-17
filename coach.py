class CoachAI:
    def __init__(self, username: str, sport: str):
        self.username = username
        self.sport = sport
        self.level = "Amateur"  # Todos empiezan como amateur
        self.streak_points = 0  # Puntaje de constancia

    def registrar_entrenamiento(self, minutos: int):
        """Suma puntos por entrenar y actualiza el nivel del deportista."""
        if minutos <= 0:
            raise ValueError("¡El tiempo de entrenamiento debe ser mayor a cero!")
        
        # Sumamos 10 puntos fijos por entrenar + 1 punto por cada 5 minutos
        puntos_ganados = 10 + (minutos // 5)
        self.streak_points += puntos_ganados
        
        # Lógica para subir de nivel [cite: 14]
        if self.streak_points >= 100:
            self.level = "Pro"
        elif self.streak_points >= 50:
            self.level = "Semi-Pro"
        else:
            self.level = "Amateur"
            
        return puntos_ganados
        