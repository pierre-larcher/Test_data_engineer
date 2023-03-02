"""Description.

Tests automatiques de la première partie.
"""

from lib_first import exercise_one, find_missing_nb, sort_positive_element

test_output = "1\n2\nThree\n4\nFive\nThree\n7\n8\nThree\nFive\n11\nThree\n13\n14\nThreeFive\n16\n17\nThree\n19\nFive\nThree\n22\n23\nThree\nFive\n26\nThree\n28\n29\nThreeFive\n31\n32\nThree\n34\nFive\nThree\n37\n38\nThree\nFive\n41\nThree\n43\n44\nThreeFive\n46\n47\nThree\n49\nFive\nThree\n52\n53\nThree\nFive\n56\nThree\n58\n59\nThreeFive\n61\n62\nThree\n64\nFive\nThree\n67\n68\nThree\nFive\n71\nThree\n73\n74\nThreeFive\n76\n77\nThree\n79\nFive\nThree\n82\n83\nThree\nFive\n86\nThree\n88\n89\nThreeFive\n91\n92\nThree\n94\nFive\nThree\n97\n98\nThree\nFive\n"


def test_first_exercise():
    resultat = exercise_one()
    return resultat == test_output


def test_second_exercise():
    liste = [6, 2, 3, 1, 4]
    resultat = find_missing_nb(liste)
    return resultat == 5


def test_third_exercise():
    liste = [-6, 2, 3, -1, 4]
    resultat = sort_positive_element(liste)
    return resultat == [-6, 2, 3, -1, 4]


def test_third_exercise_doublons():
    liste = [-6, 2, 3, -1, 4, 2]
    resultat = sort_positive_element(liste)
    return resultat == [-6, 2, 2, -1, 3, 4]
