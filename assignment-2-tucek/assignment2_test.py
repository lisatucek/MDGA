from assignment2 import Assignment2


def test_get_average_variant_quality_of_file():
    a2 = Assignment2()
    assert a2.get_average_variant_quality_of_file() == 5.0


def test_get_total_number_of_variants_of_file():
    a2 = Assignment2()
    assert a2.get_total_number_of_variants_of_file() == 4942


def test_get_vcf_fileformat():
    a2 = Assignment2()
    assert a2.get_vcf_fileformat() == "VCFv4.2"


def test_get_number_of_indels():
    a2 = Assignment2()
    assert a2.get_number_of_indels() == 320


def test_get_number_of_snvs():
    a2 = Assignment2()
    assert a2.get_number_of_snvs() == 4622


def test_get_number_of_heterozygous_variants():
    a2 = Assignment2()
    assert a2.get_number_of_heterozygous_variants() == 3803


