
# Models et champs

    * Source
        - nom_site : CharField
        - lien : URLField
    
    * Article
        - titre : CharField
        - source_image : URLField
        - date_publication : CharField
        - lien_detail : URLField
        - description : HTMLField
        - categorie : Foreignkey(Categorie)
        - tag : Foreignkey(Tag)
    
    * Categorie
        - nom : CharField
    
    * Tag
        - nom : CharField
