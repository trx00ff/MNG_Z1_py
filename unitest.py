import unittest


class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["karolina.janiak@student.wat.edu.pl", True, False, "Karolina", "Janiak"],
            ["kamil.matusik@student.wat.edu.pl", True, True, "Kamil", "Matusik"],
            ["jerzy.stanik@wat.edu.pl", False, True, "Jerzy", "Stanik"],
            ["krzysztof.kanciak@wat.edu.pl", False, True, "Krzysztof", "Kanciak"],
            ["anna.zalewska@student.wat.edu.pl", True, False, "Anna", "Zalewska"],
            ["jolanta.kondratiuk@wat.edu.pl", False, False, "Jolanta", "Kondratiuk"],
            ["eliasz.nasur@student.wat.edu.pl", True, True, "Eliasz", "Nasur"],
            ["klaudia.kucharska@student.wat.edu.pl", True, False, "Klaudia", "Kucharska"],
            ["irena.eris@wat.edu.pl", False, False, "Irena", "Eris"],
            ["tobiasz.iksinski@wat.edu.pl", False, True, "Tobiasz", "Iksiński"],

        ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())


if __name__ == '__EmailExtractor__':
    unittest.main()
