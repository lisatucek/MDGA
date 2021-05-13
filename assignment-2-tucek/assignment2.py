#! /usr/bin/env python3

import vcf

__author__ = 'Lisa Tucek'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_variant_quality_of_file(self):
        vcf_reader = vcf.Reader(open('chr21_new.vcf', 'r'))
        count = 0
        sum_qual = 0
        for record in vcf_reader:
            count += 1
            sum_qual += record.QUAL
        average_qual = sum_qual/count
        return average_qual
        
        
    def get_total_number_of_variants_of_file(self):
        vcf_reader = vcf.Reader(open('chr21_new.vcf', 'r'))
        count = 0
        for record in vcf_reader:
            count += 1
        return count
    
    
    def get_vcf_fileformat(self):
        vcf_reader = vcf.Reader(open('chr21_new.vcf', 'r'))
        fileformat = vcf_reader.metadata['fileformat']
        return fileformat


    def get_number_of_indels(self):
        vcf_reader = vcf.Reader(open('chr21_new.vcf', 'r'))
        count = 0
        for record in vcf_reader:
            if record.is_indel:
                count += 1
        return count


    def get_number_of_snvs(self):
        vcf_reader = vcf.Reader(open('chr21_new.vcf', 'r'))
        count = 0
        for record in vcf_reader:
            if record.is_snp:
                count += 1
        return count


    def get_number_of_heterozygous_variants(self):
        vcf_reader = vcf.Reader(open('chr21_new.vcf', 'r'))
        count = 0
        sum_het = 0
        for record in vcf_reader:
            count += 1
            sum_het += record.num_het
        return sum_het
