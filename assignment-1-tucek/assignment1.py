import pysam
import pybedtools

__author__ = 'Lisa Tucek'


class Assignment1:

    def __init__(self):
        self.bamfile_path = "chr21_small.bam"

    def get_gene_information(self):
        return {"symbol": "RRP1B",
                "refseq": "NM_015056",
                "chr": "chr21",
                "tx_start": 43659559,
                "tx_end": 43696079,
                "strand": "+",
                "num_exons": 16,
                "exons_start": "43659559,43669883,43672307,43673869,43674635,43675033,43676271,43676732,43683278,43684552,43685769,43686803,43687515,43690287,43691438,43693189",
                "exons_end": "43659794,43669966,43672365,43673955,43674697,43675163,43676336,43676914,43683373,43684650,43685789,43686935,43688240,43690440,43691502,43696079"
                }

    ## Return: gene symbol name
    def get_gene_symbol(self):
        return self.get_gene_information()["symbol"] # Dictionarys anschauen

    ## Return: chr:start-end
    def get_region_of_gene(self):
        gene_region = str(self.get_gene_information()["chr"]) + ":" + str(self.get_gene_information()["tx_start"]) + "-" + str(self.get_gene_information()["tx_end"])
        return gene_region

    ## Return the number of exons
    def get_number_of_exons(self):
        return self.get_gene_information()["num_exons"]

    ## Return the number of mapped reads within the gene
    def get_number_mapped_reads_of_gene(self): #pysam
        samfile = pysam.AlignmentFile(self.bamfile_path, "rb")
        count= 0
        for read in samfile.fetch(self.get_gene_information()["chr"], self.get_gene_information()["tx_start"], self.get_gene_information()["tx_end"]):
            if not read.is_unmapped:
                count += 1 
        return count

    ## Return the name of the aligner
    def get_aligner_from_sam_header(self):
        samfile = pysam.AlignmentFile(self.bamfile_path, "rb")
        head = samfile.header
        align = head["PG"][0]["PN"]
        return align

    ## Get the number of properly paired reads within the gene
    def get_number_of_properly_paired_reads_of_gene(self):
        samfile = pysam.AlignmentFile(self.bamfile_path, "rb")
        read_count= 0
        for read in samfile.fetch(self.get_gene_information()["chr"], self.get_gene_information()["tx_start"], self.get_gene_information()["tx_end"]):
            if not read.is_unmapped and read.is_proper_pair:
                read_count += 1 
        return read_count
        

    ## Calculate the average genome coverage of the file (not only of the gene of interest)
    ## Use bedtools - genome_coverage
    def get_average_genome_coverage_of_file(self):
        bedfile = pybedtools.bedtool.BedTool(self.bamfile_path)
        genome_coverage = bedfile.genome_coverage(bg=True)
        element_count = 0
        coverage_count = 0
        for element in genome_coverage:
            coverage_count += int(element[3])
            element_count += 1
        average_coverage = coverage_count / element_count
        return average_coverage
