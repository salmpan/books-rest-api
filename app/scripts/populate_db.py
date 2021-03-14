from django.db import transaction
#
from books import models
from datetime import datetime


@transaction.atomic
def populate_authors():
    print("Adding authors...")
    authors = [
        models.Author(
            id=1,
            first_name="Kurt",
            last_name="Vonnegut",
            birthday=datetime(1922, 11, 11),
            email="vonnegut@mail.com"
        ),
        models.Author(
            id=2,
            first_name="Ray",
            last_name="Bradbury",
            birthday=datetime(1920, 8, 22),
            email="bradbury@mail.com"
        ),
        models.Author(
            id=3,
            first_name="Isaac",
            last_name="Asimov",
            birthday=datetime(1920, 1, 2),
            email="asimov@mail.com"
        ),
        models.Author(
            id=4,
            first_name="Philip K.",
            last_name="Dick",
            birthday=datetime(1928, 12, 16),
            email="dick@mail.com"
        ),
        models.Author(
            id=5,
            first_name="George",
            last_name="Orwell",
            birthday=datetime(1903, 6, 25),
            email="orwell@mail.com"
        )
    ]

    models.Author.objects.bulk_create(authors)


@transaction.atomic
def populate_publishers():
    print("Adding publishers...")
    publishers = [
        models.Publisher(
            id=1,
            name="HarperCollins Publishers",
            address="London, United Kingdom",
        ),
        models.Publisher(
            id=2,
            name="Random House USA Inc",
            address="New York, United States",
        ),
        models.Publisher(
            id=3,
            name="Bantam Doubleday Dell Publishing Group Inc",
            address="New York, United States"
        ),
        models.Publisher(
            id=4,
            name="Orion Publishing Co",
            address="London, United Kingdom",
        ),
        models.Publisher(
            id=5,
            name="Penguin Books Ltd",
            address="London, United Kingdom",
        ),
        models.Publisher(
            id=6,
            name="Vintage Publishing",
            address="London, United Kingdom",
        )
    ]

    models.Publisher.objects.bulk_create(publishers)


@transaction.atomic
def populate_books():
    print("Adding books...")
    books = [
        models.Book(
            id=1,
            title="Fahrenheit 451",
            description = ("Fahrenheit 451 is a 1953 dystopian novel by American writer Ray Bradbury."
                "Often regarded as one of his best works, the novel presents a future American society where"
                "books are outlawed and firemen burn any that are found."),
            isbn="9780006546061",
            pub_date=datetime(2019, 2, 7),
            author=models.Author.objects.get(id=2),
            publisher=models.Publisher.objects.get(id=1)
        ),
        models.Book(
            id=2,
            title="I, Robot",
            description=("I, Robot is a fixup novel of science fiction short stories or essays by"
                "American writer Isaac Asimov. The stories originally appeared in the American magazines"
                "Super Science Stories and Astounding Science Fiction between 1940 and 1950 and were"
                "then compiled into a book for stand-alone publication by Gnome Press in 1950, in an"
                "initial edition of 5,000 copies."),
            isbn="9780007491513",
            pub_date=datetime(2013, 4, 1),
            author=models.Author.objects.get(id=3),
            publisher=models.Publisher.objects.get(id=1)
        ),
        models.Book(
            id=3,
            title="Foundation and Empire",
            description=("Foundation and Empire is a science fiction novel by American writer Isaac Asimov"
                "originally published by Gnome Press in 1952. It is the second book in the Foundation Series,"
                "and the fourth in the in-universe chronology."),
            isbn="9780553293371",
            pub_date=datetime(1997, 4, 1),
            author=models.Author.objects.get(id=3),
            publisher=models.Publisher.objects.get(id=2)
        ),
        models.Book(
            id=4,
            title="Foundation And Earth",
            description=("Foundation and Earth is a science fiction novel by American writer Isaac Asimov,"
                "the fifth novel of the Foundation series and chronologically the last in the series."
                "It was published in 1986, four years after the first sequel to the Foundation trilogy,"
                "which is titled Foundation's Edge."),
            isbn="9780553587579",
            pub_date=datetime(2004, 12, 15),
            author=models.Author.objects.get(id=3),
            publisher=models.Publisher.objects.get(id=1)
        ),
        models.Book(
            id=5,
            title="Do Androids Dream Of Electric Sheep?",
            description=("Do Androids Dream of Electric Sheep? (retitled Blade Runner: Do Androids Dream"
                "of Electric Sheep? in some later printings) is a dystopian science fiction novel by American"
                "writer Philip K. Dick, first published in 1968."),
            isbn="9780575094185",
            pub_date=datetime(2017, 11, 20),
            author=models.Author.objects.get(id=4),
            publisher=models.Publisher.objects.get(id=4)
        ),
        models.Book(
            id=6,
            title="1984",
            description=("Nineteen Eighty-Four: A Novel, often published as 1984, is a dystopian social"
                "science fiction novel by English novelist George Orwell. It was published on 8 June 1949"
                "by Secker & Warburg as Orwell's ninth and final book completed in his lifetime."),
            isbn="9780141036144",
            pub_date=datetime(2008, 10, 1),
            author=models.Author.objects.get(id=5),
            publisher=models.Publisher.objects.get(id=5)
        ),
        models.Book(
            id=7,
            title="Animal Farm",
            description=("Animal Farm is an allegorical novella by George Orwell, first published in"
                "England on 17 August 1945. The book tells the story of a group of farm animals who rebel"
                "against their human farmer, hoping to create a society where the animals can be equal,"
                "free, and happy."),
            isbn="9780141036137",
            pub_date=datetime(2008, 10, 1),
            author=models.Author.objects.get(id=5),
            publisher=models.Publisher.objects.get(id=5)
        ),
        models.Book(
            id = 8,
            title="Cat's Cradle",
            description=("Cat's Cradle is a satirical postmodern novel, with science fiction elements,"
                "by American writer Kurt Vonnegut. Vonnegut's fourth novel, it was first published in 1963,"
                "exploring and satirizing issues of science, technology, the purpose of religion,"
                "and the arms race, often through the use of black humor."),
            isbn="9780241951606",
            pub_date=datetime(2011, 4, 7),
            author=models.Author.objects.get(id=1),
            publisher=models.Publisher.objects.get(id=1)
        ),
        models.Book(
            id=9,
            title="Mother Night",
            description=("Mother Night is a novel by American author Kurt Vonnegut, first published"
                "in February 1962. The title of the book is taken from Goethe's Faust. The novel takes the"
                "form of the fictional memoirs of Howard W. Campbell Jr., an American, who moved to Germany"
                "in 1923 at age 11, and later became a well-known playwright and Nazi propagandist."),
            isbn="9780099819301",
            pub_date=datetime(2019, 3, 5),
            author=models.Author.objects.get(id=1),
            publisher=models.Publisher.objects.get(id=4)
        )
    ]

    models.Book.objects.bulk_create(books)


def run():
    try:
        populate_authors()
        populate_publishers()
        populate_books()
    except Exception as e:
        print(e)
