from datetime import datetime

def current_year(request):
    """Añade el año actual al contexto de las plantillas como 'year'."""
    return {'year': datetime.now().year}
