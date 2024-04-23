# TODO-1: add convert_to_letter_grade(score) function

def convert_to_letter_grade(score):
    """
    Converts a numerical score into a letter grade.

    Input:
        score (int or float): The numerical score to be converted into a letter grade.

    Output:
        str: The letter grade corresponding to the input score.

    Exception Raises:
        ValueError: If the input score is outside the range of 0 to 100.
        TypeError: If the input score is not an int or float.

    Sample Example:
        >>> convert_to_letter_grade(85)
        'B'
    """
    if not isinstance(score,(int, float)):
        raise TypeError("Score must be a numeric value.")

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    

    if score >= 90:
        return 'A'
    elif score >= 80 and score <= 89:
        return 'B'
    elif score >= 70 and score <= 79:
        return 'C'
    elif score >= 60 and score <= 69:
        return 'D'
    else:
        return 'F'



