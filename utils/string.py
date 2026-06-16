def normalize_speciality(name: str) -> str:
    """Normalise le nom d'une spécialité en l'écrivant avec la première lettre en majuscule et le reste en minuscule"""
    return name.strip().lower().capitalize()