import os
from assignment3 import Assignment3


def test_get_number_of_annotated_variants():
    a3 = Assignment3()
    assert a3.get_number_of_annotated_variants() == 900


def test_get_list_of_genes():
    a3 = Assignment3()
    assert os.path.exists("annotation_result.json"), "The annotation JSON file does not exist"
    assert a3.get_list_of_genes() == 21 or len(a3.get_list_of_genes()) == 21


def test_get_num_variants_modifier():
    a3 = Assignment3()
    assert os.path.exists("annotation_result.json"), "The annotation JSON file does not exist"
    assert a3.get_num_variants_modifier() == 67


def test_get_num_variants_with_mutationtaster_annotation():
    a3 = Assignment3()
    assert os.path.exists("annotation_result.json"), "The annotation JSON file does not exist"
    assert a3.get_num_variants_with_mutationtaster_annotation() == 5


def test_view_vcf_in_browser():
    a3 = Assignment3()
    assert os.path.exists("annotation_result.json"), "The annotation JSON file does not exist"
    assert "vcf.iobio.io" in a3.view_vcf_in_browser()



