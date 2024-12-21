class Books:
    fp = 'yes'

    @classmethod
    def is_fP(cls):
        print()


maths = Books()
science = Books()
english = Books()


print()
print("maths:", maths.fp)
print("science:", science.fp)
print("english:", english.fp)


print()
science.fp = 'not available'
english.fp = 'available'
print("maths:", maths.fp)
print("science:", science.fp)
print("english:", english.fp)

