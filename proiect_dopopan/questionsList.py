# tipul obiectului:
# [ intrebare, weight, [raspunsuri], raspuns corect ]

class Question:
    def __init__(self, text, weight, answers, right_answer):
        self.text = text
        self.weight = weight
        self.answers = answers
        self.right_answer = right_answer

    def show(self):
        print("intrebare: " + self.text + '\n' + "weight: " + str(self.weight))
        print("raspunsuri posibile: ")
        for ans in self.answers:
            print(ans)
        print("raspuns corect: " + self.right_answer)


questions = [
    Question("Care este numele celei mai mari companii tehnologice din Coreea de Sud?", 1,
             ['Apple', 'Google', 'Samsung'], 'Samsung'),
    Question("Care este capitala Portugaliei?", 1, [
             'Bucuresti', 'Lisabona', 'Madrid'], 'Lisabona'),
    Question("Care este simbolul chimic pentru argint?",
             1, ['Ag', 'Arg', 'Ar'], 'Ag'),
    Question("Care este cea mai mică pasăre din lume?", 1, [
             'Vrabia', 'Colibri', 'Randunica'], 'Colibri'),
    Question("Ce metal a fost descoperit de Hans Christian Oersted în 1825?", 2,
             ['Otel', 'Aluminiu', 'Metalul alcalin'], 'Aluminiu'),
    Question("Câte respirații are corpul uman zilnic?",
             2, ["20'000", "15'000", "25'000"], "20'000"),
    Question("In ce tara se gaseste reperul Taj Mahal?", 2, ['India', 'Emiratele Arabe Unite', 'Egipt'], 'India'),
    Question(
        "În ce an s-a scufundat Titanicul în Oceanul Atlantic, la 15 aprilie, în călătoria sa de fată din Southampton?",
        3, ['1910', '1911', '1912'], '1912'),
    Question("Câte inimi are o caracatiță?", 3,
             ['Doua', 'Trei', 'Sapte'], 'Trei'),
    Question("In ce tara se gaseste Statuia Libertatii?",
             3, ['UK', 'USA', 'Austria'], 'USA'),
    Question("Care este durata de viață a unei libelule?", 4,
             ['6 ore', '16 ore', '24 de ore'], '24 de ore'),
    Question("In ce an a castigat FC Arges primul titlu?",
             5, ['1968', '1972', '1979'], '1972'),
    Question("In ce an s-a nascut William Shakespeare?",
             5, ['1601', '1564', '1587'], '1564'),
    Question("Ce țară din America de Sud are cea mai mare suprafață?", 7, ['Brazilia', 'Argentina', 'Uruguay'],
             'Brazilia'),
    Question("Care este capitala Islandei?", 7, [
             'Reykjavik', 'Dublin', 'Cork'], 'Reykjavik')
]

for q in questions:
    q.show()
