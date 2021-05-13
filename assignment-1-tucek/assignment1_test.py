from assignment1 import Assignment1


def test_gene_symbol():
    a1 = Assignment1()
    assert a1.get_gene_symbol() == "RRP1B"


def test_get_region_of_gene():
    a1 = Assignment1()
    assert a1.get_region_of_gene() == "chr21:43659559-43696079"


def test_get_number_of_exons():
    a1 = Assignment1()
    assert a1.get_number_of_exons() == 16


def test_get_number_mapped_reads():
    a1 = Assignment1()
    assert a1.get_number_mapped_reads_of_gene() == 11821


def test_get_aligner_from_sam_header():
    a1 = Assignment1()
    assert a1.get_aligner_from_sam_header() == "novoalign"


def test_get_number_of_properly_paired_reads_of_gene():
    a1 = Assignment1()
    assert a1.get_number_of_properly_paired_reads_of_gene() == 11624


def test_calculate_average_genome_coverage_of_file():
    a1 = Assignment1()
    x = 47.15
    assert x - 1 <= a1.get_average_genome_coverage_of_file() <= x + 1





