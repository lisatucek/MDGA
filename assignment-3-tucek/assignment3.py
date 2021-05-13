#! /usr/bin/env python3

import vcf
import httplib2
import os.path
import json

__author__ = 'Lisa Tucek'


##
##
## Aim of this assignment is to annotate the variants with various attributes
## We will use the API provided by "myvariant.info" - more information here: https://docs.myvariant.info
## NOTE NOTE! - check here for hg38 - https://myvariant.info/faq
## 1) Annotate the first 900 variants in the VCF file
## 2) Store the result in a data structure (not in a database)
## 3) Use the data structure to answer the questions
##
## 4) View the VCF in a browser
##

class Assignment3:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)

        self.vcf_path = "hg_chr16.vcf"
        self.annotation_result_path = "annotation_result.json"

        ## Call annotate_vcf_file here
        if not os.path.isfile(self.annotation_result_path):
            self.annotate_vcf_file()
        
        with open(self.annotation_result_path) as file:
            self.annotation = json.load(file)


    def annotate_vcf_file(self):
        ## Build the connection
        h = httplib2.Http()
        headers = {'content-type': 'application/x-www-form-urlencoded'}
                
        params_pos = []  # List of variant positions
        with open(self.vcf_path) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for counter, record in enumerate(vcf_reader):
                params_pos.append(record.CHROM + ":g." + str(record.POS) + record.REF + ">" + str(record.ALT[0]))
                
                if counter >= 899:
                    break
        
        ## Build the parameters using the list we just built
        params = 'ids=' + ",".join(params_pos) + '&hg38=true'
        
        ## Perform annotation
        res, con = h.request('http://myvariant.info/v1/variant', 'POST', params, headers=headers)
        annotation_result = con.decode('utf-8')
    
        file = open("annotation_result.json", "w")
        file.write(annotation_result)
        file.close()


    def get_number_of_annotated_variants(self):
        num_annotated_variants = len(self.annotation)
        return num_annotated_variants


    def get_list_of_genes(self):
        '''
        Print the name of genes in the annotation data set
        :return:
        '''
        print("TODO")
    
    
    def get_num_variants_modifier(self):
        '''
        Print the number of variants with putative_impact "MODIFIER"
        :return:
        '''
        print("TODO")
        
    
    def get_num_variants_with_mutationtaster_annotation(self):
        count = 0
        for i in self.annotation:
            if "dbnsfp" in i:
                if i["dbnsfp"]["mutationtaster"]:
                    count += 1
        return count

    
    def view_vcf_in_browser(self):
        return "https://vcf.iobio.io/?species=Human&build=GRCh38&vcf=https%3A%2F%2Flf-proxy.iobio.io%2Fy83z-vg9r%2Fhg_chr16.vcf.gz&tbi=https%3A%2F%2Flf-proxy.iobio.io%2Fy83z-vg9r%2Fhg_chr16.vcf.gz.tbi"
            




