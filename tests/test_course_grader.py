import pytest
from course_grader import convert_to_letter_grade


# TODO-1: Add test_exact_grade_boundaries() function

class TestConversions:
    def test_exact_grade_boundaries(self):
        assert convert_to_letter_grade(90) == 'A'
        assert convert_to_letter_grade(89) == 'B'
        assert convert_to_letter_grade(80) == 'B'
        assert convert_to_letter_grade(79) == 'C'
        assert convert_to_letter_grade(70) == 'C'
        assert convert_to_letter_grade(69) == 'D'
        assert convert_to_letter_grade(60) == 'D'
        assert convert_to_letter_grade(59) == 'F'
        assert convert_to_letter_grade(0) == 'F'


    # TODO-2: Add test_invalid_numerical_score() function

    def test_invalid_numerical_score(self):
        with pytest.raises(ValueError) as valerror:
            convert_to_letter_grade(101)
        assert str(valerror.value) == "Score must be between 0 and 100."

        with pytest.raises(ValueError) as valerror:
            convert_to_letter_grade(-101)
        assert str(valerror.value) == "Score must be between 0 and 100."


    # TODO-3: Add test_non_numeric_input() function
    def test_non_numeric_input(self):
        with pytest.raises(TypeError) as tyerror:
            convert_to_letter_grade("maanya")
        assert str(tyerror.value) == "Score must be a numeric value."

        with pytest.raises(TypeError) as tyerror:
            convert_to_letter_grade([1,2,3])
        assert str(tyerror.value) == "Score must be a numeric value."

        with pytest.raises(TypeError) as tyerror:
            convert_to_letter_grade(None)
        assert str(tyerror.value) == "Score must be a numeric value."
