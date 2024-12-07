from django.db import migrations


def load_initial_data(apps, schema_editor):
    poi_model = apps.get_model('WanderWayBackend', 'POI')
    poi_model.objects.create(
        name="Stary Ratusz",
        description="Późnogotycki budynek na wrocławskim Rynku, jeden z najlepiej zachowanych historycznych ratuszy w Polsce, zarazem jeden z głównych zabytków architektonicznych Wrocławia.",
        latitude=51.109562,
        longitude=17.031937,
        imgURI = "placeholder.jpg"
    )
    poi_model.objects.create(
        name="Katerdra św. Jana Chrzciciela",
        description="Rzymskokatolicki gotycki kościół parafialny, położony na Ostrowie Tumskim - najstarszej części Wrocławia, położonej na lewym brzegu Odry.",
        latitude=51.114187,
        longitude=17.046563,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Hala Stulecia",
        description="Hala widowiskowo-sportowa we Wrocławiu, ekspresjonistyczna, wzniesiona w latach 1911–1913 według projektu Maxa Berga.",
        latitude=51.106938,
        longitude=17.077312,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Ogród Japoński",
        description="Ogród japoński znajdujący się w Parku Szczytnickim we Wrocławiu. Stanowi połączenie kilku typów ogrodów japońskich: publicznego, wodnego, związanego z ceremonią picia herbaty oraz kamienistej plaży.",
        latitude=51.109687,
        longitude=17.079062,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Zoo Wrocław",
        description="Ogród zoologiczny znajdujący się przy ul. Wróblewskiego 1–5 we Wrocławiu, otwarty 10 lipca 1865. Jest najstarszym na obecnych ziemiach polskich ogrodem zoologicznym w Polsce.",
        latitude=51.105688,
        longitude=17.076188,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Sky Tower",
        description="Neomodernistyczny wieżowiec we Wrocławiu, stanowiący wraz z dwoma sąsiadującymi budynkami kompleks mieszkalny, biurowy, handlowo-usługowy i rekreacyjny. Jest najwyższym budynkiem mieszkalnym we Wrocławiu i jednym z najwyższych w Polsce.",
        latitude=51.094562,
        longitude=17.018937,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Dworzec Świebodzki",
        description="Nieczynna stacja kolejowa w ścisłym centrum Wrocławia przy placu Orląt Lwowskich; najstarszy z trzech zachowanych do dziś pasażerskich dworców kolejowych we Wrocławiu.",
        latitude=51.108062,
        longitude=17.020063,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Galeria Neon Side",
        description="Najjaśniejsze podwórko Wrocławia - Ruska 46, rozświetlone zabytkowymi neonami, to miejsce skupiające organizacje kulturalne, galerie sztuki, zespoły muzyczne, kluby, teatry, organizacje pozarządowe i artystów freelancerów, którzy mają tu swoje siedziby lub pracownie.",
        latitude=51.109938,
        longitude=17.024563,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Hala Targowa",
        description="Hala targowa we Wrocławiu, zlokalizowana przy ul. Piaskowej 17, w pobliżu Rynku.",
        latitude=51.112562,
        longitude=17.039813,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Most Grunwaldzki",
        description="Most drogowy wiszący nad Odrą we Wrocławiu, zbudowany w latach 1908-1910. Początkowo most nosił nazwę Mostu Cesarskiego, a następnie Mostu Wolności.",
        latitude=51.109437,
        longitude=17.052563,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Muzeum Narodowe",
        description="Jedno z głównych muzeów Wrocławia i Dolnego Śląska. Zbiory muzeum obejmują przede wszystkim malarstwo i rzeźbę, ze szczególnym uwzględnieniem sztuki całego Śląska.",
        latitude=51.110937,
        longitude=17.047688,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Wrocławska Fontanna Multimedialna",
        description="Fontanna we Wrocławiu, otoczona pergolą, przy Hali Stulecia. Jest największą fontanną w Polsce i jedną z największych w Europie.",
        latitude=51.108812,
        longitude=17.078938,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Plac Nowy Targ",
        description="Jeden z trzech historycznych placów targowych Starego Miasta we Wrocławiu, obok Rynku i placu Solnego.",
        latitude=51.111312,
        longitude=17.038312,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Narodowe Forum Muzyki im. Witolda Lutosławskiego",
        description="Jeden z największych obiektów koncertowych w Europie mieszczący się we Wrocławiu oraz nazwa instytucji kultury powstałej w 2014 roku.",
        latitude=51.107062,
        longitude=17.026438,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Panorama Racławicka",
        description="Muzeum sztuki we Wrocławiu, oddział Muzeum Narodowego we Wrocławiu, założone w 1893 we Lwowie, od 1980 we Wrocławiu.",
        latitude=51.110312,
        longitude=17.044938,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Bastion Sakwowy",
        description="Fragment dawnych fortyfikacji miasta Wrocławia, w południowo-wschodnim ich narożniku. W latach 1948–2024 wzgórze nosiło nazwę Wzgórze Partyzantów.",
        latitude=51.104813,
        longitude=17.038562,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Teatr Muzyczny „Capitol”",
        description="Teatr muzyczny powstały we Wrocławiu w 2004 roku, będący kontynuacją wcześniejszych teatrów istniejących w tym samym miejscu takich jak: Operetka Dolnośląska (1955 – 1976), Teatr Muzyczny (1977 – 1979), Operetka Wrocławska (1979 – 1991) oraz Teatr Muzyczny – Operetka Wrocławska (1991 – 2004).",
        latitude=51.100562,
        longitude=17.029812,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Pałac Królewski we Wrocławiu",
        description="Zespół pałacowy stanowiący od XVIII do XX wieku wrocławską rezydencję pruskich królów z dynastii Hohenzollernów, obecnie siedziba Muzeum Miejskiego Wrocławia.",
        latitude=51.107437,
        longitude=17.028813,
        imgURI="placeholder.jpg"
    )
    poi_model.objects.create(
        name="Gmach główny Uniwersytetu Wrocławskiego",
        description="Barokowy budynek o długości 171 metrów, zbudowany w XVIII wieku na miejscu dawnego zamku piastowskiego. Powstał z inicjatywy cesarza Leopolda I jako siedziba Akademii Leopoldyńskiej.",
        latitude=51.114062,
        longitude=17.034438,
        imgURI="placeholder.jpg"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('WanderWayBackend', 'poi'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]


