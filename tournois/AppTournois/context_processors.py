# Toujours en développement. Cela devrait permettre à terme de dérouler un fil d'Ariane pour savoir où on se situe dans le site
# La fonction breadcrumb prend une requête HTTP en entrée et renvoie un dictionnaire contenant une liste de dictionnaires. Chaque élément de cette liste représente une étape dans le fil d'Ariane. Le premier élément est toujours la page d'accueil du site.
# La fonction commence par récupérer le chemin d'accès (path) de la requête. Ensuite, elle découpe ce chemin en segments en utilisant le caractère / comme séparateur. Ces segments sont stockés dans une liste.
# Un parcours de cette liste est ensuite effectué pour chaque segment. La fonction essaie de trouver la vue correspondante à chaque segment en utilisant la fonction resolve de Django. Si la vue possède un attribut breadcrumb_name, cela signifie qu'elle a une appellation spéciale pour le fil d'Ariane. Dans ce cas, un dictionnaire contenant le nom de la vue et son URL est ajouté à la liste
# Importation de la fonction 'resolve' depuis le module 'django.urls'
from django.urls import resolve

# Définition de la fonction 'breadcrumb' prenant en argument une requête HTTP


def breadcrumb(request):
    # Récupération de l'URL de la requête HTTP
    path = request.path
    # Séparation de l'URL en une liste de parties
    path_list = path.split('/')[1:]
    # Initialisation d'une liste de miettes de pain (breadcrumb) commençant par la page d'accueil
    breadcrumb_list = [{'name': 'Home', 'url': '/'}]

    # Initialisation d'une variable contenant l'URL courante
    url_so_far = ''
    # Parcours des parties de l'URL
    for path_part in path_list:
        # Ajout de la partie courante à l'URL courante
        url_so_far += '/' + path_part
        # Tentative de résolution de la vue correspondant à l'URL courante
        try:
            view_func = resolve(url_so_far).func
            # Si la vue a un attribut 'breadcrumb_name', alors on ajoute une miette de pain à la liste
            if hasattr(view_func, 'breadcrumb_name'):
                breadcrumb_list.append(
                    {'name': view_func.breadcrumb_name, 'url': url_so_far})
        # Si la résolution de la vue échoue, on continue le parcours de l'URL
        except:
            pass

    # Retourne un dictionnaire contenant la liste des miettes de pain
    return {'breadcrumb_list': breadcrumb_list}
